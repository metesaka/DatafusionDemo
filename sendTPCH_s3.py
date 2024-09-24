import os
import boto3

top_dir = "./dummyData"
url = "http://localhost:8888/"
s3 = boto3.client('s3', endpoint_url='http://localhost:8333', aws_access_key_id='admin', aws_secret_access_key='admin')

'''
This script sends the TPCH data to the server using the S3 interface.
You can see the data in the server by visiting the following URL:
http://localhost:8888/buckets/tpchDummy

Or also you can see the bucket in the s3 interface:
http://localhost:8333/
'''


# recursive function to get all files in a directory
def get_files(directory):
    files = []
    for file in os.listdir(directory):
        if ".DS_Store" in file:
            continue
        path = os.path.join(directory, file)
        if os.path.isdir(path):
            files.extend(get_files(path))
        else:
            files.append(path)
    return files


for file in get_files(top_dir):
    sub_dir2 = file.replace(top_dir, "")
    s3.put_object(Bucket='tpchDummy', Key=sub_dir2, Body=open(file, 'rb'))



# TO DELETE FILES
# for i in range(1,11):
#     requests.delete(f"{url}supplier{i}.parquet")

