import pickle

def load_train_data(path):
    with open(path, "rb") as f:
        return pickle.load(f)
