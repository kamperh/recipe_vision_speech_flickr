Results: Neural Networks Trained on Flickr8k Speech Data
========================================================


Oracle results
--------------

### OracleSpeechCNN, MFCC, max pooling

Model directory: models/train_bow_cnn/9e191f0eca
Options: {'ff_keep_prob': 1.0, 'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_most_common': 1000, 'script': 'train_bow_cnn', 'rnd_seed': 42, 'data_dir': 'data/mfcc_cmvn_dd_vad', 'batch_size': 128, 'center_padded': True, 'n_max_epochs': 25, 'model_dir': 'models/train_bow_cnn', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'pool_shapes': [[1, 3], [1, 3], [1, 75]], 'label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_hiddens': [2048]}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 20908
    No. true tokens: 29808
    Precision: 14639 / 20908 = 70.0163%
    Recall: 14639 / 29808 = 49.1110%
    F-score: 57.7293%
    Average precision: 55.6694%
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 21038
    No. true tokens: 29617
    Precision: 14796 / 21038 = 70.3299%
    Recall: 14796 / 29617 = 49.9578%
    F-score: 58.4187%
    Average precision: 56.3539%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 15921
    No. true tokens: 29617
    Precision: 13140 / 15921 = 82.5325%
    Recall: 13140 / 29617 = 44.3664%
    F-score: 57.7100%
    Average precision: 56.3539%
    ---------------------------------------------------------------------------
    Average P@10: 0.9350
    Average P@N: 0.7151
    Average EER: 0.0798
    ---------------------------------------------------------------------------


### OracleSpeechCNN, MFFC, mean pooling

Model directory: models/train_bow_cnn_custompool/c08666fcc5
Options: {'pool_shapes': [[1, 3], [1, 3], None], 'n_most_common': 1000, 'rnd_seed': 42, 'batch_size': 128, 'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_hiddens': [2048], 'ff_keep_prob': 1.0, 'data_dir': 'data/mfcc_cmvn_dd_vad', 'script': 'train_bow_cnn_custompool', 'pooling': 'mean', 'n_max_epochs': 25, 'model_dir': 'models/train_bow_cnn_custompool', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, 'label_dict': 'data/captions_content_dict.pkl'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 14075
    No. true tokens: 29808
    Precision: 9754 / 14075 = 69.3002%
    Recall: 9754 / 29808 = 32.7228%
    F-score: 44.4546%
    Average precision: 41.2801%
    ---------------------------------------------------------------------------


### OracleSpeechPSyC, MFCC, logsumexp pooling

Model directory: models/train_psyc/94a0a7228e
Options: {'pool_shapes': [None, None, None, None, None, None], 'n_most_common': 1000, 'rnd_seed': 42, 'batch_size': 128, 'optimizer': {'learning_rate': 0.001, 'type': 'adam'}, 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 64], 1, 10, 64, 64], [1, 10, 64, 64], [1, 10, 64, 64], [1, 10, 64, 1000]], 'ff_keep_prob': 1.0, 'data_dir': 'data/mfcc_mvn_dd_vad', 'script': 'train_psyc', 'pooling': 'logsumexp', 'n_max_epochs': 25, 'r': 1.0, 'model_dir': models/train_psyc', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, 'label_dict': 'data/captions_ontent_dict.pkl'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 23393
    No. true tokens: 29808
    Precision: 17858 / 23393 = 76.3391%
    Recall: 17858 / 29808 = 59.9101%
    F-score: 67.1341%
    Average precision: 67.4453%
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 23776
    No. true tokens: 29617
    Precision: 18136 / 23776 = 76.2786%
    Recall: 18136 / 29617 = 61.2351%
    F-score: 67.9340%
    Average precision: 68.2631%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 17637
    No. true tokens: 29617
    Precision: 15346 / 17637 = 87.0103%
    Recall: 15346 / 29617 = 51.8148%
    F-score: 64.9511%
    Average precision: 68.2631%
    ---------------------------------------------------------------------------
    Average P@10: 0.9600
    Average P@N: 0.8081
    Average EER: 0.0484
    ---------------------------------------------------------------------------




Speech from vision results
--------------------------

### VisionSpeechCNN, MFCC, max pooling

