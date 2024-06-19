""" Tensorflow Preprocessing Adapter

Allows use of Tensorflow preprocessing pipeline in PyTorch Transform

Copyright of original Tensorflow code below.

Hacked together by / Copyright 2020 Ross Wightman
"""

# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""ImageNet preprocessing for MnasNet."""
import tensorflow.compat.v1 as tf
import numpy as np

IMAGE_SIZE = 224
CROP_PADDING = 32

tf.compat.v1.disable_eager_execution()

def distorted_bounding_box_crop(image_bytes,
                                bbox,
                                min_object_covered=0.1,
                                aspect_ratio_range=(0.75, 1.33),
                                area_range=(0.05, 1.0),
                                max_attempts=100,
                                scope=None):
    """Generates cropped_image using one of the bboxes randomly distorted.

    See `tf.image.sample_distorted_bounding_box` for more documentation.

    Args:
      image_bytes: `Tensor` of binary image data.
      bbox: `Tensor` of bounding boxes arranged `[1, num_boxes, coords]`
          where each coordinate is [0, 1) and the coordinates are arranged
          as `[ymin, xmin, ymax, xmax]`. If num_boxes is 0 then use the whole
          image.
      min_object_covered: An optional `float`. Defaults to `0.1`. The cropped
          area of the image must contain at least this fraction of any bounding
          box supplied.
      aspect_ratio_range: An optional list of `float`s. The cropped area of the
          image must have an aspect ratio = width / height within this range.
      area_range: An optional list of `float`s. The cropped area of the image
          must contain a fraction of the supplied image within in this range.
      max_attempts: An optional `int`. Number of attempts at generating a cropped
          region of the image of the specified constraints. After `max_attempts`
          failures, return the entire image.
      scope: Optional `str` for name scope.
    Returns:
      cropped image `Tensor`
    """
    with tf.name_scope(scope, 'distorted_bounding_box_crop', [image_bytes, bbox]):
        shape = tf.image.extract_jpeg_shape(image_bytes)
        sample_distorted_bounding_box = tf.image.sample_distorted_bounding_box(
            shape,
            bounding_boxes=bbox,
            min_object_covered=min_object_covered,
            aspect_ratio_range=aspect_ratio_range,
            area_range=area_range,
            max_attempts=max_attempts,
            use_image_if_no_bounding_boxes=True)
        bbox_begin, bbox_size, _ = sample_distorted_bounding_box

        # Crop the image to the specified bounding box.
        offset_y, offset_x, _ = tf.unstack(bbox_begin)
        target_height, target_width, _ = tf.unstack(bbox_size)
        crop_window = tf.stack([offset_y, offset_x, target_height, target_width])
        image = tf.image.decode_and_crop_jpeg(image_bytes, crop_window, channels=3)

        return image


def _at_least_x_are_equal(a, b, x):
    """At least `x` of `a` and `b` `Tensors` are equal."""
    match = tf.equal(a, b)
    match = tf.cast(match, tf.int32)
    return tf.greater_equal(tf.reduce_sum(match), x)


def _decode_and_random_crop(image_bytes, image_size, resize_method):
    """Make a random crop of image_size."""
    bbox = tf.constant([0.0, 0.0, 1.0, 1.0], dtype=tf.float32, shape=[1, 1, 4])
    image = distorted_bounding_box_crop(
        image_bytes,
        bbox,
        min_object_covered=0.1,
        aspect_ratio_range=(3. / 4, 4. / 3.),
        area_range=(0.08, 1.0),
        max_attempts=10,
        scope=None)
    original_shape = tf.image.extract_jpeg_shape(image_bytes)
    bad = _at_least_x_are_equal(original_shape, tf.shape(image), 3)

    image = tf.cond(
        bad,
        lambda: _decode_and_center_crop(image_bytes, image_size),
        lambda: tf.image.resize([image], [image_size, image_size], resize_method)[0])

    return image


