import numpy as np

class Embedding:
    def __init__(self, dim):
        self.dim = dim

    def embed(self, terms):
        return np.random.rand(self.dim)
