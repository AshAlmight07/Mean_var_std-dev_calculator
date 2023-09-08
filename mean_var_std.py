"""
Mean, Variance, and Standard Deviation Calculator

This module defines a function for calculating the mean, variance, standard deviation,
max, min, and sum of rows, columns, and elements in a 3x3 matrix.

Author: Hryday Naidu
"""
import numpy as np

def calculate(numbers):
    """
    Calculate the mean, variance, standard deviation, max, min, and sum
    of the rows, columns, and elements in a 3x3 matrix.

    Args:
        numbers (list): A list containing 9 digits.

    Returns:
        dict: A dictionary containing the calculated statistics.
    """
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers")

    matrix = np.array(numbers).reshape(3,3)

    calculations = {
    'mean': [matrix.mean(axis=0).tolist(),
             matrix.mean(axis=1).tolist(),matrix.mean().tolist()],
    'variance': [matrix.var(axis=0).tolist(),matrix.var(axis=1).tolist(),
                 matrix.var().tolist()],
    'standard deviation': [matrix.std(axis=0).tolist(),
                           matrix.std(axis=1).tolist(),
                           matrix.std().tolist()],
    'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(),
            matrix.max().tolist()],
    'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(),
            matrix.min().tolist()],
    'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()]
  }

    return calculations
