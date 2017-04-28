#!/usr/bin/env python

"""
Apply the VGG16 network to a directory of images.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from datetime import datetime
from os import path
from scipy.misc import imread, imresize
import argparse
import glob
import numpy as np
import os
import sys
import tensorflow as tf

import vgg16

TF_DTYPE = tf.float32
TF_ITYPE = tf.int32
weights_fn = path.join("data", "vgg16_weights.npz")


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument("input_dir", type=str, help="directory containing images")
    parser.add_argument("output_npz_fn", type=str, help="Numpy archive to write features too")
    parser.add_argument(
        "--output_layer", help="which VGG layer to use (default: %(default)s)",
        choices=["fc7", "prob"], default="fc7"
        )
    parser.add_argument("--batch_size", type=int, help="batch size (default: %(default)s)", default=1)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


def images_from_dir(directory, extension="jpg"):
    images_dict = {}
    for image_fn in sorted(glob.glob(path.join(directory, "*." + extension))):
        image = imread(image_fn, mode="RGB")
        image = imresize(image, (224, 224))
        images_dict[path.splitext(path.split(image_fn)[-1])[0]] = image
    return images_dict


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

    # Data
    print datetime.now()
    print "Reading directory:", args.input_dir
    images_dict = images_from_dir(args.input_dir)
    image_keys = sorted(images_dict.keys())
    print datetime.now()
    print "No. images:", len(images_dict)
    input_x = np.array([images_dict[i] for i in image_keys])

    # Batch feed iterator
    print "Batch size:", args.batch_size
    class BatchFeedIterator(object):
        def __init__(self, x_mat):
            self._x_mat = x_mat
        def __iter__(self):
            n_batches = int(np.float(self._x_mat.shape[0] / args.batch_size))
            for i_batch in xrange(n_batches):
                yield (
                    self._x_mat[
                        i_batch * args.batch_size:(i_batch + 1) * args.batch_size
                        ]
                    )
    apply_batch_iterator = BatchFeedIterator(input_x)

    # Pretrained weights
    assert path.isfile(weights_fn)
    print "Reading:", weights_fn
    weights = np.load(weights_fn)

    # Build model
    x = tf.placeholder(TF_DTYPE, [None, 224, 224, 3])
    vgg_dict, parameters = vgg16.build_vgg16(x)
    print "VGG output:", args.output_layer
    vgg_output = vgg_dict[args.output_layer]

    # Run model
    print datetime.now()
    init = tf.initialize_all_variables()
    with tf.Session(config=config) as session:
        session.run(init)

        print "Pretrained parameters"
        for i, key in enumerate(sorted(weights.keys())):
            print("{}: {}".format(key, list(weights[key].shape)))
            session.run(parameters[i].assign(weights[key]))

        # Apply model to batches
        output_dict = {}
        n_outputs = 0
        print datetime.now()
        print "Passing batches through model"
        for cur_feed in apply_batch_iterator:
            cur_output = session.run(vgg_output, feed_dict={x: cur_feed})
            for i in xrange(cur_output.shape[0]):
                # print "-"*79
                # print image_keys[0]
                output_dict[image_keys.pop(0)] = cur_output[i, :]
                n_outputs += 1
                # from imagenet_classes import class_names
                # predictions = (np.argsort(cur_output[i, :])[::-1])[0:5]
                # for p in predictions:
                #     print class_names[p], cur_output[i, :][p]

        print "Processed {} inputs out of {}".format(n_outputs, input_x.shape[0])

    print datetime.now()

    print "Writing:", args.output_npz_fn
    np.savez_compressed(args.output_npz_fn, **output_dict)


if __name__ == "__main__":
    main()