Model directory: models/train_visionsig_cnn/5bb5c4b4bd
Options: {'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_hiddens': [2048], 'rnd_seed': 42, 'batch_size': 128, 'vissionsig_threshold': None, 'speech_data_dir': 'data/mfcc_cmvn_dd_vad', 'pool_shapes': [[1, 3], [1, 3], [1, 75]], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_most_common': 1000, 'ff_keep_prob': 1.0, 'script': 'train_visionsig_cnn', 'word_to_d_dict': '../vision_nn/data/flickr30k/word_to_id_content.pkl', 'n_max_epochs': 25, 'model_dir': 'models/train_visionsig_nn', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': True, 'visionsig_npz': '../vision_nn/models/trainbow_mlp/d64b725040/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 18765
    No. true tokens: 29808
    Precision: 7023 / 18765 = 37.4261%
    Recall: 7023 / 29808 = 23.5608%
    F-score: 28.9173%
    Average precision: 21.6058%
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 19446
    No. true tokens: 29617
    Precision: 7236 / 19446 = 37.2107%
    Recall: 7236 / 29617 = 24.4319%
    F-score: 29.4968%
    Average precision: 21.7135%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 4456
    No. true tokens: 29617
    Precision: 2733 / 4456 = 61.3330%
    Recall: 2733 / 29617 = 9.2278%
    F-score: 16.0420%
    Average precision: 21.7135%
    ---------------------------------------------------------------------------
    Average P@10: 0.5350
    Average P@N: 0.3221
    Average EER: 0.2275
    ---------------------------------------------------------------------------


### VisionSpeechCNN, filterbanks, max pooling

Model directory: models/train_visionsig_cnn/65f9e0c68e
Options: {'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_hiddens': [2048], 'rnd_seed': 42, 'batch_ize': 128, 'vissionsig_threshold': None, 'speech_data_dir': 'data/fbank_vad', 'pool_shapes': [[1, 3], [1, 3], [1, 75], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[40, 9, 1, 64], [1, 10, 64, 256], [1, 1, 256, 1024]], 'n_most_common': 1000, 'ff_keep_prob': 1.0, 'script': 'train_visionsig_cnn', 'word_to_id_dict': '..vision_nn/data/flickr30k/word_to_id_content.pkl', 'n_max_epochs': 25, 'model_dir': 'models/train_visionsig_cnn', n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': True, 'visionsig_npz': '../vision_nn/models/train_ow_mlp/d64b725040/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    -------------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 16983
    No. true tokens: 29808
    Precision: 6235 / 16983 = 36.7132%
    Recall: 6235 / 29808 = 20.9172%
    F-score: 26.6504%
    Average precision: 19.9837%
    -------------------------------------------------------------------------------


### VisionSpeechCNN, MFCC, mean pooling

Model directory: models/train_visionsig_cnn_custompool/270a5fd1b0
Options: {'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_hiddens': [2048], 'rnd_seed': 42, 'batch_ize': 128, 'vissionsig_threshold': None, 'speech_data_dir': 'data/mfcc_cmvn_dd_vad', 'pool_shapes': [[1, 3], [1, 3] None], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 256], [, 11, 256, 1024]], 'n_most_common': 1000, 'ff_keep_prob': 1.0, 'script': 'train_visionsig_cnn_custompool', 'word_to_d_dict': '../vision_nn/data/flickr30k/word_to_id_content.pkl', 'pooling': 'mean', 'n_max_epochs': 25, 'model_dir': models/train_visionsig_cnn_custompool', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, visionsig_npz': '../vision_nn/models/train_bow_mlp/d64b725040/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 12983
    No. true tokens: 29808
    Precision: 4708 / 12983 = 36.2628%
    Recall: 4708 / 29808 = 15.7944%
    F-score: 22.0046%
    Average precision: 16.3493%
    ---------------------------------------------------------------------------


### VisionSpeechCNN, filterbanks, mean pooling

Model directory: models/train_visionsig_cnn_custompool/4617be96f5
Options: {'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_hiddens': [2048], 'rnd_seed': 42, 'batch_ize': 128, 'vissionsig_threshold': None, 'speech_data_dir': 'data/fbank_vad', 'pool_shapes': [[1, 3], [1, 3], None] 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[40, 9, 1, 64], [1, 10, 64, 256], [1, 11, 56, 1024]], 'n_most_common': 1000, 'ff_keep_prob': 1.0, 'script': 'train_visionsig_cnn_custompool', 'word_to_id_ict': '../vision_nn/data/flickr30k/word_to_id_content.pkl', 'pooling': 'mean', 'n_max_epochs': 25, 'model_dir': models/train_visionsig_cnn_custompool', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, visionsig_npz': '../vision_nn/models/train_bow_mlp/d64b725040/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 10750
    No. true tokens: 29808
    Precision: 3977 / 10750 = 36.9953%
    Recall: 3977 / 29808 = 13.3421%
    F-score: 19.6114%
    Average precision: 15.2995%
    ---------------------------------------------------------------------------


### VissionSpeechPSyC, MFCC, logsumexp pooling

Model directory: models/train_visionsig_psyc/4073c4072c
Options: {'optimizer': {'learning_rate': 0.001, 'type': 'adam'}, 'n_most_common': 1000, 'rnd_seed': 1, batch_size': 128, 'vissionsig_threshold': None, 'speech_data_dir': 'data/mfcc_cmvn_dd_vad', 'pool_shapes': [None, None, one, None, None, None], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[39, 9, 1, 64], [1, 0, 64, 64], [1, 10, 64, 64], [1, 10, 64, 64], [1, 10, 64, 64], [1, 10, 64, 1000]], 'ff_keep_prob': 1.0, 'script': train_visionsig_psyc', 'word_to_id_dict': '../vision_nn/data/flickr30k/word_to_id_content.pkl', 'pooling': 'logsumexp', n_max_epochs': 50, 'r': 1.0, 'model_dir': 'models/train_visionsig_psyc', 'n_padded': 800, 'detect_sigmoid_hreshold': 0.4, 'center_padded': False, 'visionsig_npz': '../vision_nn/models/train_bow_mlp/d64b725040/sigmoid_output_dict.lickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 19231
    No. true tokens: 29808
    Precision: 6827 / 19231 = 35.5000%
    Recall: 6827 / 29808 = 22.9032%
    F-score: 27.8431%
    Average precision: 19.2118%
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 19477
    No. true tokens: 29617
    Precision: 6864 / 19477 = 35.2416%
    Recall: 6864 / 29617 = 23.1759%
    F-score: 27.9627%
    Average precision: 18.9869%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 4019
    No. true tokens: 29617
    Precision: 2262 / 4019 = 56.2827%
    Recall: 2262 / 29617 = 7.6375%
    F-score: 13.4499%
    Average precision: 18.9869%
    ---------------------------------------------------------------------------
    Average P@10: 0.4800
    Average P@N: 0.3225
    Average EER: 0.2292
    ---------------------------------------------------------------------------


### VissionSpeechPSyC, filterbanks, logsumexp pooling

Model directory: models/train_visionsig_psyc/7f29164a94
Options: {'optimizer': {'learning_rate': 0.001, 'type': 'adam'}, 'n_most_common': 1000, 'rnd_seed': 1, 'batch_size': 128, 'vissionsig_threshold': None, 'speech_data_dir': 'data/fbank_vad', 'pool_shapes': [None, None, None, one, None, None], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[40, 9, 1, 64], [1, 10, 64, 4], [1, 10, 64, 64], [1, 10, 64, 64], [1, 10, 64, 64], [1, 10, 64, 1000]], 'ff_keep_prob': 1.0, 'script': 'train_isionsig_psyc', 'word_to_id_dict': '../vision_nn/data/flickr30k/word_to_id_content.pkl', 'pooling': 'logsumexp', 'n_ax_epochs': 50, 'r': 1.0, 'model_dir': 'models/train_visionsig_psyc', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, center_padded': False, 'visionsig_npz': '../vision_nn/models/train_bow_mlp/d64b725040/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 16983
    No. true tokens: 29808
    Precision: 6235 / 16983 = 36.7132%
    Recall: 6235 / 29808 = 20.9172%
    F-score: 26.6504%
    Average precision: 19.9837%
    ---------------------------------------------------------------------------




Unigram baseline results
------------------------

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 34447
    No. true tokens: 29808
    Precision: 4153 / 34447 = 12.0562%
    Recall: 4153 / 29808 = 13.9325%
    F-score: 12.9266%
    Average precision: 6.9581%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 9842
    No. true tokens: 29808
    Precision: 1758 / 9842 = 17.8622%
    Recall: 1758 / 29808 = 5.8977%
    F-score: 8.8676%
    Average precision: 6.9581%
    ---------------------------------------------------------------------------
    Average P@10: 0.0450
    Average P@N: 0.0377
    Average EER: 0.5000
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 34587
    No. true tokens: 29617
    Precision: 4214 / 34587 = 12.1838%
    Recall: 4214 / 29617 = 14.2283%
    F-score: 13.1269%
    Average precision: 6.8280%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 9882
    No. true tokens: 29617
    Precision: 1740 / 9882 = 17.6078%
    Recall: 1740 / 29617 = 5.8750%
    F-score: 8.8103%
    Average precision: 6.8280%
    ---------------------------------------------------------------------------
    Average P@10: 0.0500
    Average P@N: 0.0348
    Average EER: 0.5000
    ---------------------------------------------------------------------------


