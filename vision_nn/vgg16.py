"""
Functions for building the VGG16 network.

See <https://www.cs.toronto.edu/~frossard/post/vgg16/> for details.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017
"""

import numpy as np
import tensorflow as tf

from imagenet_classes import class_names

TF_DTYPE = tf.float32
TF_ITYPE = tf.int32


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def build_conv2d_relu(x, filter_shape, name):
    with tf.variable_scope(name):
        W = tf.get_variable(
            "W", filter_shape, dtype=TF_DTYPE, initializer=tf.contrib.layers.xavier_initializer()
            )
        b = tf.get_variable(
            "b", [filter_shape[-1]], dtype=TF_DTYPE, initializer=tf.random_normal_initializer()
            )
        x = tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")
        x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x), [W, b]


def build_maxpool2d(x, pool_shape, name=None):
    """Max pool over `x` using a `pool_shape` of [pool_height, pool_width]."""
    ksize = [1,] + pool_shape + [1,]
    return tf.nn.max_pool(x, ksize=ksize, strides=ksize, padding="SAME", name=name)


def build_linear(x, n_output, name):
    with tf.variable_scope(name):
        n_input = x.get_shape().as_list()[-1]
        W = tf.get_variable(
            "W", [n_input, n_output], dtype=TF_DTYPE, initializer=tf.contrib.layers.xavier_initializer()
            )
        b = tf.get_variable(
            "b", [n_output], dtype=TF_DTYPE, initializer=tf.random_normal_initializer()
            )
    return tf.matmul(x, W) + b, [W, b]


#-----------------------------------------------------------------------------#
#                                    VGG16                                    #
#-----------------------------------------------------------------------------#

def build_vgg16(x):

    vgg_dict = {}
    parameters = []

    with tf.variable_scope("preprocess"):
        mean = tf.constant([123.68, 116.779, 103.939], dtype=TF_DTYPE, shape=[1, 1, 1, 3], name="img_mean")
        x_min_mean = x - mean

    conv1_1, params = build_conv2d_relu(x_min_mean, [3, 3, 3, 64], "conv1_1")
    parameters.extend(params)
    conv1_2, params = build_conv2d_relu(conv1_1, [3, 3, 64, 64], "conv1_2")
    parameters.extend(params)

    pool1 = build_maxpool2d(conv1_2, [2, 2], name="pool1")

    conv2_1, params = build_conv2d_relu(pool1, [3, 3, 64, 128], "conv2_1")
    parameters.extend(params)
    conv2_2, params = build_conv2d_relu(conv2_1, [3, 3, 128, 128], "conv2_2")
    parameters.extend(params)

    pool2 = build_maxpool2d(conv2_2, [2, 2], name="pool2")

    conv3_1, params = build_conv2d_relu(pool2, [3, 3, 128, 256], "conv3_1")
    parameters.extend(params)
    conv3_2, params = build_conv2d_relu(conv3_1, [3, 3, 256, 256], "conv3_2")
    parameters.extend(params)
    conv3_3, params = build_conv2d_relu(conv3_2, [3, 3, 256, 256], "conv3_3")
    parameters.extend(params)

    pool3 = build_maxpool2d(conv3_3, [2, 2], name="pool3")

    conv4_1, params = build_conv2d_relu(pool3, [3, 3, 256, 512], "conv4_1")
    parameters.extend(params)
    conv4_2, params = build_conv2d_relu(conv4_1, [3, 3, 512, 512], "conv4_2")
    parameters.extend(params)
    conv4_3, params = build_conv2d_relu(conv4_2, [3, 3, 512, 512], "conv4_3")
    parameters.extend(params)

    pool4 = build_maxpool2d(conv4_3, [2, 2], name="pool4")

    conv5_1, params = build_conv2d_relu(pool4, [3, 3, 512, 512], "conv5_1")
    parameters.extend(params)
    conv5_2, params = build_conv2d_relu(conv5_1, [3, 3, 512, 512], "conv5_2")
    parameters.extend(params)
    conv5_3, params = build_conv2d_relu(conv5_2, [3, 3, 512, 512], "conv5_3")
    parameters.extend(params)

    pool5 = build_maxpool2d(conv5_3, [2, 2], name="pool5")
    pool5_flat = tf.contrib.layers.flatten(pool5)

    fc6, params = build_linear(pool5_flat, 4096, "fc6")
    parameters.extend(params)
    fc6_relu = tf.nn.relu(fc6)

    fc7, params = build_linear(fc6_relu, 4096, "fc7")
    vgg_dict["fc7"] = fc7
    parameters.extend(params)
    fc7_relu = tf.nn.relu(fc7)
    vgg_dict["fc7_relu"] = fc7_relu

    fc8, params = build_linear(fc7_relu, 1000, "fc8")
    parameters.extend(params)

    prob = tf.nn.softmax(fc8, name="prob")
    vgg_dict["prob"] = prob

    return vgg_dict, parameters


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():

    from os import path
    from scipy.misc import imread, imresize

    # Input
    # image = imread("data/laska.png", mode="RGB")
    image = imread("data/1007129816_e794419615.jpg", mode="RGB")
    image = imresize(image, (224, 224))

    # Pretrained weights
    weights_fn = path.join("data", "vgg16_weights.npz")
    assert path.isfile(weights_fn)
    print "Reading:", weights_fn
    weights = np.load(weights_fn)

    # Build model
    x = tf.placeholder(TF_DTYPE, [None, 224, 224, 3])
    vgg_dict, parameters = build_vgg16(x)

    # Run model
    config = None
    init = tf.initialize_all_variables()
    with tf.Session(config=config) as session:
        session.run(init)

        print "Pretrained parameters"
        for i, key in enumerate(sorted(weights.keys())):
            print("{}: {}".format(key, list(weights[key].shape)))
            session.run(parameters[i].assign(weights[key]))

        # VGG output
        fc7_relu = session.run(vgg_dict["fc7_relu"], feed_dict={x: [image]})[0]
        prob = session.run(vgg_dict["prob"], feed_dict={x: [image]})[0]

    # Print output
    predictions = (np.argsort(prob)[::-1])[0:5]
    for p in predictions:
        print class_names[p], prob[p]
    print fc7_relu[np.where(fc7_relu > 0)[0]][:100]


if __name__ == "__main__":
    main()
