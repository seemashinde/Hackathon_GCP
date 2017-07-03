import xml
import xml.dom.minidom as mdom
import urllib



# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

bucket = storage_client.get_bucket('monsoon_1')

blob = bucket.get_blob('gs://monsoon_1/Test1.xml')

print(blob.download_as_string())

#doc = mdom.parseString(blob)
#print doc



  