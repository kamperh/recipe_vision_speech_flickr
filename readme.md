Multimodal Modelling of Flickr Vision and Speech Data
=====================================================

Contributors
------------
- [Herman Kamper](http://www.kamperh.com/)
- Shane Settle
- [Karen Livescu](http://ttic.uchicago.edu/~klivescu/)
- [Greg Shakhnarovich](http://ttic.uchicago.edu/~gregory/)


Overview
--------
This is a recipe for grounding untranscribed speech using paired images.
Details are given in [Kamper et al., 2017](https://arxiv.org/abs/1703.08136):

- H. Kamper, S. Settle, G. Shakhnarovich, and K. Livescu, "Visually grounded
  learning of keyword prediction from untranscribed speech," *arXiv preprint
  arXiv:1703.08136*, 2017.

Please cite this paper if you use this code.


Disclaimer
----------
The code provided here is not pretty. But I believe research should be
reproducible, and I hope that this repository is sufficient to make this
possible for the above paper. I provide no guarantees with the code, but please
let me know if you have any problems, find bugs or have general comments.


Datasets
--------
The following datasets need to be obtained:

- [Flickr audio](https://groups.csail.mit.edu/sls/downloads/flickraudio/)
- [Flickr8k images](http://nlp.cs.illinois.edu/HockenmaierGroup/Framing_Image_Description/Flickr8k_Dataset.zip)
- [Flickr8k text](http://nlp.cs.illinois.edu/HockenmaierGroup/Framing_Image_Description/Flickr8k_Dataset.zip)
- [Flickr30k](http://shannon.cs.illinois.edu/DenotationGraph/)

Flickr30k is used for training a vision tagging system. The Flickr8k audio and
image datasets gives paired images with spoken captions; we do not use the
labels from either of these. The Flickr8k text corpus is purely for reference.
The Flickr8k dataset can also be browsed directly
[here](http://nlp.cs.illinois.edu/HockenmaierGroup/8k-pictures.html).
