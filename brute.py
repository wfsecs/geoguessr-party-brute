import threading
import requests
import random
import string
import time
import json

# Variables
chars = string.ascii_uppercase + string.digits
api_url = 'https://www.geoguessr.com/api/v3/join-codes/'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
headers = {'User-agent': ua}


def check(code):
    r = requests.get(api_url + code + '?s=Manual', headers=headers).json()
    try:
        code = r['code']
        expires = r['expires']
        print(f'\nExpires: {expires}\nCode: {code}')
    except:
        return


while True:
    rcode = ''.join(random.choices(chars, k=4))
    has_numbers = any(char.isdigit() for char in rcode)
    if has_numbers:
        thread = threading.Thread(target=check, args=(rcode,), daemon=True)
        time.sleep(0.1)
        thread.start()
