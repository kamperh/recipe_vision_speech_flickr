#!/usr/bin/env python

"""
Evaluate a given model in keyword spotting.

The keywords list is specified by the `keywords_fn` variable.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
from datetime import datetime
from os import path
from scipy.interpolate import interp1d
from scipy.optimize import brentq
import argparse
import cPickle as pickle
import numpy as np
import sklearn.metrics as metrics
import sys

keywords_fn = path.join("..", "data", "keywords.4.txt")


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument("model_dir", type=str, help="model directory")
    parser.add_argument(
        "subset", type=str, help="subset to perform evaluation on", choices=["train", "dev", "test"]
        )
    parser.add_argument(
        "--analyze", help="print an analysis of the evaluation output for each utterance",
        action="store_true"
        )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                             EVALUATION FUNCTIONS                            #
#-----------------------------------------------------------------------------#

def calculate_eer(y_true, y_score):
    # https://yangcha.github.io/EER-ROC/
    fpr, tpr, thresholds = metrics.roc_curve(y_true, y_score)
    eer = brentq(lambda x : 1. - x - interp1d(fpr, tpr)(x), 0., 1.)
    thresh = interp1d(fpr, thresholds)(eer)
    return eer


def eval_keyword_spotting(sigmoid_dict, word_to_id, keyword_counts, label_dict, analyze=False):
    """Return P@10, P@N and EER."""
    
    keywords = sorted(keyword_counts)
    utterances = sorted(sigmoid_dict)
    keyword_ids = [word_to_id[w] for w in keywords]

    # Get sigmoid matrix for keywords
    keyword_sigmoid_mat = np.zeros((len(utterances), len(keywords)))
    for i_utt, utt in enumerate(utterances):
        keyword_sigmoid_mat[i_utt, :] = sigmoid_dict[utt][keyword_ids]

    # Keyword spotting evaluation
    p_at_10 = []
    p_at_n = []
    eer = []
    if analyze:
        print
    for i_keyword, keyword in enumerate(keywords):

        # Rank
        rank_order = keyword_sigmoid_mat[:, i_keyword].argsort()[::-1]
        utt_order = [utterances[i] for i in rank_order]

        # EER
        y_true = []
        for utt in utt_order:
            if keyword in label_dict[utt]:
                y_true.append(1)
            else:
                y_true.append(0)
        y_score = keyword_sigmoid_mat[:, i_keyword][rank_order]
        cur_eer = calculate_eer(y_true, y_score)
        eer.append(cur_eer)

        # P@10
        cur_p_at_10 = float(sum(y_true[:10]))/10.
        p_at_10.append(cur_p_at_10)

        # P@N
        cur_p_at_n = float(sum(y_true[:keyword_counts[keyword]]))/keyword_counts[keyword]
        p_at_n.append(cur_p_at_n)

        if analyze:
            print "-"*79
            print "Keyword:", keyword
            print "Current P@10: {:.4f}".format(cur_p_at_10)
            print "Current P@N: {:.4f}".format(cur_p_at_n)
            print "Current EER: {:.4f}".format(cur_eer)
            print "Top 10 utterances: ", utt_order[:10]
            if cur_p_at_10 != 1:
                # print "Incorrect in top 10:", [
                #     utt for i, utt in enumerate(utt_order[:10]) if y_true[i] == 0
                #     ]
                print "Incorrect in top 10:"
                print "\n".join([
                    "/share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/"
                    + utt[4:] + ".wav" for i, utt in enumerate(utt_order[:10]) if y_true[i] == 0
                    ])

    if analyze:
        print "-"*79
        print

    # Average
    p_at_10 = np.mean(p_at_10)
    p_at_n = np.mean(p_at_n)
    eer = np.mean(eer)

    return p_at_10, p_at_n, eer


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    # Load the model options to obtain dataset information
    options_dict_fn = path.join(args.model_dir, "options_dict.pkl")
    print "Reading:", options_dict_fn
    with open(options_dict_fn, "rb") as f:
        options_dict = pickle.load(f)

    # Load mapping dict
    word_to_id_fn = path.join(args.model_dir, "word_to_id.pkl")
    print "Reading:", word_to_id_fn
    with open(word_to_id_fn, "rb") as f:
        word_to_id = pickle.load(f)
    id_to_word = dict([(i[1], i[0]) for i in word_to_id.iteritems()])

    # Read ground truth labels
    if "speech_label_dict" in options_dict:
        label_dict = options_dict["speech_label_dict"]
    else:
        label_dict = options_dict["label_dict"]
    print "Reading:", label_dict
    with open(label_dict, "rb") as f:
        true_dict = pickle.load(f)

    # Read sigmoid output
    sigmoid_output_dict_fn = path.join(args.model_dir, "sigmoid_output_dict." + args.subset + ".pkl")
    print "Reading:", sigmoid_output_dict_fn
    with open(sigmoid_output_dict_fn, "rb") as f:
        sigmoid_output_dict = pickle.load(f)
    utterances = sorted(sigmoid_output_dict.keys())

    # Read keywords
    print "Reading:", keywords_fn
    with open(keywords_fn, "r") as f:
        keywords = []
        for line in f:
            keywords.append(line.strip())
    print "Keywords:", keywords

    print "Getting subset labels: {}".format(args.subset)
    true_dict_subset = {}
    word_tokens = []
    for utt in utterances:
        true_dict_subset[utt] = true_dict[utt]
        word_tokens.extend(true_dict[utt])
    word_counts = Counter(word_tokens)
    keyword_counts = dict([(i, word_counts[i]) for i in word_counts if i in keywords])

    print "Performing evaluation"
    p_at_10, p_at_n, eer = eval_keyword_spotting(
        sigmoid_output_dict, word_to_id, keyword_counts, true_dict_subset, args.analyze
        )

    print
    print "-"*79
    print "Average P@10: {:.4f}".format(p_at_10)
    print "Average P@N: {:.4f}".format(p_at_n)
    print "Average EER: {:.4f}".format(eer)
    print "-"*79


if __name__ == "__main__":
    main()
