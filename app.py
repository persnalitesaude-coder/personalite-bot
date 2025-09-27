Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from flask import Flask, request
... 
... app = Flask(_name_)
... 
... @app.route('/webhook', methods=['GET', 'POST'])
... def webhook():
...     if request.method == 'GET':
...         verify_token = "personalite123"
...         if request.args.get("hub.verify_token") == verify_token:
...             return request.args.get("hub.challenge")
...         return "Token inválido", 403
... 
...     if request.method == 'POST':
...         data = request.json
...         print("Mensagem recebida:", data)
...         return "OK", 200
... 
... if _name_ == "_main_":
