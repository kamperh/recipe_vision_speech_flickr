#!/usr/bin/env python

"""
Train a bag-of-words MLP on top of Flickr30k VGG16 features.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

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
from tflego.blocks import TF_DTYPE, TF_ITYPE, NP_DTYPE


#-----------------------------------------------------------------------------#
#                           DEFAULT TRAINING OPTIONS                          #
#-----------------------------------------------------------------------------#

default_options_dict = {
    "data_dir": "data/flickr30k", # "data/temp", # 
    "label_dict": "captions_word_ids_content_dict.pkl", # "captions_word_ids_dict.pkl", # 
    "model_dir": "models/train_bow_mlp",
    "n_max_epochs": 25,
    "batch_size": 64,  # 64
    "ff_keep_prob": 0.75,
    "n_most_common": 1000,  # 3000
    "n_hiddens": [1024, 1024, 1024, 1024],
    # "optimizer": {
    #     "type": "sgd",
    #     "learning_rate": 0.001
    # },
    "optimizer": {
        "type": "adam",
        "learning_rate": 0.0001
    },
    "detect_sigmoid_threshold": 0.5,
    "train_bow_type": "single",  # "single", "average", "top_k"
    "rnd_seed": 2,
    }


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
    # if len(sys.argv) == 1:
    #     parser.print_help()
    #     sys.exit(1)
    return parser.parse_args()


def load_flickr30k_bow_labelled(data_dir, subset, label_dict, n_bow, 
        bow_type="single"):
    """
    Return the Flickr30k image matrices and bag-of-word label vectors.

    Parameters
    ----------
    bow_type : str
        How should the multiple captions be handled in constructing the
        bag-of-words vector: "single" assigns 1 to a word that occurs in any of
        the captions; "average" sums the word counts and then divides by the
        number of captions; "top_k" keeps only the top k most common words.
    """

    assert subset in ["train_no8ktrain", "dev", "test"]

    # Load data and shuffle
    npz_fn = path.join(data_dir, "fc7.npz")
    print "Reading:", npz_fn
    features_dict = np.load(npz_fn)
    subset_fn = path.join("..", "data", "flickr30k_" + subset + ".txt")
    print "Reading:", subset_fn
    image_keys = []
    with open(subset_fn, "r") as f:
        for line in f:
            image_keys.append(line.strip())
    np.random.shuffle(image_keys)
    x = np.array([features_dict[i] for i in image_keys], dtype=NP_DTYPE)

    # Bag-of-word vectors
    print datetime.now()
    print "Getting bag-of-word vectors"
    bow_vectors = np.zeros((len(x), n_bow), dtype=NP_DTYPE)
    if bow_type == "single":
        for i_data, image_key in enumerate(image_keys):
            for i_caption in xrange(5):
                label_key = "{}_{}".format(image_key, i_caption)
                if not label_key in label_dict:
                    print "Warning: Missing label " + label_key
                else:
                    for i_word in label_dict[label_key]:
                        bow_vectors[i_data, i_word] = 1
    elif bow_type == "average":
        for i_data, image_key in enumerate(image_keys):
            for i_caption in xrange(5):
                label_key = "{}_{}".format(image_key, i_caption)
                if not label_key in label_dict:
                    print "Warning: Missing label " + label_key
                else:
                    for i_word in label_dict[label_key]:
                        bow_vectors[i_data, i_word] += 1
            bow_vectors[i_data, :] = bow_vectors[i_data, :]/5.
    elif bow_type == "top_k":
        k = 10
        for i_data, image_key in enumerate(image_keys):
            cur_count_vector = np.zeros(n_bow, dtype=NP_DTYPE)
            for i_caption in xrange(5):
                label_key = "{}_{}".format(image_key, i_caption)
                if not label_key in label_dict:
                    print "Warning: Missing label " + label_key
                else:
                    for i_word in label_dict[label_key]:
                        cur_count_vector[i_word] += 1
            top_k_indices = cur_count_vector.argsort()[-k:][::-1]
            bow_vectors[i_data, top_k_indices] = 1
    else:
        assert False

    # # Temp
    # word_to_id_fn = path.join(data_dir, "word_to_id_content.pkl")
    # print "Reading:", word_to_id_fn
    # with open(word_to_id_fn, "rb") as f:
    #     word_to_id = pickle.load(f)
    # id_to_word = dict([(i[1], i[0]) for i in word_to_id.iteritems()])
    # for i_data in xrange(len(image_keys)):
    #     print image_keys[i_data]
    #     print bow_vectors[i_data]
    #     print [id_to_word[i] for i in np.where(bow_vectors[i_data, :])[0]]
    #     assert False

    return x, bow_vectors

# def load_flickr30k_bow_labelled(data_dir, subset, label_dict, n_bow):
#     """Return the Flickr30k image matrices and bag-of-word label vectors."""

#     assert subset in ["train", "dev", "test"]

#     # Load data
#     npz_fn = path.join(data_dir, "fc7.npz")
#     print "Reading:", npz_fn
#     features_dict = np.load(npz_fn)
#     subset_fn = path.join(data_dir, subset + ".txt")
#     print "Reading:", subset_fn
#     image_keys = []
#     with open(subset_fn, "r") as f:
#         for line in f:
#             image_keys.append(line.strip())

#     # Bag-of-word vectors
#     print datetime.now()
#     print "Getting bag-of-word vectors"
#     x = []
#     bow_vectors = []
#     for image_key in image_keys:
#         for i_caption in xrange(5):
#             label_key = "{}_{}".format(image_key, i_caption)
#             if not label_key in label_dict:
#                 print "Warning: Missing label " + label_key
#             else:
#                 bow_vector = np.zeros(n_bow, dtype=NP_DTYPE)
#                 for i_word in label_dict[label_key]:
#                     bow_vector[i_word] = 1
#                 x.append(features_dict[image_key])
#                 bow_vectors.append(bow_vector)

#     # Shuffle
#     print "Suffling data"
#     shuffle_indices = range(len(x))
#     random.shuffle(shuffle_indices)
#     x_shuffle = []
#     bow_vectors_shuffle = []
#     for i_data in shuffle_indices:
#         x_shuffle.append(x[i_data])
#         bow_vectors_shuffle.append(bow_vectors[i_data])

#     return np.array(x_shuffle, dtype=NP_DTYPE), np.array(bow_vectors, dtype=NP_DTYPE)


#-----------------------------------------------------------------------------#
#                              TRAINING FUNCTIONS                             #
#-----------------------------------------------------------------------------#


def build_bow_mlp_from_options_dict(x, keep_prob, options_dict):
    mlp = blocks.build_feedforward(x, options_dict["n_hiddens"], keep_prob)
    with tf.variable_scope("ff_layer_final"):
        mlp = blocks.build_linear(mlp, options_dict["d_out"])
        print "Final linear layer shape:", mlp.get_shape().as_list()
    return mlp


def train_bow_mlp(options_dict=None, config=None, model_dir=None):
    """Train and save a bag-of-words MLP."""

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

    # Model filename
    n_epochs_post_complete = epoch_offset + options_dict["n_max_epochs"]
    model_fn = path.join(model_dir, "model.n_epochs_{}.ckpt".format(n_epochs_post_complete))

    # Random seeds
    random.seed(options_dict["rnd_seed"])
    np.random.seed(options_dict["rnd_seed"])
    tf.set_random_seed(options_dict["rnd_seed"])


    # LOAD AND FORMAT DATA

    # Read word ID labels
    label_dict_fn = path.join(options_dict["data_dir"], options_dict["label_dict"])
    print "Reading:", label_dict_fn
    with open(label_dict_fn, "rb") as f:
        label_dict = pickle.load(f)

    # Filter out uncommon words (assume IDs sorted by count)
    print "Keeping most common words:", options_dict["n_most_common"]
    for image_key in sorted(label_dict):
        label_dict[image_key] = [i for i in label_dict[image_key] if i < options_dict["n_most_common"]]

    # Load image data
    train_x, train_y_bow = load_flickr30k_bow_labelled(
        options_dict["data_dir"], "train_no8ktrain", label_dict,
        options_dict["n_most_common"], bow_type=options_dict["train_bow_type"]
        )
    dev_x, dev_y_bow = load_flickr30k_bow_labelled(
        options_dict["data_dir"], "dev", label_dict, options_dict["n_most_common"]
        )
    print "Train items shape:", train_x.shape
    print "Dev items shape:", dev_x.shape

    # Dimensionalities
    d_in = train_x.shape[1]
    d_out = options_dict["n_most_common"]
    options_dict["d_in"] = d_in
    options_dict["d_out"] = d_out

    # Batch feed iterators
    class BatchFeedIterator(object):
        def __init__(self, x_mat, y_vec, keep_prob, shuffle_epoch=False):
            self._x_mat = x_mat
            self._y_vec = y_vec
            self._keep_prob = keep_prob
            self._shuffle_epoch = shuffle_epoch
        def __iter__(self):
            if self._shuffle_epoch:
                shuffle_indices = range(self._y_vec.shape[0])
                random.shuffle(shuffle_indices)
                self._x_mat = self._x_mat[shuffle_indices]
                self._y_vec = self._y_vec[shuffle_indices]
            n_batches = int(np.float(self._y_vec.shape[0] / options_dict["batch_size"]))
            for i_batch in xrange(n_batches):
                yield (
                    self._x_mat[
                        i_batch * options_dict["batch_size"]:(i_batch + 1) * options_dict["batch_size"]
                        ],
                    self._y_vec[
                        i_batch * options_dict["batch_size"]:(i_batch + 1) * options_dict["batch_size"]
                        ],
                    self._keep_prob
                    )
    train_batch_iterator = BatchFeedIterator(
        train_x, train_y_bow, options_dict["ff_keep_prob"], shuffle_epoch=True
        )
    val_batch_iterator = BatchFeedIterator(
        dev_x, dev_y_bow, 1.0, shuffle_epoch=False
        )


    # DEFINE MODEL

    print datetime.now()
    print "Building bag-of-words MLP"

    # Model
    x = tf.placeholder(TF_DTYPE, [None, d_in])
    y = tf.placeholder(TF_DTYPE, [None, d_out])
    keep_prob = tf.placeholder(TF_DTYPE)
    mlp = build_bow_mlp_from_options_dict(x, keep_prob, options_dict)

    # Training tensors
    loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(mlp, y))
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
        tf.greater_equal(tf.nn.sigmoid(mlp), options_dict["detect_sigmoid_threshold"]), TF_DTYPE
        )
    n_tp = tf.reduce_sum(prediction * y)
    n_pred = tf.reduce_sum(prediction)
    n_true = tf.reduce_sum(y)
    precision = n_tp/n_pred
    recall = n_tp/n_true
    fscore = 2.*precision*recall/(precision + recall)

    # TRAIN MODEL

    print(datetime.now())
    print "Training bag-of-words MLP"
    record_dict = training.train_fixed_epochs(
        options_dict["n_max_epochs"], optimizer, loss, train_batch_iterator,
        [x, y, keep_prob], [loss, precision, recall, fscore],
        val_batch_iterator, load_model_fn=load_model_fn,
        save_model_fn=model_fn, config=config, epoch_offset=epoch_offset
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
    options_dict["script"] = "train_bow_mlp"

    # Train model
    train_bow_mlp(options_dict, config, model_dir=args.model_dir)


if __name__ == "__main__":
    main()

