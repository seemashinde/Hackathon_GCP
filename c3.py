import xml
import untangle

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

bucket = storage_client.get_bucket('monsoon_1')

obj = untangle.parse("gs://monsoon_1/Test1.xml")

print obj.root.child['name']
