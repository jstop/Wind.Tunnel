import json
import os
import requests


#fhir server endpoint
URL = "https://sandbox-api.fhirsandbox.aws.greenwayhealth.com/$expunge"

filePath = '/Users/joshuastein/workspace/greenway/fhir/Wind.Tunnel/expunge.json'

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

try:
    with open(filePath) as bundle_file:
        data = bundle_file.read()
    r = requests.delete(url = URL, data = data, headers = headers, auth=('admin','password')) 
    print(f'HTTP {r.status_code} - {filePath}')
except Exception as e:
    print(f'unable to process: {filePath} with error: {e}')
