import base64
import json
import os
import requests

if not os.path.exists("images"):
    print("images folder does not exits, please make a folder 'images' and paste all images in that folder")
    exit()

url = "https://deep-index.moralis.io/api/v2/ipfs/uploadFolder"
finalArray = []
print("Processing")
for i in os.listdir("images"):
    with open("images/" + str(i), "rb") as image_file:
        b64 = base64.b64encode(image_file.read())
        body = {"path": "NFT/" + str(i), "content": str(b64, "utf-8")}
        finalArray.append(body)

header = {"X-API-Key": "hfIwtLH5S62AGzhPrUMWn6tVddAohLT0nIsCMkdilQYd6DROJfL6k0sdYSFxn3z3",
                  "Content-Type": "application/json; charset=utf-8", "Host": "deep-index.moralis.io",
                  "Content-Length": str(len(json.dumps(body)))}
print("Uploading: "+ str(len(os.listdir("images")))+ " images")
responseData = requests.post(url=url, headers=header, data=json.dumps(finalArray))
print("Uploaded")
print("BASE URL:"+"/".join(responseData.json()[0]["path"].split("/")[:-1]))