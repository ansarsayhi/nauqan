import requests
import os

bot_token = '7782201874:AAGLP2NEYzr-DEwRQBY8Oqb7B6Pr6BS5aW8E'
channel_id = '-1002200553688' 



folder_path = 'nauqas1/screens'


for filename in os.listdir(folder_path):
    image_path = os.path.join(folder_path, filename)
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    with open(image_path, 'rb') as image_file:
        data = {
            'chat_id': channel_id,
        }
        files = {
            'photo': image_file
        }



