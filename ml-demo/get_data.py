import os
import wget
import tensorflow as tf
# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048
import config

import pandas as pd
df=pd.read_csv('one_hot_encoded.csv')
df=df.drop(labels=['Unnamed: 0'],axis=1)
# print(df.head())
df.to_csv(config.data_path)


# upload file to google storage
from google.cloud import storage
storage_client = storage.Client()
bucket = storage_client.bucket(config.gs_bucket_name)
bucket.blob('data/data_raw.csv').upload_from_filename('data_raw.csv', content_type='text/csv')
print("Data DownLoaded Sucessfully")