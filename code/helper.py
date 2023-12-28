import csv
import sys
import os
import numpy as np

def read_file(file):
    params = {}
    with open(file, 'r') as f:
        for line in f:
            splits = line.split('=')
            if len(splits) > 1:  # avoid comment
                key, value = splits[0:2]
                params[key] = value.replace('\n', '')
    return params


def loadcsv(file):
    params = {}
    with open(file, 'r') as f:
        csv.field_size_limit(sys.maxsize)
        csv_file = csv.reader(f, delimiter='=')
        for line in csv_file:
            if len(line) > 1:  # avoid comment
                key, value = line[0:2]
                params[key] = value.replace('\n', '')
        return params


def load_params(filename):
    for f in os.listdir():
        if f.endswith(filename):
            # return load_csv
            return read_file(f)
    raise Exception('No file ends with the given filename')


if __name__ == "__main__":
    params = load_params("params.txt")
    print(params)

