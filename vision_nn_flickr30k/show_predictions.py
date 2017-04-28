#!/usr/bin/env python

"""
Show bag-of-word label predictions by thresholding output.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

import argparse
import cPickle as pickle
import numpy as np
import sys


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument("sigmoid_npz", type=str, help="Numpy archive with sigmoid activations")
    parser.add_argument("word_to_id_pkl", type=str, help="pickled dictionary giving ID to word mapping")
    parser.add_argument(
        "--sigmoid_threshold", type=float,
        help="threshold for sigmoid output (default: %(default)s)", default=0.5
        )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()
    
    print "Reading:", args.sigmoid_npz
    sigmoid_dict = dict(np.load(args.sigmoid_npz))

    print "Reading:", args.word_to_id_pkl
    with open(args.word_to_id_pkl, "rb") as f:
        word_to_id = pickle.load(f)
    id_to_word = dict([(i[1], i[0]) for i in word_to_id.iteritems()])    

    print "Thresholding and mapping IDs to words"
    mapped_prediction_dict = {}
    for image_key in sigmoid_dict:
        mapped_prediction_dict[image_key] = [
            id_to_word[i] for i in np.where(sigmoid_dict[image_key] >= args.sigmoid_threshold)[0]
            ]

    # Print predictions
    print
    for image_key in sorted(mapped_prediction_dict):
        pred = mapped_prediction_dict[image_key]
        if len(pred) > 0:
            print "-"*79
            print "Image:", image_key
            print "Predicted:", pred
    print "-"*79
    print



if __name__ == "__main__":
    main()