def _decode_and_center_crop(image_bytes, image_size, resize_method):
    """Crops to center of image with padding then scales image_size."""
    shape = tf.image.extract_jpeg_shape(image_bytes)
    image_height = shape[0]
    image_width = shape[1]

    padded_center_crop_size = tf.cast(
        ((image_size / (image_size + CROP_PADDING)) *
         tf.cast(tf.minimum(image_height, image_width), tf.float32)),
        tf.int32)

    offset_height = ((image_height - padded_center_crop_size) + 1) // 2
    offset_width = ((image_width - padded_center_crop_size) + 1) // 2
    crop_window = tf.stack([offset_height, offset_width,
                            padded_center_crop_size, padded_center_crop_size])
    image = tf.image.decode_and_crop_jpeg(image_bytes, crop_window, channels=3)
    image = tf.image.resize([image], [image_size, image_size], resize_method)[0]

    return image


def _flip(image):
    """Random horizontal image flip."""
    image = tf.image.random_flip_left_right(image)
    return image


def preprocess_for_train(image_bytes, use_bfloat16, image_size=IMAGE_SIZE, interpolation='bicubic'):
    """Preprocesses the given image for evaluation.

    Args:
      image_bytes: `Tensor` representing an image binary of arbitrary size.
      use_bfloat16: `bool` for whether to use bfloat16.
      image_size: image size.
      interpolation: image interpolation method

    Returns:
      A preprocessed image `Tensor`.
    """
    resize_method = tf.image.ResizeMethod.BICUBIC if interpolation == 'bicubic' else tf.image.ResizeMethod.BILINEAR
    image = _decode_and_random_crop(image_bytes, image_size, resize_method)
    image = _flip(image)
    image = tf.reshape(image, [image_size, image_size, 3])
    image = tf.image.convert_image_dtype(
        image, dtype=tf.bfloat16 if use_bfloat16 else tf.float32)
    return image


def preprocess_for_eval(image_bytes, use_bfloat16, image_size=IMAGE_SIZE, interpolation='bicubic'):
    """Preprocesses the given image for evaluation.

    Args:
      image_bytes: `Tensor` representing an image binary of arbitrary size.
      use_bfloat16: `bool` for whether to use bfloat16.
      image_size: image size.
      interpolation: image interpolation method

    Returns:
      A preprocessed image `Tensor`.
    """
    resize_method = tf.image.ResizeMethod.BICUBIC if interpolation == 'bicubic' else tf.image.ResizeMethod.BILINEAR
    image = _decode_and_center_crop(image_bytes, image_size, resize_method)
    image = tf.reshape(image, [image_size, image_size, 3])
    image = tf.image.convert_image_dtype(
        image, dtype=tf.bfloat16 if use_bfloat16 else tf.float32)
    return image


def preprocess_image(image_bytes,
                     is_training=False,
                     use_bfloat16=False,
                     image_size=IMAGE_SIZE,
                     interpolation='bicubic'):
    """Preprocesses the given image.

    Args:
      image_bytes: `Tensor` representing an image binary of arbitrary size.
      is_training: `bool` for whether the preprocessing is for training.
      use_bfloat16: `bool` for whether to use bfloat16.
      image_size: image size.
      interpolation: image interpolation method

    Returns:
      A preprocessed image `Tensor` with value range of [0, 255].
    """
    if is_training:
        return preprocess_for_train(image_bytes, use_bfloat16, image_size, interpolation)
    else:
        return preprocess_for_eval(image_bytes, use_bfloat16, image_size, interpolation)


class TfPreprocessTransform:

    def __init__(self, is_training=False, size=224, interpolation='bicubic'):
        self.is_training = is_training
        self.size = size[0] if isinstance(size, tuple) else size
        self.interpolation = interpolation
        self._image_bytes = None
        self.process_image = self._build_tf_graph()
        self.sess = None

    def _build_tf_graph(self):
        with tf.device('/cpu:0'):
            self._image_bytes = tf.placeholder(
                shape=[],
                dtype=tf.string,
            )
            img = preprocess_image(
                self._image_bytes, self.is_training, False, self.size, self.interpolation)
        return img

    def __call__(self, image_bytes):
        if self.sess is None:
            self.sess = tf.Session()
        img = self.sess.run(self.process_image, feed_dict={self._image_bytes: image_bytes})
        img = img.round().clip(0, 255).astype(np.uint8)
        if img.ndim < 3:
            img = np.expand_dims(img, axis=-1)
        img = np.rollaxis(img, 2)  # HWC to CHW
        return img
