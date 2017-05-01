#!/usr/bin/env python

"""
Train a bag-of-words CNN with the structure of [Palaz et al., IS'16].

The CNN architecture and loss is described in:

- D. Palaz, G. Synnaeve, and R. Collobert, "Jointly learning to locate and
  classify words using convolutional networks," in *Proc. Interspeech*, 2016

I refer to this architecture as the PSyC bag-of-words CNN, after **P**alaz,
**Sy**nnaeve, and **C**ollobert.

Note that the final CNN layer is linear, since using a final ReLU results in a
minimum value of 0 to the sigmoid-based loss, in turn yielding a minimum
sigmoid probability of 0.5.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
from datetime import datetime
from os import path
import argparse
import cPickle as pickle
import hashlib
import numpy as np
import os
import random
import sys
import tensorflow as tf

sys.path.append(path.join("..", "..", "src", "tflego"))

from tf0_12 import sequence_mask
from tflego import blocks
from tflego import training
from tflego.blocks import TF_DTYPE, TF_ITYPE
import data_io


#-----------------------------------------------------------------------------#
#                           DEFAULT TRAINING OPTIONS                          #
#-----------------------------------------------------------------------------#

default_options_dict = {
    "data_dir": "data/mfcc_cmvn_dd_vad", # "data/fbank_vad_tmp", # 
    "label_dict": "data/captions_content_dict.pkl", 
    "model_dir": "models/train_psyc",
    "n_padded": 800,
    "n_most_common": 1000,
    "n_max_epochs": 25,
    "batch_size": 64, # 128
    "ff_keep_prob": 1.0,
    "center_padded": False,
    # "optimizer": {
    #     "type": "sgd",
    #     "learning_rate": 0.1
    # },
    "optimizer": {
        "type": "adam",
        "learning_rate": 0.001
    },
    "filter_shapes": [
        [39, 9, 1, 96],  # [39, 9, 1, 64]
        [1, 10, 96, 96],
        [1, 10, 96, 96],
        [1, 10, 96, 96],
        [1, 10, 96, 96],
        [1, 10, 96, 1000],
        # [1, 10, 64, 256],
        # [1, 11, 256, 1000]
    ],
    "pool_shapes": [None]*6,
    # "filter_shapes": [
    #     [39, 9, 1, 64],
    #     [1, 10, 64, 256],
    #     # [1, 11, 256, 256],
    #     [1, 11, 256, 1000]
    # ],
    # "pool_shapes": [
    #     [1, 3],
    #     [1, 3],
    #     # [1, 3],
    #     None
    # ],
    "detect_sigmoid_threshold": 0.4,
    # "n_hiddens": [2048],
    "pooling": "logsumexp",  # "avg", "max", "logsumexp"
    "r": 1.0, # hyperparameter when logsumexp pooling is used above
    "rnd_seed": 42,
    }


#-----------------------------------------------------------------------------#
#                              TRAINING FUNCTIONS                             #
#-----------------------------------------------------------------------------#

def build_psyc_from_options_dict(x, x_lengths, keep_prob, options_dict):
    
    # ReLU CNN layers
    cnn = blocks.build_cnn(
        x, options_dict["input_shape"], options_dict["filter_shapes"][:-1],
        options_dict["pool_shapes"][:-1], padding="VALID"
        )

    # Linear CNN layer
    i_layer = len(options_dict["filter_shapes"]) - 1
    filter_shape = options_dict["filter_shapes"][-1]
    padding="VALID"
    with tf.variable_scope("cnn_layer_{}".format(i_layer)):
        cnn = blocks.build_conv2d_linear(cnn, filter_shape, padding=padding)
        print "CNN linear layer {} shape: {}".format(i_layer, cnn.get_shape().as_list())

    # Create mask
    n_padded_after_cnn = cnn.get_shape().as_list()[-2]
    # def get_lengths_after_cnn():
    lengths_after_cnn = tf.cast(x_lengths, dtype=TF_DTYPE)
    for i_cnn_layer in xrange(len(options_dict["pool_shapes"])):

        lengths_after_cnn = tf.maximum(
            1.0, lengths_after_cnn - options_dict["filter_shapes"][i_cnn_layer][1] + 1
            )
        # assert False, "check this"

        if options_dict["pool_shapes"][i_cnn_layer] is not None:
            lengths_after_cnn = tf.ceil(
                lengths_after_cnn / options_dict["pool_shapes"][i_cnn_layer][1]
                )
    # lengths_after_cnn = tf.cast(tf.minimum(float(n_padded_after_cnn), lengths_after_cnn), dtype=TF_ITYPE)
    mask = sequence_mask(lengths_after_cnn, n_padded_after_cnn)

    # Pooling
    with tf.variable_scope("pooling_final"):
        axis = 1
        if options_dict["pooling"] == "avg":
            assert cnn.get_shape().as_list()[axis] == 1
            cnn = tf.squeeze(cnn, [axis])
            cnn = cnn * tf.cast(mask, dtype=TF_DTYPE)[:, :, None]
            frame_scores = cnn
            cnn = tf.reduce_sum(
                cnn, reduction_indices=axis
                ) / tf.cast(lengths_after_cnn, dtype=TF_DTYPE)[:, None]
            print "Average pool layer shape:", cnn.get_shape().as_list()
        elif options_dict["pooling"] == "max":
            assert cnn.get_shape().as_list()[axis] == 1
            cnn = tf.squeeze(cnn, [axis])
            add_mask = tf.select(
                mask, tf.zeros_like(mask, dtype=tf.float32), -np.inf*tf.ones_like(mask, dtype=tf.float32)
                )
            frame_scores_masked = cnn + add_mask[:, :, None]
            frame_scores = frame_scores_masked
            # cnn = cnn * tf.cast(mask, dtype=TF_DTYPE)[:, :, None]
            cnn = tf.reduce_max(cnn, reduction_indices=axis)
            print "Max pool layer shape:", cnn.get_shape().as_list()
        elif options_dict["pooling"] == "logsumexp":
            assert "r" in options_dict
            assert cnn.get_shape().as_list()[axis] == 1

            # Logsumexp-trick to calculate logsumexp score
            cnn = tf.squeeze(cnn, [axis])
            add_mask = tf.select(
                mask, tf.zeros_like(mask, dtype=tf.float32), -np.inf*tf.ones_like(mask, dtype=tf.float32)
                )
            frame_scores_masked = cnn + add_mask[:, :, None]
            frame_scores = frame_scores_masked
            max_vec = tf.reduce_max(
                options_dict["r"]*frame_scores_masked, reduction_indices=axis, keep_dims=True
                )
            sequence_score_logsumexp_trick = 1./options_dict["r"] * (
                tf.log(1./tf.cast(lengths_after_cnn[:, None, None], dtype=TF_DTYPE))
                + tf.log(tf.reduce_sum(tf.exp(options_dict["r"]*frame_scores_masked
                - max_vec), reduction_indices=axis, keep_dims=True)) + max_vec
                )
            cnn = tf.squeeze(sequence_score_logsumexp_trick, [axis])
            print "Logsumexp pool layer shape:", cnn.get_shape().as_list()
        else:
            assert False

    # # Fully-connected and output layers, if specified
    # if "n_hiddens" in options_dict:
    #     cnn = blocks.build_feedforward(cnn, options_dict["n_hiddens"], keep_prob=keep_prob)
    # if "d_out" in options_dict:
    #     with tf.variable_scope("ff_layer_final"):
    #         cnn = blocks.build_linear(cnn, options_dict["d_out"])
    #         print "Final linear layer shape:", cnn.get_shape().as_list()

    return cnn, frame_scores


def train_psyc(options_dict=None, config=None, model_dir=None):
    """Train and save a PSyC CNN."""

    # PRELIMINARY

    assert (options_dict is not None) or (model_dir is not None)
    print datetime.now()

    # Output directory
    epoch_offset = 0
    load_model_fn = None
    if model_dir is None:
        hasher = hashlib.md5(repr(sorted(options_dict.items())).encode("ascii"))
        # hash_str = datetime.now().strftime("%y%m%d.%Hh%Mm%Ss") + "." + hasher.hexdigest()[:10]
        hash_str = hasher.hexdigest()[:10]
        model_dir = path.join(options_dict["model_dir"], hash_str)
        options_dict_fn = path.join(model_dir, "options_dict.pkl")
    else:
        # Start from previous model, if available
        options_dict_fn = path.join(model_dir, "options_dict.pkl")
        if path.isfile(options_dict_fn):
            print "Continuing from previous model"
            print "Reading:", options_dict_fn
            with open(options_dict_fn, "rb") as f:
                options_dict = pickle.load(f)
            epoch_offset = options_dict["n_epochs_complete"]
            print "Starting epoch:", epoch_offset            
            load_model_fn = path.join(model_dir, "model.n_epochs_{}.ckpt".format(epoch_offset))
    print "Model directory:", model_dir
    if not os.path.isdir(model_dir):
        os.makedirs(model_dir)
    print "Options:", options_dict

    # Model filenames
    n_epochs_post_complete = epoch_offset + options_dict["n_max_epochs"]
    model_fn = path.join(model_dir, "model.n_epochs_{}.ckpt".format(n_epochs_post_complete))
    best_model_fn = path.join(model_dir, "model.best_val.ckpt")

    # Random seeds
    random.seed(options_dict["rnd_seed"])
    np.random.seed(options_dict["rnd_seed"])
    tf.set_random_seed(options_dict["rnd_seed"])


    # LOAD AND FORMAT DATA

    # Read ground truth labels and determine most common words
    print "Reading:", options_dict["label_dict"]
    with open(options_dict["label_dict"], "rb") as f:
        label_dict = pickle.load(f)
    word_tokens = []
    for utt in label_dict:
        word_tokens.extend(label_dict[utt])
    word_to_id = dict([
        (j[0], i) for i, j in enumerate(Counter(word_tokens).most_common(options_dict["n_most_common"]))
        ])
    word_to_id_fn = path.join(model_dir, "word_to_id.pkl")
    print "Writing:", word_to_id_fn
    with open(word_to_id_fn, "wb") as f:
        pickle.dump(word_to_id, f, -1)

    # Load data into matrices
    train_x, train_y_bow, train_x_lengths = data_io.load_flickr8k_padded_bow_labelled(
        options_dict["data_dir"], "train", options_dict["n_padded"],
        label_dict, word_to_id, center_padded=options_dict["center_padded"]
        )
    dev_x, dev_y_bow, dev_x_lengths = data_io.load_flickr8k_padded_bow_labelled(
        options_dict["data_dir"], "dev", options_dict["n_padded"],
        label_dict, word_to_id, center_padded=options_dict["center_padded"]
        )
    test_x, test_y_bow, test_x_lengths = data_io.load_flickr8k_padded_bow_labelled(
        options_dict["data_dir"], "test", options_dict["n_padded"],
        label_dict, word_to_id, center_padded=options_dict["center_padded"]
        )
    train_x = np.swapaxes(train_x, 2, 1)
    dev_x = np.swapaxes(dev_x, 2, 1)
    test_x = np.swapaxes(test_x, 2, 1)
    print "Train items shape:", train_x.shape
    print "Dev items shape:", dev_x.shape
    print "Test items shape:", test_x.shape

    # Dimensionalities
    d_in = train_x.shape[1]*train_x.shape[2]
    d_out = len(word_to_id)
    input_shape = [-1, train_x.shape[1], train_x.shape[2], 1]  # [n_data, height, width, d_in]
    options_dict["d_in"] = d_in
    options_dict["d_out"] = d_out
    options_dict["input_shape"] = input_shape

    # Flatten data
    train_x = train_x.reshape((-1, d_in))
    dev_x = dev_x.reshape((-1, d_in))
    test_x = test_x.reshape((-1, d_in))

    # Batch feed iterators
    class BatchFeedIterator(object):
        def __init__(self, x_mat, x_lengths, y_vec, keep_prob, shuffle_epoch=False):
            self._x_mat = x_mat
            self._x_lengths = x_lengths
            self._y_vec = y_vec
            self._keep_prob = keep_prob
            self._shuffle_epoch = shuffle_epoch
        def __iter__(self):
            if self._shuffle_epoch:
                shuffle_indices = range(self._y_vec.shape[0])
                random.shuffle(shuffle_indices)
                self._x_mat = self._x_mat[shuffle_indices]
                self._x_lengths = self._x_lengths[shuffle_indices]
                self._y_vec = self._y_vec[shuffle_indices]
            n_batches = int(np.float(self._y_vec.shape[0] / options_dict["batch_size"]))
            for i_batch in xrange(n_batches):
                yield (
                    self._x_mat[
                        i_batch * options_dict["batch_size"]:(i_batch + 1) * options_dict["batch_size"]
                        ],
                    self._x_lengths[
                        i_batch * options_dict["batch_size"]:(i_batch + 1) * options_dict["batch_size"]
                        ],
                    self._y_vec[
                        i_batch * options_dict["batch_size"]:(i_batch + 1) * options_dict["batch_size"]
                        ],
                    self._keep_prob
                    )
    train_batch_iterator = BatchFeedIterator(
        train_x, train_x_lengths, train_y_bow, options_dict["ff_keep_prob"],
        shuffle_epoch=True
        )
    val_batch_iterator = BatchFeedIterator(
        dev_x, dev_x_lengths, dev_y_bow, 1.0
        )


    # DEFINE MODEL

    print datetime.now()
    print "Building bag-of-words PSyC CNN"

    # Model
    x = tf.placeholder(TF_DTYPE, [None, d_in])
    x_lengths = tf.placeholder(TF_ITYPE, [None])
    y = tf.placeholder(TF_DTYPE, [None, d_out])
    keep_prob = tf.placeholder(TF_DTYPE)
    cnn = build_psyc_from_options_dict(x, x_lengths, keep_prob, options_dict)
    cnn = cnn[0]

    # Training tensors
    loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(cnn, y))
    if options_dict["optimizer"]["type"] == "sgd":
        optimizer_class = tf.train.GradientDescentOptimizer
    elif options_dict["optimizer"]["type"] == "momentum":
        optimizer_class = tf.train.MomentumOptimizer
    elif options_dict["optimizer"]["type"] == "adagrad":
        optimizer_class = tf.train.AdagradOptimizer
    elif options_dict["optimizer"]["type"] == "adadelta":
        optimizer_class = tf.train.AdadeltaOptimizer
    elif options_dict["optimizer"]["type"] == "adam":
        optimizer_class = tf.train.AdamOptimizer
    optimizer_kwargs = dict([i for i in options_dict["optimizer"].items() if i[0] != "type"])
    optimizer = optimizer_class(**optimizer_kwargs).minimize(loss)

    # Test tensors
    prediction = tf.cast(
        tf.greater_equal(tf.nn.sigmoid(cnn), options_dict["detect_sigmoid_threshold"]), TF_DTYPE
        )
    n_tp = tf.reduce_sum(prediction * y)
    n_pred = tf.reduce_sum(prediction)
    n_true = tf.reduce_sum(y)
    precision = n_tp/n_pred
    recall = n_tp/n_true
    fscore = 2*precision*recall/(precision + recall)


    # TRAIN MODEL

    print(datetime.now())
    print "Training CNN"
    record_dict = training.train_fixed_epochs(
        options_dict["n_max_epochs"], optimizer, loss, train_batch_iterator,
        [x, x_lengths, y, keep_prob], [loss, precision, recall, -fscore],
        val_batch_iterator, load_model_fn=load_model_fn,
        save_model_fn=model_fn, config=config, epoch_offset=epoch_offset,
        save_best_val_model_fn=best_model_fn
        )

    # Save record
    record_dict_fn = path.join(model_dir, "record_dict.n_epochs_{}.pkl".format(n_epochs_post_complete))
    print "Writing:", record_dict_fn
    with open(record_dict_fn, "wb") as f:
        pickle.dump(record_dict, f, -1)

    # Save options_dict
    options_dict["n_epochs_complete"] = n_epochs_post_complete
    # options_dict_fn = path.join(model_dir, "options_dict.pkl")
    print("Writing: " + options_dict_fn)
    with open(options_dict_fn, "wb") as f:
        pickle.dump(options_dict, f, -1)

    print datetime.now()


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])#, add_help=False)
    parser.add_argument(
        "--model_dir", type=str,
        help="if provided, this is the path where the model will be stored "
        "and where previous models would be searched for",
        default=None
        )
    # parser.add_argument("--n_max_epochs", type=int, default=None)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    # Slurm options
    if "OMP_NUM_THREADS" in os.environ:
        num_threads = int(os.environ["OMP_NUM_THREADS"])
        config = tf.ConfigProto(intra_op_parallelism_threads=num_threads) #, log_device_placement=True)
    else:
        config = None

    # Set options
    options_dict = default_options_dict.copy()
    options_dict["script"] = "train_psyc"

    # Check model options: should match PSyC architecture
    assert not "n_hiddens" in options_dict  # no fully-connected layers
    assert options_dict["filter_shapes"][-1][-1] == options_dict["n_most_common"]
    # assert all([i is None for i in options_dict["pool_shapes"]])  # no pooling

    # Train model
    train_psyc(options_dict, config, model_dir=args.model_dir)


if __name__ == "__main__":
    main()
