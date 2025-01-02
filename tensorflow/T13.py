import numpy as np
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
import seaborn as sn

print(tf.__version__)


# Intialization of Tensor
x = tf.constant(4, dtype=tf.int64)  # << data type default = int32
x = tf.constant([[1, 2, 3], [4, 5, 6]])
x = tf.ones(shape=(8, 4), dtype=tf.int8)
x = tf.zeros(shape=(4, 4))
x = tf.eye(4)  # indentity matrix
x = tf.random.normal(shape=(4, 4), mean=80, stddev=2)
x = tf.random.uniform(shape=(4, 3), minval=1, maxval=5)
x = tf.range(9)
x = tf.cast(x, dtype=tf.int64)
# Mathematical Operations on Tensor
a = tf.constant([1, 2, 3])
b = tf.constant([9, 8, 7])

x = a + b

x = a - b
x = b - a
x = a * b
x = a / b
x = b / a
x = b**a
x = a % b

x = tf.tensordot(a, b, axes=1)
print(x)
# Indexing
