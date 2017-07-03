import boto

import gcs_oauth2_boto_plugin
MSN_BUCKET1 = 'MSNBKT1' 
MSN_BUCKET2 = 'MSNBKT2' 

GOOGLE_STORAGE = 'gs'

# If there is no domain for your project, then project_id = 'YOUR_PROJECT'
project_id = 'hack-gcph-5'

CLIENT_ID = 'GOOGMKN3HTEYYYADJ2IT'
CLIENT_SECRET = 'r9DCMNszQRSurzNeYeaMAs05Cn6VCB6cBMjcKils'

gcs_oauth2_boto_plugin.SetFallbackClientIdAndSecret(CLIENT_ID, CLIENT_SECRET)

print 'Successfully login' 



for name in (MSN_BUCKET1, MSN_BUCKET2):
  # Instantiate a BucketStorageUri object.
  #uri = boto.storage_uri(name, GOOGLE_STORAGE)
  # Try to create the bucket.
  
  uri = boto.storage_uri('', GOOGLE_STORAGE)
# If the default project is defined, call get_all_buckets() without arguments.
for bucket in uri.get_all_buckets():
  print bucket.name
  
  try:
    # If the default project is defined,
    # you do not need the headers.
    # Just call: uri.create_bucket()
    #header_values = {"x-goog-project-id": project_id}
    #uri.create_bucket('new_monsoon_bucket1')

    print 'Successfully created bucket "%s"' % name
  except boto.exception.StorageCreateError, e:
    print 'Failed to create bucket:', e