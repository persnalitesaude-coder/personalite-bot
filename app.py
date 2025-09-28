# app.py
import os
import requests
from flask import Flask, request, Response

app = Flask(__name__)
app.url_map.strict_slashes = False

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "personalite123")
WA_TOKEN    = os.getenv("WHATSAPP_TOKEN")            # token PERMANENTE
WA_PHONE_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")  # ex.: "123456789012345"

@app.route("/", methods=["GET"])
def root():
    return "OK", 200

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == VERIFY_TOKEN and challenge:
            return Response(challenge, status=200, mimetype="text/plain")
        return Response("Token inválido", status=403)

    # POST (eventos do WhatsApp)
    data = request.get_json(silent=True) or {}
    print("Webhook event:", data)

    try:
        entry = (data.get("entry") or [])[0]
        change = (entry.get("changes") or [])[0]
        value = change.get("value") or {}
        messages = value.get("messages") or []
        if messages:
            msg = messages[0]
            from_wa = msg.get("from")  # E.164, ex: "55DDNNNNNNNN"
            text = None

            if msg.get("type") == "text":
                text = msg["text"]["body"]
            elif msg.get("type") == "interactive":
                i = msg.get("interactive") or {}
                if i.get("type") == "button_reply":
                    text = i["button_reply"]["title"]
                elif i.get("type") == "list_reply":
                    text = i["list_reply"]["title"]

            if from_wa and text:
                send_whatsapp_text(from_wa, f"Você disse: {text}")
    except Exception as e:
        print("Erro ao processar webhook:", e)

    return Response("OK", status=200)

def send_whatsapp_text(to: str, body: str):
    if not (WA_TOKEN and WA_PHONE_ID):
        print("Faltam WHATSAPP_TOKEN ou WHATSAPP_PHONE_NUMBER_ID")
        return
    url = f"https://graph.facebook.com/v20.0/{WA_PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WA_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": body}
    }
    r = requests.post(url, headers=headers, json=payload, timeout=10)
    print("Resposta do envio:", r.status_code, r.text)