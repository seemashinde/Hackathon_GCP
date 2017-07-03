import xml
import os
import time
import xmlutils.xml2csv as x2c 
import xml.etree.ElementTree as ET

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()
#create new bucket

bucket_name="monsoon_hackers_"+str(time.time()).split(".")[0]
storage_client.create_bucket(bucket_name)
print "Bucket created:"+bucket_name
bucket = storage_client.get_bucket(bucket_name)

#Upload XML
blob = bucket.blob('country.xml')
blob.upload_from_filename('country.xml')
print "XML Copied to newly created bucket"

blob.download_to_filename('country1.xml')
print "Downloded xml file"

print "Parsing XML file for changes according to business rule"
doc = ET.parse('country1.xml')
root = doc.getroot()
#remove some data with business criteria
for country in root.findall('country'):
     rank = int(country.find('rank').text)
     if rank > 50:
         root.remove(country)
print "Writing cleansed xml"
doc.write('output.xml')

#convert to csv
print "Transforming XML to CSV"
converter = x2c.xml2csv('output.xml','country1.csv')
converter.convert()

#upload csv to bucket
print "Uploading transformed csv to bucket"
blob = bucket.blob('country.csv')
blob.upload_from_filename('country.csv')
#Making csv file publicly available
print "Making csv file publicly available"
blob.make_public()
#Getting the media link for the blob
link=blob.media_link
print " Access this link for downloading csv file: " +link
