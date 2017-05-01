Results: Neural Networks Trained on Flickr8k Speech Data
========================================================


Oracle results
--------------

### OracleSpeechCNN, MFCC, max pooling

Model directory: models/train_bow_cnn/4f8af91591
Options: {'ff_keep_prob': 1.0, 'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_most_common': 1000, 'script': 'train_bow_cnn', 'rnd_seed': 42, 'data_dir': 'data/mfcc_cmvn_dd_vad', 'batch_size': 16, 'center_padded': True, 'n_max_epochs': 25, 'model_dir': 'models/train_bow_cnn', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'pool_shapes': [[1, 3], [1, 3], [1, 75]], 'label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_hiddens': [4096]}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 19168
    No. true tokens: 29808
    Precision: 14838 / 19168 = 77.4103%
    Recall: 14838 / 29808 = 49.7786%
    F-score: 60.5929%
    Average precision: 58.5717%
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 19108
    No. true tokens: 29617
    Precision: 14969 / 19108 = 78.3389%
    Recall: 14969 / 29617 = 50.5419%
    F-score: 61.4428%
    Average precision: 59.5470%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 14306
    No. true tokens: 29617
    Precision: 12883 / 14306 = 90.0531%
    Recall: 12883 / 29617 = 43.4987%
    F-score: 58.6617%
    Average precision: 59.5470%
    ---------------------------------------------------------------------------
    Average P@10: 0.9200
    Average P@N: 0.7238
    Average EER: 0.062
    ---------------------------------------------------------------------------


### OracleSpeechCNN, MFFC, mean pooling

