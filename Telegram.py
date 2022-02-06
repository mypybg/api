import requests, re
from flask import Flask , request ,jsonify
app=Flask(__name__)
@app.route("/")
		
def check():
	user = request.args.get("user")
	r = requests.get(f"https://t.me/{user}").text
	
	find = re.findall('<div class="tgme_page_title"><span dir="auto">(.*?)</span></div>', r)
	
	try:
		if find[0] != None:
			ok = jsonify(ok=False, status="UnAvailable", user=user)
	except:
			ok = jsonify(ok= True,status="Available",user=user)
			
	return ok			
app.run()
