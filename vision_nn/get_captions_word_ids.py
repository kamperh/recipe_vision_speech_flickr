#!/usr/bin/env python

"""
Convert the Flickr captions to word IDs.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

from collections import Counter
from datetime import datetime
from nltk.corpus import stopwords
from os import path
import argparse
import cPickle as pickle
import os
import re
import sys


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0], add_help=False)
    parser.add_argument("captions_fn", type=str, help="Flickr tokens file")
    parser.add_argument("output_dir", type=str, help="write files to this directory")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    if not path.isdir(args.output_dir):
        os.mkdir(args.output_dir)


    # ALL WORDS

    captions_dict = {}
    word_tokens = []
    print datetime.now()
    print "Reading:", args.captions_fn
    with open(args.captions_fn) as f:
        for line in f:
            line = line.strip().split()
            utt = line[0].replace(".jpg#", "_")
            captions_dict[utt] = [i.lower() for i in line[1:] if re.match(r"^[a-z\-']*$", i.lower())]
            # if i not in [".", ",", '"', "!", "#"]]
            word_tokens.extend(captions_dict[utt])
    print datetime.now()

    print "No. word tokens:", len(word_tokens)
    print "No. word types:", len(set(word_tokens))
    print "Most common words:", Counter(word_tokens).most_common(20)

    # Get mapping
    word_to_id = {}
    for i, (word, count) in enumerate(Counter(word_tokens).most_common()):
        word_to_id[word] = i
    word_to_id_fn = path.join(args.output_dir, "word_to_id.txt")
    print "Writing:", word_to_id_fn
    with open(word_to_id_fn, "w") as f:
        for word in sorted(word_to_id):
            f.write(word + " " + str(word_to_id[word]) + "\n")
    word_to_id_fn = path.join(args.output_dir, "word_to_id.pkl")
    print "Writing:", word_to_id_fn
    with open(word_to_id_fn, "wb") as f:
        pickle.dump(word_to_id, f, -1)

    # Map captions
    captions_word_ids_dict = {}
    for utt in captions_dict:
        captions_word_ids_dict[utt] = [word_to_id[word] for word in captions_dict[utt]]
    captions_word_ids_fn = path.join(args.output_dir, "captions_word_ids.txt")
    print "Writing:", captions_word_ids_fn
    with open(captions_word_ids_fn, "w") as f:
        for utt in sorted(captions_word_ids_dict):
            f.write(utt + " " + " ".join([str(i) for i in captions_word_ids_dict[utt]]) + "\n")
        # for word in sorted(captions_word_ids):
        #     f.write(word + " " + str(captions_word_ids[word]) + "\n")
    captions_word_ids_fn = path.join(args.output_dir, "captions_word_ids_dict.pkl")
    print "Writing:", captions_word_ids_fn
    with open(captions_word_ids_fn, "wb") as f:
        pickle.dump(captions_word_ids_dict, f, -1)


    # CONTENT WORDS

    print datetime.now()
    print "Filtering out stop words"
    captions_content_dict = {}
    word_tokens_content = []
    for utt in captions_dict:
        captions_content_dict[utt] = [
            i for i in captions_dict[utt] if i not in
            stopwords.words("english") and not "'" in i and i != "-"
            ]
        word_tokens_content.extend(captions_content_dict[utt])
    print datetime.now()

    print "No. content word tokens:", len(word_tokens_content)
    print "No. content word types:", len(set(word_tokens_content))
    print "Most common content words:", Counter(word_tokens_content).most_common(20)

    # Get mapping
    word_to_id_content = {}
    for i, (word, count) in enumerate(Counter(word_tokens_content).most_common()):
        word_to_id_content[word] = i
    word_to_id_content_fn = path.join(args.output_dir, "word_to_id_content.txt")
    print "Writing:", word_to_id_content_fn
    with open(word_to_id_content_fn, "w") as f:
        for word in sorted(word_to_id_content):
            f.write(word + " " + str(word_to_id_content[word]) + "\n")
    word_to_id_content_fn = path.join(args.output_dir, "word_to_id_content.pkl")
    print "Writing:", word_to_id_content_fn
    with open(word_to_id_content_fn, "wb") as f:
        pickle.dump(word_to_id_content, f, -1)

    # Map captions
    captions_word_ids_content_dict = {}
    for utt in captions_content_dict:
        captions_word_ids_content_dict[utt] = [
            word_to_id_content[word] for word in captions_content_dict[utt]
            ]
    captions_word_ids_content_fn = path.join(args.output_dir, "captions_word_ids_content.txt")
    print "Writing:", captions_word_ids_content_fn
    with open(captions_word_ids_content_fn, "w") as f:
        for utt in sorted(captions_word_ids_content_dict):
            f.write(utt + " " + " ".join([str(i) for i in captions_word_ids_content_dict[utt]]) + "\n")
        # for word in sorted(captions_word_ids_content_:
        #     f.write(word + " " + str(captions_word_ids_content_word]) + "\n")
    captions_word_ids_content_fn = path.join(args.output_dir, "captions_word_ids_content_dict.pkl")
    print "Writing:", captions_word_ids_content_fn
    with open(captions_word_ids_content_fn, "wb") as f:
        pickle.dump(captions_word_ids_content_dict, f, -1)

    print datetime.now()


if __name__ == "__main__":
    main()
