import base64
import json
import os
import requests

env = json.loads(open("constants/env.json").read())
url = env["url"]
apiKey = env["X-API-Key"]
parentFolder = "data"


def upload(folder):
    if not os.path.exists(parentFolder + "/" + folder):
        print("images folder does not exits, please make a folder 'images' and paste all images in that folder")
        exit()
    final_array = []
    print("Processing")
    images_list = os.listdir(parentFolder + "/" + folder)
    for i in images_list:
        with open(parentFolder + "/" + folder + "/" + str(i), "rb") as image_file:
            b64 = base64.b64encode(image_file.read())
            body = {"path": "NFT/" + str(i), "content": str(b64, "utf-8")}
            final_array.append(body)

    header = {"X-API-Key": apiKey,
              "Content-Type": "application/json; charset=utf-8", "Host": "deep-index.moralis.io",
              "Content-Length": str(len(json.dumps(body)))}

    print("Uploading: " + str(len(images_list)) + " " + folder)
    response_data = requests.post(url=url, headers=header, data=json.dumps(final_array))
    print("Uploaded")
    base_url = "/".join(response_data.json()[0]["path"].split("/")[:-1])
    print("BASE URL of " + folder + ": " + base_url, end="\n*******************************\n")
    return base_url

def add_path_in_json():
    pass

upload("images")
upload("jsons")
