#!/usr/bin/env python

"""
Calculate precision and recall metrics of the image captions.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
from datetime import datetime
from os import path
import argparse
import cPickle as pickle
import numpy as np
import sklearn.metrics as metrics
import sys


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
        "--sigmoid_threshold", type=float,
        help="threshold for sigmoid output (default: %(default)s)", default=0.4
        )
    parser.add_argument(
        "--analyze", help="print an analysis of the evaluation output for each utterance",
        action="store_true"
        )
    parser.add_argument("--plot", help="plot the precision-recall curve", action="store_true")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                             EVALUATION FUNCTIONS                            #
#-----------------------------------------------------------------------------#

def eval_precision_recall_fscore(prediction_dict, true_dict, analyze=False):
    """Evaluate precision and recall for a particular output."""

    # Calculate precision and recall
    n_tp = 0
    n_pred = 0
    n_true = 0
    word_tokens_correct = []
    if analyze:
        print
    for utt in sorted(prediction_dict):
        y_pred = prediction_dict[utt]
        y_true = true_dict[utt]
        cur_tokens_correct = set([i for i in y_true if i in y_pred])
        word_tokens_correct.extend(cur_tokens_correct)
        n_tp += len(cur_tokens_correct)
        n_pred += len(y_pred)
        n_true += len(set(y_true))
        if analyze:
            if len(y_pred) > 0:
                print "-"*79
                print "Image:", utt
                print "Predicted:", y_pred
                print "Ground truth:", y_true
                if n_pred > 0:
                    print "Current precision: {} / {} = {:.4f}".format(
                        n_tp, n_pred, float(n_tp)/n_pred*100.
                        )
                if n_true > 0:
                    print "Current recall: {} / {} = {:.4f}".format(
                        n_tp, n_true, float(n_tp)/n_true*100.
                        )
    precision = float(n_tp)/n_pred
    recall = float(n_tp)/n_true
    f_score = 2*precision*recall/(precision + recall)

    if analyze:
        print "-"*79
        print
        print "Most common correctly predicted words:", Counter(word_tokens_correct).most_common(15)

    return n_tp, n_pred, n_true, precision, recall, f_score


def eval_average_precision(sigmoid_output_dict, true_dict_id, show_plot=False):
    """Calculate average precision."""

    # Get maximum indices
    max_id = -1
    for image_key in true_dict_id:
        for i in true_dict_id[image_key]:
            if i > max_id:
                max_id = i
    max_sigmoid_id = sigmoid_output_dict[sigmoid_output_dict.keys()[0]].shape[0] - 1

    # Obtain sigmoid and true bag-of-word vectors:
    true_bow_vectors = np.zeros((len(sigmoid_output_dict), max_id + 1), dtype=np.int)
    sigmoid_bow_vectors = np.zeros((len(sigmoid_output_dict), max_id + 1))
    for i_data, image_key in enumerate(sorted(sigmoid_output_dict)):
        for i_word in true_dict_id[image_key]:
            true_bow_vectors[i_data, i_word] = 1
        sigmoid_bow_vectors[i_data, :max_sigmoid_id + 1] = sigmoid_output_dict[image_key]

    # # Obtain prediction at threshold
    # sigmoid_threshold = 0.5
    # prediction = sigmoid_bow_vectors >= sigmoid_threshold
    # n_tp = np.sum(prediction * true_bow_vectors)
    # n_pred = np.sum(prediction)
    # n_true = np.sum(true_bow_vectors)
    # precision = float(n_tp)/n_pred
    # recall = float(n_tp)/n_true
    # f_score = 2*precision*recall/(precision + recall)

    ap = metrics.average_precision_score(true_bow_vectors, sigmoid_bow_vectors, average="micro")

    if show_plot:
        import matplotlib.pyplot as plt
        precisions, recalls, _ = metrics.precision_recall_curve(
            true_bow_vectors.ravel(), sigmoid_bow_vectors.ravel()
            )
        plt.plot(recalls, precisions)
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        # plt.savefig("a.png")
        plt.show()

    return ap


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    # Model options
    options_dict_fn = path.join(args.model_dir, "options_dict.pkl")
    print "Reading:", options_dict_fn
    with open(options_dict_fn, "rb") as f:
        options_dict = pickle.load(f)

    # Mapping dictionary
    if "content" in options_dict["label_dict"]:
        word_to_id_fn = path.join(options_dict["data_dir"], "word_to_id_content.pkl")
    else:
        word_to_id_fn = path.join(options_dict["data_dir"], "word_to_id.pkl")
    print "Reading:", word_to_id_fn
    with open(word_to_id_fn, "rb") as f:
        word_to_id = pickle.load(f)
    id_to_word = dict([(i[1], i[0]) for i in word_to_id.iteritems()])    

    # Ground truth labels
    label_dict_fn = path.join(options_dict["data_dir"], options_dict["label_dict"])
    print "Reading:", label_dict_fn
    with open(label_dict_fn, "rb") as f:
        label_dict = pickle.load(f)
    true_dict = {}
    true_dict_id = {}
    for image_key in label_dict:
        if not image_key[:-2] in true_dict:
            true_dict[image_key[:-2]] = []
            true_dict_id[image_key[:-2]] = []
        true_dict[image_key[:-2]].extend([id_to_word[i] for i in label_dict[image_key]])
        true_dict_id[image_key[:-2]].extend(label_dict[image_key])

    # Read sigmoid output
    sigmoid_output_dict_fn = path.join(args.model_dir, "sigmoid_output_dict." + args.subset + ".npz")
    print "Reading:", sigmoid_output_dict_fn
    sigmoid_output_dict = dict(np.load(sigmoid_output_dict_fn))
    # with open(sigmoid_output_dict_fn, "rb") as f:
    #     sigmoid_output_dict = pickle.load(f)

    print "Thresholding and mapping IDs to words"
    word_output_dict = {}
    for utt in sigmoid_output_dict:
        word_output_dict[utt] = [
            id_to_word[i] for i in np.where(sigmoid_output_dict[utt] >= args.sigmoid_threshold)[0]
            ]

    print "Evaluating output"
    analysis = eval_precision_recall_fscore(word_output_dict, true_dict, args.analyze)
    n_tp = analysis[0]
    n_pred = analysis[1]
    n_true = analysis[2]
    precision = analysis[3]
    recall = analysis[4]
    f_score = analysis[5]
    average_precision = eval_average_precision(sigmoid_output_dict, true_dict_id, args.plot)

    print
    print "-"*79
    print "Sigmoid threshold: {:.2f}".format(args.sigmoid_threshold)
    print "No. predictions:", n_pred
    print "No. true tokens:", n_true
    print "Precision: {} / {} = {:.4f}%".format(n_tp, n_pred, precision*100.)
    print "Recall: {} / {} = {:.4f}%".format(n_tp, n_true, recall*100.)
    print "F-score: {:.4f}%".format(f_score*100.)
    print "Average precision: {:.4f}%".format(average_precision*100.)
    print "-"*79


if __name__ == "__main__":
    main()
