from flask import *
import requests
from user_agent import generate_user_agent

app = Flask(__name__)

@app.route('/',methods=['GET'])
def login():

    username = str(request.args.get('username'))

    password = str(request.args.get('password'))

    url = 'https://www.instagram.com/accounts/login/ajax/'

    head = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate,br",
        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
        "content-length": "416",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-site": "same-origin",
        "user-agent": generate_user_agent(),
        "x-csrftoken": "iPbbQelxf2U4m4YMkwIEhnB0DlMAOn17",
        "x-ig-app-id": "1217981644879628",
        "x-instagram-ajax": "038693313a95",
        "x-requested-with": "XMLHttpRequest"
    }

    data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1642498262:'+password,
        'username': username,
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'stopDeletionNonce': '',
        'trustedDeviceRecords': '{}',
    }

    response = requests.post(url, headers=head, data=data)
    if '"authenticated":false,' in response.text:
        return {
            'Username': username,
            'Password': password,
            'Status': 'Faild',
            'By': '@zzaaz',
        }
    elif '"authenticated":True,' in response.text:
        return {
            'Username': username,
            'Password': password,
            'Status': 'Ok',
            'By': '@zzaaz',
        }
    elif 'checkpoint_required' in response.text:
        return {
            'Username': username,
            'Password': password,
            'Status': 'Checkpoint',
            'By': '@zzaaz',
        }
    else:
        return {
            'Username': username,
            'Password': password,
            'Status': 'Wait...',
            'By': '@zzaaz',
        }



if __name__ == "__main__":
    app.run()
