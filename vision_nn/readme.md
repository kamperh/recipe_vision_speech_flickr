Vision Neural Networks Trained on Flickr30k
===========================================


Overview
--------
VGG code is based on <https://www.cs.toronto.edu/~frossard/post/vgg16/>.
Flickr30k is split into train/dev/test following the same split used in
<http://cs.stanford.edu/people/karpathy/deepimagesent/>. The splits are given
in the `data/flickr30k` directory.


Preliminaries
-------------
Download the VGG weights in Numpy archive format:

    cd data/
    wget https://www.cs.toronto.edu/~frossard/vgg16/vgg16_weights.npz
    cd ..


