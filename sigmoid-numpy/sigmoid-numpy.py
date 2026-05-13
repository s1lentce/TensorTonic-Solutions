import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x_typed = np.asarray(x , dtype = float)
    q = 1/(1+np.exp(-(x_typed)))
    return q