import xml
import os
import xmlutils.xml2csv as x2c 
import xml.etree.ElementTree as ET

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

bucket = storage_client.get_bucket('monsoon_1')
blob = bucket.blob('country.xml')
blob.upload_from_filename('country.xml')
print bucket
blob.download_to_filename('country1.xml')
doc = ET.parse('country1.xml')
root = doc.getroot()
#remove some data with business criteria
for country in root.findall('country'):
     rank = int(country.find('rank').text)
     if rank > 50:
         root.remove(country)
doc.write('output.xml')

#convert to csv
converter = x2c.xml2csv('output.xml','country1.csv')
converter.convert()

#upload csv to bucket

blob = bucket.blob('country.csv')
blob.upload_from_filename('country.csv')
blob.make_public()
