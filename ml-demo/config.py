gs_bucket_name="data-labeling-demo"
Bucket_uri="gs://data-labeling-demo"
version=1
#it will create fresh artifact version after each run
store_artifacts=Bucket_uri + "/" + str(version)
data_path=Bucket_uri + "/" + "data/data_raw.csv"
processed_data=Bucket_uri + "/" + "processed/data_processed.csv"
