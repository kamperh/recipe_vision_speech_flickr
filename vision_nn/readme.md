Vision Neural Networks Trained on Flickr30k
===========================================


Overview
--------
VGG code is based on <https://www.cs.toronto.edu/~frossard/post/vgg16/>.
Flickr30k is split into train/dev/test following the same split used in
<http://cs.stanford.edu/people/karpathy/deepimagesent/>. The splits are given
in the `../data/` directory.


Preliminaries
-------------
Download the VGG-16 weights in Numpy archive format:

    cd data/
    wget https://www.cs.toronto.edu/~frossard/vgg16/vgg16_weights.npz
    cd ..

Get Flickr30k captions:

    ./get_captions_word_ids.py \
        /share/data/vision-greg/flickr30k/results_20130124.token \
        data/flickr30k


Apply pretrained VGG-16 to Flickr8k and Flickr30k
-------------------------------------------------
Apply VGG16 to all the Flickr30k images:

    mkdir data/flickr30k/
    ./apply_vgg16.py --output_layer fc7 --batch_size 37 \
        /share/data/vision-greg/flickr30k/flickr30k-images/ \
        data/flickr30k/fc7.npz

Apply VGG16 to all the Flickr8k images:

    mkdir data/flickr8k/
    ./apply_vgg16.py --output_layer fc7 --batch_size 93 \
        /share/data/lang/users/kamperh/flickr_multimod/Flickr8k_Dataset/Flicker8k_Dataset/ \
        data/flickr8k/fc7.npz


Bag-of-words MLP for Flickr30k on top of VGG16
----------------------------------------------
Train and evaluate a bag-of-words MLP on Flickr30k VGG16 features:

    ./train_bow_mlp.py
    ./apply_bow_mlp.py models/train_bow_mlp/d64b725040 dev
    ./eval_precision_recall.py --analyze --sigmoid_threshold 0.4 \
        models/train_bow_mlp/d64b725040 dev

This should give approximately the following scores:

    Sigmoid threshold: 0.40
    No. predictions: 6726
    No. true tokens: 23428
    Precision: 3373 / 6726 = 50.1487%
    Recall: 3373 / 23428 = 14.3973%
    F-score: 22.3718%
    Average precision: 22.8551%

This is the model that will be used for visual processing in the experiments
for grounding speech, so the model directory should be noted. In my case, the
model was saved to:

    models/train_bow_mlp/d64b725040

The model needs to be applied to the Flickr8k dataset for the visual grounding
experiments. No training occurs. To apply the model to Flickr8k, and inspect
predictions, run:

    ./apply_bow_mlp.py --batch_size 93 models/train_bow_mlp/d64b725040 flickr8k
    ./show_predictions.py --sigmoid_threshold 0.7 \
        models/train_bow_mlp/d64b725040/sigmoid_output_dict.flickr8k.npz \
        data/flickr30k/word_to_id_content.pkl

This shows some of the system outputs, e.g.:

    Image: 1007320043_627395c3d8
    Predicted: ['young', 'red', 'child', 'little', 'climbing', 'playground']

The complte output (used in the subsequent grounding experiments) is saved as:

    models/train_bow_mlp/d64b725040/sigmoid_output_dict.flickr8k.npz
