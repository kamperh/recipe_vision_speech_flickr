#!/usr/bin/env python

"""
Get the ground truth Flickr8k captions.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
from datetime import datetime
from os import path
from nltk.corpus import stopwords
import cPickle as pickle

captions_fn = path.join("..", "kaldi_features", "data", "full_vad", "text")
data_dir = "data"


def main():

    print datetime.now()
    print "Reading:", captions_fn
    captions_dict = {}
    with open(captions_fn) as f:
        for line in f:
            line = line.strip().split()
            captions_dict[line[0]] = [i for i in line[1:] if "<" not in i and not "'" in i]
    print datetime.now()

    print "Filtering out stop words"
    captions_content_dict = {}
    for utt in captions_dict:
        captions_content_dict[utt] = [i for i in captions_dict[utt] if i not in stopwords.words("english")]
    print datetime.now()

    captions_dict_fn = path.join(data_dir, "captions_dict.pkl")
    captions_content_dict_fn = path.join(data_dir, "captions_content_dict.pkl")
    print "Writing:", captions_dict_fn
    with open(captions_dict_fn, "wb") as f:
        pickle.dump(captions_dict, f, -1)
    print "Writing:", captions_content_dict_fn
    with open(captions_content_dict_fn, "wb") as f:
        pickle.dump(captions_content_dict, f, -1)

    print datetime.now()


    # # Get word tokens
    # word_tokens = []
    # for utt in captions_dict:
    #     word_tokens.extend(captions_dict[utt])

    # print [i for i in set(word_tokens) if "<" in i]
    # print "Most common word types:", Counter(word_tokens).most_common(100)

    # # Analyze words
    # print
    # print "-"*79
    # print "Analysis of all words"
    # print "No. word tokens:", len(word_tokens)
    # print "No. word types:", len(set(word_tokens))
    # print "Most common word types:", Counter(word_tokens).most_common(10)
    # most_common_1k = [i[0] for i in Counter(word_tokens).most_common(1000)]
    # word_tokens_1k = [i for i in word_tokens if i in most_common_1k]
    # print "No. word tokens in 1k most common types: {} ({}%)".format(
    #     len(word_tokens_1k), float(len(word_tokens_1k)) / len(word_tokens) * 100
    #     )
    # print "-"*79

    # print datetime.now()
    # print "Filtering out stop words"
    # captions_content_dict = {}
    # for utt in captions_dict:
    #     captions_content_dict[utt] = [i for i in captions_dict[utt] if i not in stopwords.words("english")]
    # print datetime.now()

    # # Get word tokens
    # word_tokens = []
    # for utt in captions_content_dict:
    #     word_tokens.extend(captions_content_dict[utt])

    # # Analyze words
    # print "-"*79
    # print "Analysis of content words"
    # print "No. word tokens:", len(word_tokens)
    # print "No. word types:", len(set(word_tokens))
    # print "Most common word types:", Counter(word_tokens).most_common(10)
    # most_common_1k = [i[0] for i in Counter(word_tokens).most_common(1000)]
    # word_tokens_1k = [i for i in word_tokens if i in most_common_1k]
    # print "No. word tokens in 1k most common types: {} ({}%)".format(
    #     len(word_tokens_1k), float(len(word_tokens_1k)) / len(word_tokens) * 100
    #     )
    # print "-"*79

    # print
    # print datetime.now()


if __name__ == "__main__":
    main()
