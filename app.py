from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot Flask Backend Activo 🚀"

@app.route('/dialogflow_webhook', methods=['POST'])
def dialogflow_webhook():
    req = request.get_json()
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName", "")
    
    if intent == "planes_equipos":
        response_text = "Tenemos planes desde $199 al mes con equipo incluido. ¿Te gustaría conocerlos?"
    elif intent == "renovacion":
        response_text = "Puedes renovar tu equipo si ya cumpliste 18 meses de contrato. ¿Quieres revisar si ya puedes hacerlo?"
    elif intent == "facturacion_pagos":
        response_text = "Puedes pagar en línea, en OXXO o con transferencia. ¿Te envío el enlace de pago?"
    elif intent == "soporte_tecnico":
        response_text = "Por favor intenta reiniciar tu equipo. Si el problema continúa, te canalizo con soporte técnico."
    elif intent == "fallback":
        response_text = "No entendí tu mensaje. ¿Podrías repetirlo o elegir una opción del menú?"
    else:
        response_text = "Gracias por tu mensaje. ¿En qué más puedo ayudarte?"

    return jsonify({"fulfillmentText": response_text})
