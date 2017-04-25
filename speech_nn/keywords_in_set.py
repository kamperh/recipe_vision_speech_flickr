#!/usr/bin/env python

"""
Shows how often a set of keywords appear in a given set.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
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
    parser.add_argument("keywords_fn", type=str, help="keywords file")
    parser.add_argument("subset", type=str, help="obtain counts for this subset")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    features_dict_fn = "data/mfcc_cmvn_dd_vad/{}.npz".format(args.subset)
    print "Reading:", features_dict_fn
    features_dict = np.load(features_dict_fn)
    utterances = sorted(features_dict.keys())
    print "No. utterances:", len(utterances)

    label_dict_fn = "data/captions_content_dict.pkl"
    print "Reading:", label_dict_fn
    with open(label_dict_fn, "rb") as f:
        label_dict = pickle.load(f)

    print "Getting subset labels: {}".format(args.subset)
    label_dict_subset = {}
    for utt in utterances:
        label_dict_subset[utt] = label_dict[utt]

    print "Getting statistics for all words in {}".format(args.subset)
    word_tokens = []
    for utt in sorted(label_dict_subset):
        word_tokens.extend(label_dict_subset[utt])
    counter = Counter(word_tokens)

    print "Reading:", args.keywords_fn
    keywords = []
    with open(args.keywords_fn) as f:
        for line in f:
            keywords.append(line.strip())

    keyword_counter = Counter()
    for keyword in sorted(keywords):
        keyword_counter[keyword] = counter[keyword]
    print "Counts:", keyword_counter.most_common()

    print
    for keyword in sorted(keywords):
        print keyword, keyword_counter[keyword]


if __name__ == "__main__":
    main()
