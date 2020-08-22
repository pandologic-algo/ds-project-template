# base
from labs import experiment_path
import json
import sys
import os
import argparse

# path
cwd = os.getcwd()
sys.path.append(cwd)


# internal
from modeling.experiment.model import *
from modeling.utils.data_handling import *
from modeling.utils.evaluation import *


# configs
data_path="datasets/example_dataset"
cv_config = dict(n=5, seed=111)
target_name="target"
features_names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7',
                'col8', 'col9', 'col10', 'col11', 'col12', 'col13', 'col14', 'col15']


def experiment(experiment_params, artifacts_path, metrics):
    """Run experiment"""


def get_parser():
    parser = argparse.ArgumentParser(description='Experiment params')

    # add arguments

    return parser


def process_arg_parser(parser):
    args = parser.parse_args()

    experiment_params = {'hyperparams': json.loads(args.hyperparams)}

    # get args

    # fill experiment func kwargs
    kwargs = {}

    return kwargs


if __name__ == '__main__':
    my_parser = get_parser()

    kwargs = process_arg_parser(my_parser)

    main(**kwargs)

