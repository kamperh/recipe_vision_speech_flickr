Speech Neural Networks Trained on Images with Spoken Captions
=============================================================

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
    ./apply_bow_cnn.py models/train_bow_cnn/9e191f0eca dev
    ./eval_precision_recall.py --analyze models/train_bow_cnn/9e191f0eca dev

    # Apply and evaluate on test
    ./apply_bow_cnn.py models/train_bow_cnn/9e191f0eca test
    ./eval_precision_recall.py models/train_bow_cnn/9e191f0eca test

The dataset can be set by changing the "data_dir" value in the `options_dict`
in `train_bow_cnn.py`. The sigmoid threshold used for detection can also be
adjusted by passing the `--sigmoid_threshold` option to
`eval_precision_recall.py`.

On the test set, this model achieves the following scores, as in Table 1 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under OracleSpeechCNN:

    Sigmoid threshold: 0.40
    No. predictions: 21038
    No. true tokens: 29617
    Precision: 14796 / 21038 = 70.3299%
    Recall: 14796 / 29617 = 49.9578%
    F-score: 58.4187%
    Average precision: 56.3539%

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
        models/train_bow_cnn_custompool/c08666fcc5 dev
    ./eval_precision_recall.py models/train_bow_cnn_custompool/c08666fcc5 dev

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
        models/train_psyc/907ae37ccc dev
    ./eval_precision_recall.py models/train_psyc/907ae37ccc dev
    ./apply_bow_cnn_custompool.py models/train_psyc/907ae37ccc test
    ./eval_precision_recall.py models/train_psyc/907ae37ccc test

On the test set, this model achieves the following scores, as in Table 1 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under OracleSpeechPSC:

    ...

To obtain and analyze the frame scores:

    ./apply_psyc_frames.py --n_batches 1 --batch_size 259 \
        models/train_psyc/2f6c7d8856 dev

Then view these using the `analysis_sandbox.ipynb` IPython notebook.


Visually grounded spoken bag-of-words CNN with max pooling
----------------------------------------------------------
Train and evaluate a visually grounded bag-of-words CNN:

    ./train_visionspeech_cnn.py
    ./apply_bow_cnn.py models/train_visionsig_cnn/8e6c2607c2 dev
    ./eval_precision_recall.py \
        --analyze --plot --sigmoid_threshold 0.7 --analyze_confusions \
        models/train_visionsig_cnn/8e6c2607c2 dev
    ./apply_bow_cnn.py models/train_visionsig_cnn/8e6c2607c2 test
    ./eval_precision_recall.py models/train_visionsig_cnn/8e6c2607c2 test

On the test set, this model achieves the following scores, as in Table 1 of
[Kamper et al., 2017](https://arxiv.org/abs/1703.08136) under OracleSpeechPSC:

    ...


Visually grounded spoken bag-of-words CNN with mean pool over output
--------------------------------------------------------------------
Train and evaluate a visually grounded bag-of-words CNN with custom pooling
layer:

    ./train_visionspeech_cnn_custompool.py
    ./apply_bow_cnn_custompool.py --batch_size 259 \
        models/train_visionsig_cnn_custompool/de68e3cd67 dev
    ./eval_precision_recall.py \
        models/train_visionsig_cnn_custompool/de68e3cd67 dev


Visually grounded spoken bag-of-words CNN with PSyC architecture
----------------------------------------------------------------
Train and evaluate a visually grounded bag-of-words CNN with a PSyC
architecture:

    ./train_visionsig_psyc.py
    ./apply_bow_cnn_custompool.py --batch_size 259 \
        models/train_visionsig_psyc/a4bc45a09c dev
    ./eval_precision_recall.py models/train_visionsig_psyc/a4bc45a09c dev

To obtain and analyze the frame scores:

    ./apply_psyc_frames.py --n_batches 1 --batch_size 259 \
        models/train_visionsig_psyc/a4bc45a09c dev

Then view these using the `analysis_sandbox.ipynb` IPython notebook.
