from flask import Flask, request

app = Flask(_name)  # Correto: __name_ com DOIS underscores

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        verify_token = "personalite123"
        if request.args.get("hub.verify_token") == verify_token:
            return request.args.get("hub.challenge")
        return "Token inválido", 403

    if request.method == 'POST':
        data = request.json
        print("Mensagem recebida:", data)
        return "OK", 200

if _name_ == "_main":  # Correto: __name_ com DOIS underscores
    app.run(host='0.0.0.0', port=5000)
