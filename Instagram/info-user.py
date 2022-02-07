import requests,json,flask,secrets,re
from flask import jsonify
from flask import *

app = Flask(__name__)
@app.route("/")

def index():
    return "<h1>Api Alosh \n عذرا لايوجد يوزر</h1>"

@app.route('/Alosh/User/instagram/',methods=['GET'])
def Hhjjj():
    try:
        import secrets,re
        cookie = secrets.token_hex(8) * 2
        G = "@DtDtDt"
        g = {}
        User = request.args.get("User")
        url =(f"https://www.instagram.com/{User}/?__a=1")
        head = {'user-agent': 'Mozilla/5.0 (Windows NT 6.2; en-US; rv:1.9.0.20) Gecko/20170715 Firefox/37.0',
  'Cookie': cookie}
        req = requests.request("GET",url, headers = head,data=g).json()
        k =req['graphql']['user']['edge_follow']['count']
        id=req['graphql']['user']['id']
        name=req['graphql']['user']['full_name']
        followes = req['graphql']['user']['edge_followed_by']['count']
        alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        alsh1 = alsh.json()            
        data = alsh1['data']		            	
        AL = {
"Followes":followes,
"Following":k,
"Name":name,
"Id":id,
"Telegarm":G,
"Data":data
    }
        
        return jsonify(AL)
    except:
        status = False  
        User = "Not User"    
        data = 0
        id = 0
        k = 0
        followes =0
        name = 0
        
    
if __name__ == "__main__":
	app.run()    
           
                         
