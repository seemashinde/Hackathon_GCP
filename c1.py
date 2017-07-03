# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'monsoon_bkt2'

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

#print('Bucket {} created.'.format(bucket.name))

bucket = storage_client.get_bucket('monsoon_1')

for bucket in storage_client.list_buckets():
	print(bucket)
