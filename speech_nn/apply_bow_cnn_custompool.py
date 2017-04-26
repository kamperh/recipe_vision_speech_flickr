#!/usr/bin/env python

"""
Apply a bag-of-words CNN with custom pooling and output sigmoids.

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

from tflego.blocks import TF_DTYPE, TF_ITYPE
import data_io
import train_bow_cnn_custompool
import train_psyc


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument("model_dir", type=str, help="model directory")
    parser.add_argument(
        "subset", type=str, help="subset to apply model to", choices=["train", "dev", "test"]
        )
    parser.add_argument("--batch_size", type=int, help="batch size (default: %(default)s)", default=1)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                             APPLY CNN FUNCTIONS                             #
#-----------------------------------------------------------------------------#

def build_model(x, x_lengths, options_dict):
    if options_dict["script"] in ["train_bow_cnn_custompool", "train_visionspeech_cnn_custompool"]:
        cnn = train_bow_cnn_custompool.build_bow_cnn_custompool_from_options_dict(
            x, x_lengths, 1.0, options_dict
            )
        cnn = tf.sigmoid(cnn)
        return cnn
    # # Temp
    # elif options_dict["script"] == "train_visionspeech_cnn_custompool2":
    #     import train_visionspeech_cnn_custompool2
    #     cnn = train_visionspeech_cnn_custompool2.build_bow_cnn_custompool_from_options_dict(
    #         x, x_lengths, 1.0, options_dict
    #         )
    #     cnn = tf.sigmoid(cnn)
    #     return cnn        
    elif options_dict["script"] in ["train_psyc", "train_visionspeech_psyc"]:
        cnn, frame_scores = train_psyc.build_psyc_from_options_dict(
            x, x_lengths, 1.0, options_dict
            )
        cnn = tf.sigmoid(cnn)
        return cnn
    else:
        assert False


def apply_model(model_dir, subset, batch_size=1, config=None):

    # Load the model options
    options_dict_fn = path.join(model_dir, "options_dict.pkl")
    print "Reading:", options_dict_fn
    with open(options_dict_fn, "rb") as f:
        options_dict = pickle.load(f)

    # Load mapping dict
    word_to_id_fn = path.join(model_dir, "word_to_id.pkl")
    print "Reading:", word_to_id_fn
    with open(word_to_id_fn, "rb") as f:
        word_to_id = pickle.load(f)
    id_to_word = dict([(i[1], i[0]) for i in word_to_id.iteritems()])

    # Load input data
    input_npz_fn = path.join(
        options_dict["speech_data_dir"] if "speech_data_dir" in options_dict
        else options_dict["data_dir"], subset + ".npz"
        )
    print "Reading:", input_npz_fn
    features_dict = np.load(input_npz_fn)
    utterances = sorted(features_dict.keys())
    input_x = [features_dict[i] for i in utterances]
    padded_x, input_x_lengths = data_io.pad_sequences(
        input_x, options_dict["n_padded"], options_dict["center_padded"]
        )
    # # Temp
    # from train_visionspeech_cnn_custompool2 import pad_sequences
    # padded_x, input_x_lengths = pad_sequences(
    #     input_x, options_dict["n_padded"], options_dict["center_padded"]
    #     )
    input_x = np.swapaxes(padded_x, 2, 1)
    print "Input items shape:", input_x.shape
    d_in = input_x.shape[1]*input_x.shape[2]
    input_x = input_x.reshape((-1, d_in))

    # Batch feed iterator
    # if batch_size is None:
    #     batch_size = input_x.shape[0]
    print "Batch size:", batch_size
    class BatchFeedIterator(object):
        def __init__(self, x_mat, x_lengths):
            self._x_mat = x_mat
            self._x_lengths = x_lengths
        def __iter__(self):
            n_batches = int(np.float(self._x_mat.shape[0] / batch_size))
            for i_batch in xrange(n_batches):
                yield (
                    self._x_mat[
                        i_batch * batch_size:(i_batch + 1) * batch_size
                        ],
                    self._x_lengths[
                        i_batch * batch_size:(i_batch + 1) * batch_size
                        ]
                    )
    apply_batch_iterator = BatchFeedIterator(input_x, input_x_lengths)

    # Build model
    x = tf.placeholder(TF_DTYPE, [None, options_dict["d_in"]])
    x_lengths = tf.placeholder(TF_ITYPE, [None])
    cnn = build_model(x, x_lengths, options_dict)

    print datetime.now()

    # Launch the graph
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
            cur_output = session.run(cnn, feed_dict={x: cur_feed[0], x_lengths: cur_feed[1]})
            for i in xrange(cur_output.shape[0]):
                sigmoid_output_dict[utterances.pop(0)] = cur_output[i, :]
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
    sigmoid_output_dict_fn = path.join(args.model_dir, "sigmoid_output_dict." + args.subset + ".pkl")
    print "Writing:", sigmoid_output_dict_fn
    with open(sigmoid_output_dict_fn, "wb") as f:
        pickle.dump(sigmoid_output_dict, f, -1)


if __name__ == "__main__":
    main()
