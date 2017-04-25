#!/usr/bin/env python

"""
Analyze the speech features data in Numpy format.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2016, 2017
"""

from datetime import datetime
import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument("npz_fn", type=str, help="")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    print datetime.now()
    print "Reading:", args.npz_fn
    features_dict = np.load(args.npz_fn)
    print datetime.now()
    print "No. utterances:", len(features_dict.keys())

    print "Getting lengths"
    lengths = []
    for utt in sorted(features_dict):
        lengths.append(features_dict[utt].shape[0])
    print datetime.now()

    for len_threshold in [500, 600, 700, 800, 900, 1000]:
        print "No. of utterances longer than {}: {} out of {}".format(
            len_threshold, len([i for i in lengths if i >= len_threshold]),
            len(features_dict.keys())
            )

    print "Total duration: {:.2f} hours".format(sum(lengths)*100e-3/60.0/60.0)
    print datetime.now()

    plt.hist(lengths, 50, facecolor="green", alpha=0.75)
    plt.xlabel("lengths")
    plt.show()


if __name__ == "__main__":
    main()
