import requests
import os
import random
import string
import json


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "scammers url"

names = json.loads(open('1000_boy_names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects=False, data={
        'website username key from network tab': username,
        'website password key from network tab': password
    })

    print('sending username %s and password %s' % (username, password))