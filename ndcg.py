import numpy as np

def dcg(scores):
    return sum(s / np.log2(i + 2) for i, s in enumerate(scores))

def ndcg(predicted, ideal):
    return dcg(predicted) / dcg(ideal)
