Vision Neural Networks Trained on Flickr30k
===========================================


Overview
--------
VGG-16 code is based on <https://www.cs.toronto.edu/~frossard/post/vgg16/>.
Flickr30k is split into train/dev/test following the same split used in
<http://cs.stanford.edu/people/karpathy/deepimagesent/>, but see the note
below. The splits are given in the `../data/` directory.

Instead of training on the Flickr30k training set and then evaluating on dev
and test (as would be standard), we instead train on all the Flickr30k images,
excluding those that are in the Flickr8k training or test sets. None of the
images on which we train the vision system here are used during either training
or testing of the visually grounded speech model. By training the vision system
in this way, we have more data to train on. But this means that evaluation on
the Flickr30k development data is not sensible here. The images on which we
train are given in `../data/flickr30k_all_no8ktraintest.txt.` By setting
`train_tag` to "train" in the `options_dict` of `train_bow_mlp.py`, you will
only train on the Flickr30k training set, and evaluation on the Flickr30k
development data would be sensible.


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
Apply VGG-16 to all the Flickr30k images:

    mkdir data/flickr30k/
    ./apply_vgg16.py --output_layer fc7 --batch_size 37 \
        /share/data/vision-greg/flickr30k/flickr30k-images/ \
        data/flickr30k/fc7.npz

Apply VGG-16 to all the Flickr8k images:

    mkdir data/flickr8k/
    ./apply_vgg16.py --output_layer fc7 --batch_size 93 \
        /share/data/lang/users/kamperh/flickr_multimod/Flickr8k_Dataset/Flicker8k_Dataset/ \
        data/flickr8k/fc7.npz


Bag-of-words MLP for Flickr30k on top of VGG-16
-----------------------------------------------
Train a bag-of-words MLP on Flickr30k VGG-16 features:

    ./train_bow_mlp.py

To evaluate this model on Flickr30k on development data, run:

    ./apply_bow_mlp.py models/train_bow_mlp/d64b725040 dev
    ./eval_precision_recall.py --analyze --sigmoid_threshold 0.4 \
        models/train_bow_mlp/dea2850778 dev

As mentioned above, this will give very high performance since we train on some
of these development images. To obtain a meaningful result, change `train_tag`
in the `options_dict` of `train_bow_mlp.py` to "train". Then training will
not be performed on any of the development or test images.

The above model will be used for visual processing in the experiments for
grounding speech, so the model directory should be noted. In my case, the model
was saved to:

    models/train_bow_mlp/dea2850778

The model needs to be applied to the Flickr8k dataset for the visual grounding
experiments. No training occurs. To apply the model to Flickr8k, and inspect
predictions, run:

    ./apply_bow_mlp.py --batch_size 93 models/train_bow_mlp/dea2850778 flickr8k
    ./show_predictions.py --sigmoid_threshold 0.7 \
        models/train_bow_mlp/dea2850778/sigmoid_output_dict.flickr8k.npz \
        data/flickr30k/word_to_id_content.pkl

This shows some of the system outputs, e.g.:

    Image: 1093716555_801aacef79
    Predicted: ['people', 'dirt', 'across', 'mountain', 'mountains', 'hiking']

The complete output (used in the subsequent grounding experiments) is saved as:

    models/train_bow_mlp/dea2850778/sigmoid_output_dict.flickr8k.npz
