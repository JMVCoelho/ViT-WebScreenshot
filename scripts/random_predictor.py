import os
import random
import math 
from sklearn.metrics import mean_squared_error

import sys

data_path = sys.argv[1]
#data

test_ids = [f.split('.')[0] for f in os.listdir(os.path.join(data_path, "test")) if f.endswith('.jpg')]

all_labels = {}

with open(os.path.join(data_path, "labels.tsv"), 'r') as file:
    for line in file:
        img_id, label = line.strip().split('\t')

        if img_id in test_ids:
            all_labels[img_id] = float(label)

min_inlink = min(list(all_labels.values()))
max_inlink = max(list(all_labels.values()))

labels = {k:(v-min_inlink)/(max_inlink-min_inlink) for k,v in all_labels.items() if k in test_ids}

assert len(labels) == len(test_ids)

random_predictor = {k:random.random() for k,v in labels.items()}

# python 3.7>: dict order is preserved, can just cast
rmse = mean_squared_error(list(labels.values()), list(random_predictor.values()), squared=False)

print(f"Random predictor RMSE: {rmse}")
