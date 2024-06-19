import unittest

from tensorflow.keras import backend as K
import tensorflow as tf
import numpy as np

tf.experimental.numpy.experimental_enable_numpy_behavior()
from src.models.model_evaluation import f1, iou


class TestMetrics(unittest.TestCase):

    def test_f1(self):
        # Create random input arrays
        y_true = np.random.rand(10, 28, 28) > 0.5
        y_pred = np.random.rand(10, 28, 28) > 0.5

        # Call the f1 function with the input arrays
        f1_score = f1(y_true.astype('float32'), y_pred.astype('float32'))
        print(type(f1_score))
        # Check if the returned value is not None and an instance of a floating oint number (float)

        self.assertIsNotNone(f1_score.numpy())
        self.assertIsInstance(f1_score, type(tf.constant(0)))
        # This checks for the EagerTensor class

    def test_f(self):
        # Create random input arrays (images)
        y_true = np.random.rand(1, 28, 28, 1).astype('float32')
        y_pred = np.random.rand(1, 28, 28, 1).astype('float32')

        intersection = K.sum(K.abs(y_true * y_pred), keepdims=False)
        total = K.sum(K.square(y_true), [1, 2, 3]) + K.sum(K.square(y_pred), [1, 2, 3])
        union = total - intersection
        result = (intersection + K.epsilon()) / (union + K.epsilon())

        # Evaluate the f function
        eval_result = result.numpy()

        self.assertIsNotNone(eval_result)
        self.assertIsInstance(eval_result, np.ndarray)


if __name__ == '__main__':
    unittest.main()
