#read the data from data source
# save it in the data/RawData for further process
import os
#from get_data import read_params, get_data
from get_data import *
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    ## gaps in the spacing, list of new columns 
    new_cols = [col.replace(" ", "_") for col in df.columns]
    #print(new_cols)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)
    #df.head(2)

#%%
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)    
# %%
