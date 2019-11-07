import requests

# reference: https://notify-bot.line.me/doc/en/

def Notify(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

if __name__=="__main__":
    # 欲傳送的訊息內容
    message = '測試一下！'
    # 您的權杖內容
    token = ''

    Notify(token, message)