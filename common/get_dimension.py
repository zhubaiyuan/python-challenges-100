import numpy as np


def get_dimension(values2dim):
    if isinstance(values2dim, list):
        return (len(values2dim), len(values2dim[0]))
    if isinstance(values2dim, np.ndarray):
        return values2dim.shape
    raise ValueError("unsupported type", type(values2dim))
