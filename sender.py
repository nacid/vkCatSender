#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import requests
import time
import json
import vk
from PIL import Image
from io import BytesIO

if __name__ == "__main__":
    if len(sys.argv) == 4:
        token = sys.argv[1]
        storage = sys.argv[2]
        receiver_id = sys.argv[3]
    else:
        exit('Incorrect Number of Arguments. Use "' + sys.argv[0] + ' <vk_access_token> <images_save_directory> <receiver_vk_id>"')

response = requests.get('http://thecatapi.com/api/images/get?format=src')
img = Image.open(BytesIO(response.content))

session = vk.Session(token)
api = vk.API(session)

upload_url = api.photos.getMessagesUploadServer()['upload_url']
upload_name = str(int(time.time())) + '.' + img.format
img.save(storage + upload_name)

pack = {'photo': (upload_name, open(storage + upload_name, 'rb'))}
upload_raw_result = requests.post(upload_url, files=pack)
upload_result = json.loads(upload_raw_result.text)
save_result = api.photos.saveMessagesPhoto(photo=upload_result['photo'], server=upload_result['server'], hash=upload_result['hash'])
send_result = api.messages.send(user_id=receiver_id, message=upload_name, attachment=save_result[0]['id'])

print(upload_name + ' complete ' + str(send_result))
