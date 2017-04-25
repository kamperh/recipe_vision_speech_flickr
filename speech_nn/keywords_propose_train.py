#!/usr/bin/env python

"""
Propose a potential keyword list after filtering out impossible words.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
from os import path
import cPickle as pickle
import matplotlib.pyplot as plt
import nltk
import numpy as np
import random


def main():
    
    n_most_common = 1000

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

    # subset = "dev"
    subset = "train"
    features_dict_fn = "data/mfcc_cmvn_dd_vad/{}.npz".format(subset)
    print "Reading:", features_dict_fn
    features_dict = np.load(features_dict_fn)
    utterances = sorted(features_dict.keys())
    print "No. utterances:", len(utterances)

    label_dict_fn = "data/captions_content_dict.pkl"
    print "Reading:", label_dict_fn
    with open(label_dict_fn, "rb") as f:
        label_dict = pickle.load(f)

    print "Getting subset labels: {}".format(subset)
    label_dict_subset = {}
    for utt in utterances:
        label_dict_subset[utt] = label_dict[utt]

    print "Getting statistics for all words in {}".format(subset)
    word_tokens = []
    for utt in sorted(label_dict_subset):
        word_tokens.extend(label_dict_subset[utt])

    # Plot zipf
    counter = Counter(word_tokens)
    counts = [i[1] for i in counter.most_common()]
    ranks = np.arange(1.0, len(counts) + 1.0)
    plt.figure()
    ax = plt.subplot(111)
    ax.scatter(ranks, counts, edgecolors="none")
    ax.set_yscale("log")
    ax.set_xscale("log")
    ax.set_xlabel("Rank of word")
    ax.set_ylabel("Count of word")
    ax.set_title("Zipf plot for all content words in {}".format(subset))

    print "Filtering words not in word IDs"
    word_tokens_filtered = []
    for utt in sorted(label_dict_subset):
        word_tokens_filtered.extend([i for i in label_dict_subset[utt] if i in word_to_id.keys()])
    print "No. word types:", len(set(word_tokens_filtered))
    word_tokens = word_tokens_filtered

    # Plot zipf
    counter_filtered = Counter(word_tokens)
    counts = [i[1] for i in counter_filtered.most_common()]
    ranks = np.arange(1.0, len(counts) + 1.0)
    plt.figure()
    ax = plt.subplot(111)
    ax.scatter(ranks, counts, edgecolors="none")
    ax.set_yscale("log")
    ax.set_xscale("log")
    ax.set_xlabel("Rank of word")
    ax.set_ylabel("Count of word")
    ax.set_title("Zipf plot for all content words in {} also in word IDs".format(subset))

    print "Filtering words according to count and POS"
    max_occur = 4000
    min_occur = 200
    word_tokens_filtered = []
    for word in word_tokens:
        pos = nltk.tag.pos_tag([word])[0][1]
        if min_occur < counter[word] < max_occur and pos not in ["IN"]:
            word_tokens_filtered.append(word)
    print "No. word types:", len(set(word_tokens_filtered))
    word_tokens = word_tokens_filtered

    # Sample keywords
    random.seed(2)
    n_keywords = 60
    keywords = []
    keywords = sorted(random.sample(set(word_tokens), n_keywords))
    print
    print "Proposed keywords:"
    for keyword, count in Counter(dict([(i, counter[i]) for i in counter if i in keywords])).most_common():
        print keyword, count, nltk.tag.pos_tag([keyword])[0][1]
    print

    fn = path.join("data", "keywords.txt")
    print "Writing:", fn
    with open(fn, "w") as f:
        f.write("\n".join(keywords))
        f.write("\n")

    # plt.show()


if __name__ == "__main__":
    main()
