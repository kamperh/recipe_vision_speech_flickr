#!/usr/bin/env python

"""
Analyze the given captions dictionary.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
import argparse
import cPickle as pickle
import sys


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument("captions_dict_fn", type=str, help="the captions dictionary")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    print "Reading:", args.captions_dict_fn
    with open(args.captions_dict_fn, "rb") as f:
        labels_dict = pickle.load(f)
    print "No. utterances:", len(labels_dict)

    word_tokens = []
    for utt in labels_dict:
        word_tokens.extend(labels_dict[utt])

    print "No. word tokens:", len(word_tokens)
    print "No. word types:", len(set(word_tokens))
    print "Most common words:", Counter(word_tokens).most_common(10)

    most_common_1k = [i[0] for i in Counter(word_tokens).most_common(1000)]
    word_tokens_1k = [i for i in word_tokens if i in most_common_1k]
    print "No. word tokens in 1k most common types: {} ({}%)".format(
        len(word_tokens_1k),
        float(len(word_tokens_1k)) / len(word_tokens) * 100
        )


if __name__ == "__main__":
    main()