Model directory: models/train_bow_cnn_custompool/c08666fcc5
Options: {'pool_shapes': [[1, 3], [1, 3], None], 'n_most_common': 1000, 'rnd_seed': 42, 'batch_size': 128, 'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_hiddens': [2048], 'ff_keep_prob': 1.0, 'data_dir': 'data/mfcc_cmvn_dd_vad', 'script': 'train_bow_cnn_custompool', 'pooling': 'mean', 'n_max_epochs': 25, 'model_dir': 'models/train_bow_cnn_custompool', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, 'label_dict': 'data/captions_content_dict.pkl'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 18885
    No. true tokens: 29808
    Precision: 13234 / 18885 = 70.0768%
    Recall: 13234 / 29808 = 44.3975%
    F-score: 54.3569%
    Average precision: 50.6143%
    ---------------------------------------------------------------------------


### OracleSpeechPSyC, MFCC, logsumexp pooling

Model directory: models/train_psyc/246f3f7f69
Options: {'pool_shapes': [None, None, None, None, None, None], 'n_most_common': 1000, 'rnd_seed': 42, 'batch_size': 64, 'optimizer': {'learning_rate': 0.001, 'type': 'adam'}, 'filter_shapes': [[39, 9, 1, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 1000]], 'ff_keep_prob': 1.0, 'data_dir': 'data/mfcc_cmvn_dd_vad', 'script': 'train_psyc', 'pooling': 'logsumexp', 'n_max_epochs': 25, 'r': 1.0, 'model_dir': 'models/train_psyc', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, 'label_dict': 'data/captions_content_dict.pkl'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 23890
    No. true tokens: 29808
    Precision: 18407 / 23890 = 77.0490%
    Recall: 18407 / 29808 = 61.7519%
    F-score: 68.5575%
    Average precision: 69.0995%
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 24217
    No. true tokens: 29617
    Precision: 18662 / 24217 = 77.0616%
    Recall: 18662 / 29617 = 63.0111%
    F-score: 69.3316%
    Average precision: 69.7159%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 18308
    No. true tokens: 29617
    Precision: 16009 / 18308 = 87.4426%
    Recall: 16009 / 29617 = 54.0534%
    F-score: 66.8086%
    Average precision: 69.7159%
    ---------------------------------------------------------------------------
    Average P@10: 0.9650
    Average P@N: 0.8303
    Average EER: 0.0413
    ---------------------------------------------------------------------------




Visually grounded speech network results
----------------------------------------

### VisionSpeechCNN, MFCC, max pooling

Model directory: models/train_visionspeech_cnn/989f00f30a
Options: {'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_hiddens': [4096], 'rnd_seed': 42, 'batch_size': 16, 'speech_data_dir': 'data/mfcc_cmvn_dd_vad', 'pool_shapes': [[1, 3], [1, 3], [1, 75]], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_most_common': 1000, 'ff_keep_prob': 1.0, 'script': 'train_visionspeech_cnn', 'visionsig_threshold': None, 'word_to_id_dict': '../vision_nn_flickr30k/data/flickr30k/word_to_id_content.pkl', 'n_max_epochs': 15, 'model_dir': 'models/train_visionspeech_cnn', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': True, 'visionsig_npz': '../vision_nn_flickr30k/models/train_bow_mlp/dea2850778/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 20137
    No. true tokens: 29808
    Precision: 7059 / 20137 = 35.0549%
    Recall: 7059 / 29808 = 23.6816%
    F-score: 28.2671%
    Average precision: 20.5216%
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 20751
    No. true tokens: 29617
    Precision: 7138 / 20751 = 34.3983%
    Recall: 7138 / 29617 = 24.1010%
    F-score: 28.3434%
    Average precision: 20.0420%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 4211
    No. true tokens: 29617
    Precision: 2648 / 4211 = 62.8829%
    Recall: 2648 / 29617 = 8.9408%
    F-score: 15.6557%
    Average precision: 20.0420%
    ---------------------------------------------------------------------------
    Average P@10: 0.5450
    Average P@N: 0.3312
    Average EER: 0.2233
    ---------------------------------------------------------------------------


### VisionSpeechCNN, filterbanks, max pooling

Model directory: models/train_visionspeech_cnn/ae93b4d568
Options: {'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_hiddens': [4096], 'rnd_seed': 42, 'batch_size': 16, 'speech_data_dir': 'data/fbank_vad', 'pool_shapes': [[1, 3], [1, 3], [1, 75]], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[40, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_most_common': 1000, 'ff_keep_prob': 1.0, 'script': 'train_visionspeech_cnn', 'visionsig_threshold': None, 'word_to_id_dict': '../vision_nn_flickr30k/data/flickr30k/word_to_id_content.pkl', 'n_max_epochs': 15, 'model_dir': 'models/train_visionspeech_cnn', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': True, 'visionsig_npz': '../vision_nn_flickr30k/models/train_bow_mlp/dea2850778/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    -------------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 18331
    No. true tokens: 29808
    Precision: 6393 / 18331 = 34.8753%
    Recall: 6393 / 29808 = 21.4473%
    F-score: 26.5606%
    Average precision: 19.1246%
    -------------------------------------------------------------------------------


### VisionSpeechCNN, MFCC, mean pooling

Model directory: models/train_visionspeech_cnn_custompool/71474cab0e
Options:  {'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_hiddens': [4096], 'rnd_seed': 42, 'batch_size': 16, 'speech_data_dir': 'data/mfcc_cmvn_dd_vad', 'pool_shapes': [[1, 3], [1, 3], None], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[39, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_most_common': 1000, 'ff_keep_prob': 1.0, 'script': 'train_visionspeech_cnn_custompool', 'visionsig_threshold': None, 'word_to_id_dict': '../vision_nn_flickr30k/data/flickr30k/word_to_id_content.pkl', 'pooling': 'mean', 'n_max_epochs': 25, 'model_dir': 'models/train_visionspeech_cnn_custompool', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, 'visionsig_npz': '../vision_nn_flickr30k/models/train_bow_mlp/dea2850778/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 16573
    No. true tokens: 29808
    Precision: 5649 / 16573 = 34.0856%
    Recall: 5649 / 29808 = 18.9513%
    F-score: 24.3591%
    Average precision: 17.3742%
    ---------------------------------------------------------------------------


### VisionSpeechCNN, filterbanks, mean pooling

Model directory: models/train_visionsig_cnn_custompool/c3a4fcfba3
Options: {'optimizer': {'learning_rate': 0.0001, 'type': 'adam'}, 'n_hiddens': [4096], 'rnd_seed': 42, 'batch_size': 16, 'speech_data_dir': 'data/fbank_vad', 'pool_shapes': [[1, 3], [1, 3], None], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[40, 9, 1, 64], [1, 10, 64, 256], [1, 11, 256, 1024]], 'n_most_common': 1000, 'ff_keep_prob': 1.0, 'script': 'train_visionspeech_cnn_custompool', 'visionsig_threshold': None, 'word_to_id_dict': '../vision_nn_flickr30k/data/flickr30k/word_to_id_content.pkl', 'pooling': 'mean', 'n_max_epochs': 25, 'model_dir': 'models/train_visionspeech_cnn_custompool', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, 'visionsig_npz': '../vision_nn_flickr30k/models/train_bow_mlp/dea2850778/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 17260
    No. true tokens: 29808
    Precision: 5534 / 17260 = 32.0626%
    Recall: 5534 / 29808 = 18.5655%
    F-score: 23.5149%
    Average precision: 16.3565%
    ---------------------------------------------------------------------------


### VissionSpeechPSyC, MFCC, logsumexp pooling

Model directory: models/train_visionsig_psyc/d5cb9be08b
Options: {'optimizer': {'learning_rate': 0.001, 'type': 'adam'}, 'n_most_common': 1000, 'rnd_seed': 1, 'batch_size': 64, 'speech_data_dir': 'data/mfcc_cmvn_dd_vad', 'pool_shapes': [None, None, None, None, None, None], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[39, 9, 1, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 1000]], 'ff_keep_prob': 1.0, 'script': 'train_visionspeech_psyc', 'visionsig_threshold': None, 'word_to_id_dict': '../vision_nn_flickr30k/data/flickr30k/word_to_id_content.pkl', 'pooling': 'logsumexp', 'n_max_epochs': 25, 'r': 1.0, 'model_dir': 'models/train_visionspeech_psyc', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, 'visionsig_npz': '../vision_nn_flickr30k/models/train_bow_mlp/dea2850778/sigmoid_output_dict.flickr8k.npz'}

Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 14401
    No. true tokens: 29808
    Precision: 5970 / 14401 = 41.4555%
    Recall: 5970 / 29808 = 20.0282%
    F-score: 27.0081%
    Average precision: 19.3197%
    ---------------------------------------------------------------------------

Results on test:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 14900
    No. true tokens: 29617
    Precision: 5977 / 14900 = 40.1141%
    Recall: 5977 / 29617 = 20.1810%
    F-score: 26.8527%
    Average precision: 18.9217%
    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.70
    No. predictions: 3135
    No. true tokens: 29617
    Precision: 1973 / 3135 = 62.9346%
    Recall: 1973 / 29617 = 6.6617%
    F-score: 12.0481%
    Average precision: 18.9217%
    ---------------------------------------------------------------------------
    Average P@10: 0.4850
    Average P@N: 0.3185
    Average EER: 0.2294
    ---------------------------------------------------------------------------


### VissionSpeechPSyC, filterbanks, logsumexp pooling

Model directory: models/train_visionspeech_psyc/da11f57155

Options: {'optimizer': {'learning_rate': 0.001, 'type': 'adam'}, 'n_most_common': 1000, 'rnd_seed': 1, 'batch_size': 64, 'speech_data_dir': 'data/fbank_vad', 'pool_shapes': [None, None, None, None, None, None], 'speech_label_dict': 'data/captions_content_dict.pkl', 'filter_shapes': [[40, 9, 1, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 96], [1, 10, 96, 1000]], 'ff_keep_prob': 1.0, 'script': 'train_visionspeech_psyc', 'visionsig_threshold': None, 'word_to_id_dict': '../vision_nn_flickr30k/data/flickr30k/word_to_id_content.pkl', 'pooling': 'logsumexp', 'n_max_epochs': 25, 'r': 1.0, 'model_dir': 'models/train_visionspeech_psyc', 'n_padded': 800, 'detect_sigmoid_threshold': 0.4, 'center_padded': False, 'visionsig_npz': '../vision_nn_flickr30k/models/train_bow_mlp/dea2850778/sigmoid_output_dict.flickr8k.npz'}
Results on dev:

    ---------------------------------------------------------------------------
    Sigmoid threshold: 0.40
    No. predictions: 14586
    No. true tokens: 29808
    Precision: 5826 / 14586 = 39.9424%
    Recall: 5826 / 29808 = 19.5451%
    F-score: 26.2468%
    Average precision: 18.1734%
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
