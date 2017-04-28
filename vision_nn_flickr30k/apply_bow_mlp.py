#!/usr/bin/env python

"""
Apply a bag-of-word MLP to a set and output the sigmoids for each utterance.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from datetime import datetime
from os import path
import argparse
import cPickle as pickle
import numpy as np
import sys
import tensorflow as tf

sys.path.append(path.join("..", "..", "src", "tflego"))

from tflego.blocks import TF_DTYPE, NP_DTYPE
import train_bow_mlp


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument("model_dir", type=str, help="model directory")
    parser.add_argument(
        "subset", type=str, help="subset to apply model to", choices=["train", "dev", "test", "flickr8k"]
        )
    parser.add_argument("--batch_size", type=int, help="batch size (default: %(default)s)", default=1)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                             APPLY MLP FUNCTIONS                             #
#-----------------------------------------------------------------------------#


def apply_model(model_dir, subset, batch_size=1, config=None):
    
    # Load the model options
    options_dict_fn = path.join(model_dir, "options_dict.pkl")
    print "Reading:", options_dict_fn
    with open(options_dict_fn, "rb") as f:
        options_dict = pickle.load(f)

    # Data
    print datetime.now()
    if subset == "flickr8k":
        npz_fn = path.join(path.split(options_dict["data_dir"])[0], "flickr8k", "fc7.npz")
        print "Reading:", npz_fn
        features_dict = np.load(npz_fn)
        image_keys = sorted(features_dict.keys())
    else:
        npz_fn = path.join(options_dict["data_dir"], "fc7.npz")
        print "Reading:", npz_fn
        features_dict = np.load(npz_fn)
        subset_fn = path.join("..", "data", "flickr30k_" + subset + ".txt")
        print "Reading:", subset_fn
        image_keys = []
        with open(subset_fn, "r") as f:
            for line in f:
                image_keys.append(line.strip())
    input_x = np.array([features_dict[i] for i in image_keys], dtype=NP_DTYPE)
    print "Input items shape:", input_x.shape
    print datetime.now()

    # Batch feed iterator
    print "Batch size:", batch_size
    class BatchFeedIterator(object):
        def __init__(self, x_mat):
            self._x_mat = x_mat
        def __iter__(self):
            n_batches = int(np.float(self._x_mat.shape[0] / batch_size))
            for i_batch in xrange(n_batches):
                yield (
                    self._x_mat[
                        i_batch * batch_size:(i_batch + 1) * batch_size
                        ]
                    )
    apply_batch_iterator = BatchFeedIterator(input_x)

    # Build model
    x = tf.placeholder(TF_DTYPE, [None, options_dict["d_in"]])
    mlp = train_bow_mlp.build_bow_mlp_from_options_dict(x, 1.0, options_dict)
    mlp = tf.sigmoid(mlp)

    # Run model
    print datetime.now()
    saver = tf.train.Saver()
    with tf.Session(config=config) as session:

        # Load model
        model_fn = path.join(model_dir, "model.n_epochs_{}.ckpt".format(options_dict["n_epochs_complete"]))
        print "Reading:", model_fn
        saver.restore(session, model_fn)

        # Apply model to batches
        sigmoid_output_dict = {}
        n_outputs = 0
        print "Passing batches through model"
        for cur_feed in apply_batch_iterator:
            cur_output = session.run(mlp, feed_dict={x: cur_feed})
            for i in xrange(cur_output.shape[0]):
                sigmoid_output_dict[image_keys.pop(0)] = cur_output[i, :]
                n_outputs += 1
        print "Processed {} inputs out of {}".format(n_outputs, input_x.shape[0])

    print datetime.now()
    return sigmoid_output_dict


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    # Slurm options
    import os
    if "OMP_NUM_THREADS" in os.environ:
        num_threads = int(os.environ["OMP_NUM_THREADS"])
        config = tf.ConfigProto(intra_op_parallelism_threads=num_threads) #, log_device_placement=True)
    else:
        config = None

    sigmoid_output_dict = apply_model(
        args.model_dir, args.subset, args.batch_size, config=config
        )
    sigmoid_output_dict_fn = path.join(args.model_dir, "sigmoid_output_dict." + args.subset + ".npz")
    print "Writing:", sigmoid_output_dict_fn
    np.savez_compressed(sigmoid_output_dict_fn, **sigmoid_output_dict)
    # with open(sigmoid_output_dict_fn, "wb") as f:
    #     pickle.dump(sigmoid_output_dict, f, -1)


if __name__ == "__main__":
    main()
