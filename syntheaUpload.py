import json
import os
import requests


#fhir server endpoint
URL = "https://smilecdr-api.fhirsandbox.aws.greenwayhealth.com/"

filePath = 'C:/Users/jcturner/Documents/_WORKSPACE/_projects/Greenway/synthea_sample_data_fhir_r4_sep2019/fhir'

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

#loop over all files in the output folder in order to upload each json file for each patient.
for dirpath, dirnames, files in os.walk(filePath):

    for file_name in files:
        
        try:
            with open(filePath + '/' + file_name, "r") as bundle_file:
                data = bundle_file.read()

            r = requests.post(url = URL, data = data, headers = headers, auth=('USERNAME', 'PASSWORD'))

            #output file name that was processed
            print(f'HTTP {r.status_code} - {file_name}')
        except Exception as e:
            print(f'unable to process: {file_name} with error: {e}')


        