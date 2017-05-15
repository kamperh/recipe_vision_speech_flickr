#!/usr/bin/env python

"""
Calculate precision and recall metrics of the spoken captions.

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
    parser.add_argument(
        "--analyze_confusions",
        help="print an analysis of the confusions between true and predicted words",
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
                print "Utterance:", utt
                print "Predicted:", sorted(y_pred)
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


def eval_average_precision(word_to_id, sigmoid_output_dict, true_dict, show_plot=False):
    """
    Calculate average precision.

    In comments below, a different method than `eval_precision_recall_fscore`
    is also given for calculating these metrics.
    """

    # Update word_to_id with all words in true labels (not only most common)
    word_to_id = word_to_id.copy()
    word_tokens = []
    for utt in true_dict:
        word_tokens.extend(true_dict[utt])
    last_id = max(word_to_id.values())
    max_sigmoid_id = last_id
    for word in sorted(set(word_tokens)):
        if word not in word_to_id:
            word_to_id[word] = last_id + 1
            last_id += 1
    # print "No. total word types:", len(word_to_id)

    # Obtain sigmoid and true bag-of-word vectors:
    true_bow_vectors = np.zeros((len(sigmoid_output_dict), len(word_to_id)), dtype=np.int)
    sigmoid_bow_vectors = np.zeros((len(sigmoid_output_dict), len(word_to_id)))
    for i_utt, utt in enumerate(sorted(sigmoid_output_dict)):
        for word in true_dict[utt]:
            true_bow_vectors[i_utt, word_to_id[word]] = 1
        sigmoid_bow_vectors[i_utt, :max_sigmoid_id + 1] = sigmoid_output_dict[utt]

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
        # plt.show()

    return ap


def analyze_confusions(prediction_dict, true_dict, show_plot=False):
    """Analyze the confusions from incorrectly predicted words."""

    # Get confusion statistics
    word_tokens_incorrect = []
    confusions_dict = {}
    for utt in sorted(prediction_dict):
        y_pred = prediction_dict[utt]
        y_true = true_dict[utt]
        cur_tokens_correct = set([i for i in y_true if i in y_pred])
        cur_tokens_incorrect = set([i for i in y_pred if i not in y_true])
        word_tokens_incorrect.extend(cur_tokens_incorrect)
        for word in cur_tokens_incorrect:
            if word not in confusions_dict:
                confusions_dict[word] = Counter()
            confusions_dict[word] += Counter(set(y_true) - set(cur_tokens_correct)) # unaccounted-for words

    # Print confusions for most common words
    n_words = 10
    n_confusions = 5
    plot_words = []
    plot_array = np.zeros((n_words, n_confusions))
    plot_confusion_labels = {}
    for i_word, (word, count) in enumerate(Counter(word_tokens_incorrect).most_common(n_words)):
        print "{} ({}): {}".format(word, count, confusions_dict[word].most_common(n_confusions))
        plot_words.append(word)
        plot_array[i_word] = np.array(
            [float(i[1])/sum(confusions_dict[word].values()) for i in
            confusions_dict[word].most_common(n_confusions)]
            )
        plot_confusion_labels[word] = [i[0] for i in confusions_dict[word].most_common(n_confusions)]


    if show_plot:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        heatmap = ax.imshow(plot_array, cmap="Blues", interpolation="nearest")
        plt.yticks(range(len(plot_words)), plot_words)
        plt.xticks([])
        for y, word in enumerate(plot_words):
            for x, label in enumerate(plot_confusion_labels[word]):
                plt.text(
                    x, y, label, horizontalalignment="center", verticalalignment="center", rotation=45
                    )

        # Axes and grid
        ax.spines["bottom"].set_color("white")
        ax.spines["top"].set_color("white") 
        ax.spines["right"].set_color("white")
        ax.spines["left"].set_color("white")
        ax.set_xticks(np.arange(-0.5, n_confusions, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, n_words, 1), minor=True)
        ax.tick_params(colors="white", which="minor")
        ax.grid(which="minor", color="w", linestyle="-", linewidth=1.5)


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
    average_precision = eval_average_precision(word_to_id, sigmoid_output_dict, true_dict, args.plot)

    if args.analyze_confusions:
        print
        print "-"*79
        print "Most common confusions:"
        analyze_confusions(word_output_dict, true_dict, args.plot)
        print "-"*79

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

    if args.plot:
        import matplotlib.pyplot as plt
        plt.show()


if __name__ == "__main__":
    main()
