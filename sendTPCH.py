import os
import requests

top_dir = "./dummyData"
url = "http://localhost:8888/"

'''
This script sends the TPCH data to the server using the http interface.
You can see the data in the server by visiting the following URL:
http://localhost:8888/TPCH_DUMMY
'''




# recursive function to get all files in a directory
def get_files(directory):
    files = []
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isdir(path):
            files.extend(get_files(path))
        else:
            files.append(path)
    return files


for file in get_files(top_dir):
    sub_dir = file.replace(top_dir, "").rsplit("/", 1)[0]
    with open(file, 'rb') as file:
        files = {'file': file}
        writeURL = f"{url}TPCH_DUMMY{sub_dir}/"
        response = requests.post(writeURL, files=files)


# TO DELETE FILES
# for i in range(1,11):
#     requests.delete(f"{url}supplier{i}.parquet")

