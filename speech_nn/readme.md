Visually Grounded Speech Neural Networks
========================================

Overview
--------
Most of the results in [Kamper et al., 2017](https://arxiv.org/abs/1703.08136)
are generated here. Apart from the results given below, more detailed analysis
of the outputs that I obtained are also given in `doc/results.md`.


Data preparation
----------------
Convert Kaldi filterbank and MFCC features to Numpy archives:

    ./get_kaldi_fbank.py
    ./get_kaldi_mfcc.py

Analyze speech data in Numpy archives:

    ./analyze_speech_data.py data/fbank_vad/train.npz
    ./analyze_speech_data.py data/mfcc_cmvn_dd_vad/test.npz

Get the ground truth captions, strip out content words, and analyze:

    ./get_captions.py
    ./analyze_captions.py data/captions_dict.pkl
    ./analyze_captions.py data/captions_content_dict.pkl


Oracle spoken bag-of-words with max pooling
-------------------------------------------
Train and evaluate the oracle bag-of-words CNN:

    # Train
    ./train_bow_cnn.py

    # Apply and evaluate on dev
    ./apply_bow_cnn.py models/train_bow_cnn/4f8af91591 dev
    ./eval_precision_recall.py --analyze models/train_bow_cnn/4f8af91591 dev

    # Apply and evaluate on test
    ./apply_bow_cnn.py models/train_bow_cnn/4f8af91591 test
    ./eval_precision_recall.py models/train_bow_cnn/4f8af91591 test

The dataset can be set by changing the "data_dir" value in the `options_dict`
in `train_bow_cnn.py`. The sigmoid threshold used for detection can also be
adjusted by passing the `--sigmoid_threshold` option to
`eval_precision_recall.py`.

On the test set, this model achieves the following scores, as in Table 1 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under OracleSpeechCNN:

    Sigmoid threshold: 0.40
    No. predictions: 19108
    No. true tokens: 29617
    Precision: 14969 / 19108 = 78.3389%
    Recall: 14969 / 29617 = 50.5419%
    F-score: 61.4428%
    Average precision: 59.5470%

Note that for the model here, max pooling is performed over the entire CNN
output. Because of this, the effect of zero-padding might be negligible.
However, since we have bias terms, which might be positive, there could be
values in the units with receptive fields within the zero-padding regions. This
is dealt with explicitly by the model below (max pooling can be selected rather
than mean pooling). But it seems that this leads to a slight drop in
performance. This could be due to the slightly different way in which padding
is done, but I have not investigated this fully.


Oracle spoken bag-of-words CNN with mean pooling
------------------------------------------------
Train and evaluate a bag-of-words CNN with custom pooling layer:

    ./train_bow_cnn_custompool.py
    ./apply_bow_cnn_custompool.py --batch_size 259 \
        models/train_bow_cnn_custompool/45be532eff dev
    ./eval_precision_recall.py models/train_bow_cnn_custompool/45be532eff dev

The "pool" value in the `options_dict` can be set to "avg", "max", or
"logsumexp"; these are different types of pooling which is exclusively
performed on valid output regions, i.e. padding is only performed for
implementational purposes and padded regions are ignored during pooling. The
logsumexp pooling is described in [Palaz et al., IS'16].


Oracle spoken bag-of-words CNN with PSyC architecture
-----------------------------------------------------
Train and evaluate a bag-of-words CNN with a PSyC architecture:

    ./train_psyc.py
    ./apply_bow_cnn_custompool.py --batch_size 259 \
        models/train_psyc/246f3f7f69 dev
    ./eval_precision_recall.py models/train_psyc/246f3f7f69 dev
    ./apply_bow_cnn_custompool.py models/train_psyc/246f3f7f69 test
    ./eval_precision_recall.py models/train_psyc/246f3f7f69 test

On the test set, this model achieves the following scores, as in Table 1 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under OracleSpeechPSC:

    Sigmoid threshold: 0.40
    No. predictions: 24217
    No. true tokens: 29617
    Precision: 18662 / 24217 = 77.0616%
    Recall: 18662 / 29617 = 63.0111%
    F-score: 69.3316%
    Average precision: 69.7159%

To obtain and analyze the frame scores:

    ./apply_psyc_frames.py --n_batches 1 --batch_size 259 \
        models/train_psyc/246f3f7f69 dev

Then view these using the `analysis_sandbox.ipynb` IPython notebook.


Visually grounded spoken bag-of-words CNN with max pooling
----------------------------------------------------------
Train and evaluate a visually grounded bag-of-words CNN:

    ./train_visionspeech_cnn.py
    ./apply_bow_cnn.py models/train_visionspeech_cnn/989f00f30a dev
    ./eval_precision_recall.py \
        --analyze --plot --sigmoid_threshold 0.7 --analyze_confusions \
        models/train_visionspeech_cnn/989f00f30a dev
    ./apply_bow_cnn.py models/train_visionspeech_cnn/989f00f30a test
    ./eval_precision_recall.py models/train_visionspeech_cnn/989f00f30a test

On the test set, this model achieves the following scores, as in Table 1 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under OracleSpeechPSC:

    Sigmoid threshold: 0.40
    No. predictions: 20751
    No. true tokens: 29617
    Precision: 7138 / 20751 = 34.3983%
    Recall: 7138 / 29617 = 24.1010%
    F-score: 28.3434%
    Average precision: 20.0420%


Visually grounded spoken bag-of-words CNN with mean pool over output
--------------------------------------------------------------------
Train and evaluate a visually grounded bag-of-words CNN with custom pooling
layer:

    ./train_visionspeech_cnn_custompool.py
    ./apply_bow_cnn_custompool.py --batch_size 259 \
        models/train_visionspeech_cnn_custompool/59e494dba3 dev
    ./eval_precision_recall.py \
        models/train_visionspeech_cnn_custompool/59e494dba3 dev


Visually grounded spoken bag-of-words CNN with PSyC architecture
----------------------------------------------------------------
Train and evaluate a visually grounded bag-of-words CNN with a PSyC
architecture:

    ./train_visionspeech_psyc.py
    ./apply_bow_cnn_custompool.py --batch_size 259 \
        models/train_visionspeech_psyc/d5cb9be08b dev
    ./eval_precision_recall.py models/train_visionspeech_psyc/d5cb9be08b dev

On the test set, this model achieves the following scores, as in Table 1 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under VisionSpeechPSC:

    Sigmoid threshold: 0.40
    No. predictions: 14900
    No. true tokens: 29617
    Precision: 5977 / 14900 = 40.1141%
    Recall: 5977 / 29617 = 20.1810%
    F-score: 26.8527%
    Average precision: 18.9217%

To obtain and analyze the frame scores:

    ./apply_psyc_frames.py --n_batches 1 --batch_size 259 \
        models/train_visionspeech_psyc/d5cb9be08b dev

Then view these using the `analysis_sandbox.ipynb` IPython notebook.


Keyword spotting
----------------
Randomly sample a set of keywords:

    ./keywords_propose_train.py

To look at the overlap of the proposed keyword list with a particular set, run:

    ./keywords_in_set.py data/keywords.txt dev

We samples keywords, and saved these in `../data/keywords.4.txt`. To perform
keyword spotting for any of the above models using this keyword set, run:

    ./eval_keyword_spotting.py models/train_visionspeech_cnn/989f00f30a test

On the test set, this model achieves the following scores, as in Table 3 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under VisionSpeechPSC:
    
    Average P@10: 0.5450
    Average P@N: 0.3312
    Average EER: 0.2233

The `keywords_fn` variable at the start of `eval_keyword_spotting.py` are used
to choose the set of keywords if you want to use a different keyword set.


Unigram baseline
----------------
Get unigram baseline and evaluate:

    ./get_unigram_baseline.py dev
    ./eval_precision_recall.py models/unigram_baseline dev
    ./get_unigram_baseline.py test
    ./eval_precision_recall.py models/unigram_baseline test

On the test set, this model achieves the following scores, as in Table 1 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under unigram baseline:

    Sigmoid threshold: 0.40
    No. predictions: 34587
    No. true tokens: 29617
    Precision: 4214 / 34587 = 12.1838%
    Recall: 4214 / 29617 = 14.2283%
    F-score: 13.1269%
    Average precision: 6.8280%
