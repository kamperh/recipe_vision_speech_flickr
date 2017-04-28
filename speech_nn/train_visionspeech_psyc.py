#!/usr/bin/env python

"""
Train a visually grounded spoken bag-of-words CNN with the structure of [Palaz
et al., IS'16].

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

from tflego import blocks
from tflego import training
from tflego.blocks import TF_DTYPE, TF_ITYPE
from train_psyc import build_psyc_from_options_dict
import data_io


#-----------------------------------------------------------------------------#
#                           DEFAULT TRAINING OPTIONS                          #
#-----------------------------------------------------------------------------#

default_options_dict = {
    "speech_data_dir": "data/mfcc_cmvn_dd_vad", # "data/fbank_vad_tmp", # 
    # "speech_data_dir": "data/fbank_vad",
    "speech_label_dict": "data/captions_content_dict.pkl", 
    # "visionsig_npz": "../vision_nn/models/train_bow_mlp/4bc0d1875f/sigmoid_output_dict.flickr8k.npz",  # 3000 classes
    "visionsig_npz": "../vision_nn/models/train_bow_mlp/d64b725040/sigmoid_output_dict.flickr8k.npz",  # 1000 classes 
    "word_to_id_dict": "../vision_nn/data/flickr30k/word_to_id_content.pkl", 
    "model_dir": "models/train_visionspeech_psyc",
    "visionsig_threshold": None,  # if None, sigmoids are used as targets directly
    "n_padded": 800,
    "n_most_common": 1000,  # needs to be less than the dimensionality of the
                            # vision sigmoids; if None, then the full vision
                            # dimensionality is used
    "n_max_epochs": 50,
    "batch_size": 128, # 128,
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
        [39, 9, 1, 64],
        [1, 10, 64, 64],
        [1, 10, 64, 64],
        [1, 10, 64, 64],
        [1, 10, 64, 64],
        [1, 10, 64, 1000],
        # [1, 10, 64, 256],
        # [1, 11, 256, 1000]
    ],
    "pool_shapes": [None]*6,
    "detect_sigmoid_threshold": 0.4,
    "pooling": "logsumexp",  # "avg", "max", "logsumexp"
    "r": 1., # hyperparameter when logsumexp pooling is used above
    "rnd_seed": 1,
    }


#-----------------------------------------------------------------------------#
#                              TRAINING FUNCTIONS                             #
#-----------------------------------------------------------------------------#

def train_visionspeech_psyc(options_dict=None, config=None, model_dir=None, extrinsic_eval=False):
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

    # Read ground truth labels, word IDs, and vision sigmoids
    print "Reading:", options_dict["speech_label_dict"]
    with open(options_dict["speech_label_dict"], "rb") as f:
        speech_label_dict = pickle.load(f)
    print "Reading:", options_dict["word_to_id_dict"]
    with open(options_dict["word_to_id_dict"], "rb") as f:
        word_to_id = pickle.load(f)
    print "Reading:", options_dict["visionsig_npz"]
    visionsig_dict = np.load(options_dict["visionsig_npz"])

    # Filter word_to_id with `n_most_common`
    if options_dict["n_most_common"] is None:
        options_dict["n_most_common"] = visionsig_dict[visionsig_dict.keys()[0]].shape[0]
    assert visionsig_dict[visionsig_dict.keys()[0]].shape[0] >= options_dict["n_most_common"]
    word_to_id_most_common = {}
    for word in word_to_id:
        word_id = word_to_id[word]
        if word_id < options_dict["n_most_common"]:
            word_to_id_most_common[word] = word_id
    word_to_id = word_to_id_most_common
    word_to_id_fn = path.join(model_dir, "word_to_id.pkl")
    print "Writing:", word_to_id_fn
    with open(word_to_id_fn, "wb") as f:
        pickle.dump(word_to_id, f, -1)

    # Load data into matrices
    train_x, train_y_visionsig, train_x_lengths = data_io.load_flickr8k_padded_visionsig(
        options_dict["speech_data_dir"], "train", options_dict["n_padded"],
        visionsig_dict, options_dict["n_most_common"],
        sigmoid_threshold=options_dict["visionsig_threshold"],
        center_padded=options_dict["center_padded"]
        )
    dev_x, dev_y_bow, dev_x_lengths = data_io.load_flickr8k_padded_bow_labelled(
        options_dict["speech_data_dir"], "dev", options_dict["n_padded"],
        speech_label_dict, word_to_id, center_padded=options_dict["center_padded"]
        )
    train_x = np.swapaxes(train_x, 2, 1)
    dev_x = np.swapaxes(dev_x, 2, 1)
    print "Train items shape:", train_x.shape
    print "Dev items shape:", dev_x.shape

    # Dimensionalities
    d_in = train_x.shape[1]*train_x.shape[2]
    d_out = options_dict["n_most_common"]
    input_shape = [-1, train_x.shape[1], train_x.shape[2], 1]  # [n_data, height, width, d_in]
    options_dict["d_in"] = d_in
    options_dict["d_out"] = d_out
    options_dict["input_shape"] = input_shape

    # Flatten data
    train_x = train_x.reshape((-1, d_in))
    dev_x = dev_x.reshape((-1, d_in))

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
        train_x, train_x_lengths, train_y_visionsig,
        options_dict["ff_keep_prob"], shuffle_epoch=True
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


    # EXTRINSIC EVALUATION

    if extrinsic_eval:

        print "Performing bag-of-word detection"

        from apply_bow_cnn_custompool import apply_model
        from eval_precision_recall import eval_precision_recall_fscore, eval_average_precision

        # Pass data through model
        tf.reset_default_graph()
        sigmoid_output_dict = apply_model(model_dir, "dev", 1, config=config)

        print "Thresholding and mapping IDs to words"
        id_to_word = dict([(i[1], i[0]) for i in word_to_id.iteritems()])
        word_output_dict = {}
        for utt in sigmoid_output_dict:
            word_output_dict[utt] = [
                id_to_word[i] for i in np.where(sigmoid_output_dict[utt] >=
                options_dict["detect_sigmoid_threshold"])[0]
                ]

        print "Evaluating output"
        analysis = eval_precision_recall_fscore(word_output_dict, speech_label_dict, False)
        n_tp = analysis[0]
        n_pred = analysis[1]
        n_true = analysis[2]
        precision = analysis[3]
        recall = analysis[4]
        f_score = analysis[5]
        average_precision = eval_average_precision(
            word_to_id, sigmoid_output_dict, speech_label_dict, False
            )

        print datetime.now()
        print
        print "-"*79
        print "Sigmoid threshold: {:.2f}".format(options_dict["detect_sigmoid_threshold"])
        print "No. predictions:", n_pred
        print "No. true tokens:", n_true
        print "Precision: {} / {} = {:.4f}%".format(n_tp, n_pred, precision*100.)
        print "Recall: {} / {} = {:.4f}%".format(n_tp, n_true, recall*100.)
        print "F-score: {:.4f}%".format(f_score*100.)
        print "Average precision: {:.4f}%".format(average_precision*100.)
        print "-"*79


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
    parser.add_argument("--extrinsic", help="perform extrinsic evaluation", action="store_true")
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
    options_dict["script"] = "train_visionspeech_psyc"

    # Train model
    train_visionspeech_psyc(options_dict, config, model_dir=args.model_dir, extrinsic_eval=args.extrinsic)


if __name__ == "__main__":
    main()
