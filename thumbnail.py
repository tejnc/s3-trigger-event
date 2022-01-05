import boto3
import os
from PIL import Image

temp_folder_name = "/tmp"

def main(event, context):
    s3_res = boto3.resource("s3")
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    _name = key.split("/")
    name = _name[1]
    path = f"/tmp/{name}"
    print(path)
    os.makedirs(temp_folder_name, exist_ok=True)
    
    print("downloading file")
    response = s3_res.meta.client.download_file(bucket_name,key, path)
    print(response)
    image_path = reduce_size(downloaded_path=path)
    image_name = image_path.split("/")[-1]
    print(image_name)
    new_image_path = "thumbnails/{}".format(image_name)
    print(new_image_path)
    print("uploading file")
    s3_res.meta.client.upload_file(image_path,bucket_name,new_image_path)


def reduce_size(downloaded_path):
    i = Image.open(downloaded_path)
    f = downloaded_path.split("/")[-1]
    fn, fext = os.path.splitext(f) # file_name , file_extension
    i.thumbnail((200,200))
    os.makedirs("/tmp/200/")
    i.save("/tmp/200/{}_200{}".format(fn,fext))
    file_path = "/tmp/200/{}_200{}".format(fn,fext)
    print(file_path)
    return file_path

