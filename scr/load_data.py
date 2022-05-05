# Read data from data source
# Save it in the data/raw for futher process

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns] #to remove space in dataset in each colms
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    sep = config["load_data"]["sep"]
    index = config["load_data"]["index"]
    df.to_csv(raw_data_path, sep=sep, index=index, header=new_cols)



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)