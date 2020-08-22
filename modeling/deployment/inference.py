import os
import sys


# path
cwd = os.getcwd()
sys.path.append(cwd)


# internal
from modeling.model import load_model


def predict(input):
    # load model
    model_path = ''
    model = load_model(model_path)

    # infer

    # output
    output = None

    return output