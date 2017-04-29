#!/usr/bin/env python

"""
Get a baseline based slimpy on unigram counts in the training data.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
from os import path
import argparse
import cPickle as pickle
import numpy as np
import os
import sys


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument(
        "subset", type=str, help="subset to get the baseline for", choices=["dev", "test"]
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

    n_most_common = 1000
    
    output_dir = "models/unigram_baseline"
    if not path.isdir(output_dir):
        os.mkdir(output_dir)

    word_to_id_dict_fn = "../vision_nn/data/flickr30k/word_to_id_content.pkl"
    print "Reading:", word_to_id_dict_fn
    with open(word_to_id_dict_fn, "rb") as f:
        word_to_id = pickle.load(f)

    print "Filtering word IDs to {} most common".format(n_most_common)
    word_to_id_most_common = {}
    for word in word_to_id:
        word_id = word_to_id[word]
        if word_id < n_most_common:
            word_to_id_most_common[word] = word_id
    word_to_id = word_to_id_most_common

    # Train and subset utterances
    features_dict_fn = "data/mfcc_cmvn_dd_vad/{}.npz".format("train")
    print "Reading:", features_dict_fn
    features_dict = np.load(features_dict_fn)
    train_utterances = sorted(features_dict.keys())
    features_dict_fn = "data/mfcc_cmvn_dd_vad/{}.npz".format(args.subset)
    print "Reading:", features_dict_fn
    features_dict = np.load(features_dict_fn)
    subset_utterances = sorted(features_dict.keys())
    print "No. train utterances:", len(train_utterances)
    print "No. {} utterances: {}".format(args.subset, len(subset_utterances))

    # Training counts
    label_dict_fn = "data/captions_content_dict.pkl"
    print "Reading:", label_dict_fn
    with open(label_dict_fn, "rb") as f:
        label_dict = pickle.load(f)
    label_dict_train = {}
    for utt in train_utterances:
        label_dict_train[utt] = label_dict[utt]
    word_tokens = []
    for utt in sorted(label_dict_train):
        word_tokens.extend(label_dict_train[utt])
    counter = Counter(word_tokens)
    print "No. word tokens in train:", len(word_tokens)
    print "Most common words:", counter.most_common(10)
    word_tokens_with_ids = []
    for word in word_tokens:
        if word in word_to_id:
            word_tokens_with_ids.append(word)
    counter = Counter(word_tokens_with_ids)
    print "No. word tokens with IDs in train:", len(word_tokens_with_ids)
    print "Most common words with IDs:", counter.most_common(10)

    # Unigram vector
    unigram_vector = np.zeros(n_most_common, dtype=np.float32)
    for word in word_to_id:
        i_word = word_to_id[word]
        unigram_vector[i_word] = float(counter[word])/len(word_tokens_with_ids)
    print "Unigram vector maximum:", max(unigram_vector)
    unigram_vector = unigram_vector/max(unigram_vector)

    # Unigram sigmoid_output_dict
    sigmoid_output_dict = {}
    for utt in sorted(subset_utterances):
        sigmoid_output_dict[utt] = unigram_vector
    sigmoid_output_dict_fn = path.join(output_dir, "sigmoid_output_dict." + args.subset + ".pkl")
    print "Writing:", sigmoid_output_dict_fn
    with open(sigmoid_output_dict_fn, "wb") as f:
        pickle.dump(sigmoid_output_dict, f, -1)

    # Other outputs required for valid model
    word_to_id_fn = path.join(output_dir, "word_to_id.pkl")
    print "Writing:", word_to_id_fn
    with open(word_to_id_fn, "wb") as f:
        pickle.dump(word_to_id, f, -1)
    options_dict_fn = path.join(output_dir, "options_dict.pkl")
    print "Writing:", options_dict_fn
    with open(options_dict_fn, "wb") as f:
        pickle.dump({"label_dict": "data/captions_content_dict.pkl"}, f, -1)


if __name__ == "__main__":
    main()
