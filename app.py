from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot Flask Backend Activo 🚀"

@app.route('/dialogflow_webhook', methods=['POST'])
def dialogflow_webhook():
    req = request.get_json()
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    if intent == "saludo" or intent == "Default Welcome Intent":
        response_text = "¡Hola! 👋 Soy tu asistente Datbot. ¿En qué puedo ayudarte hoy?"
    elif intent == "planes_equipos":
        response_text = "Tenemos planes desde $199 al mes con equipo incluido. ¿Te gustaría conocerlos?"
    elif intent == "renovacion":
        response_text = "Puedes renovar tu equipo si ya cumpliste 18 meses de contrato. ¿Quieres revisar si ya puedes hacerlo?"
    elif intent == "facturacion_pagos":
        response_text = "Puedes pagar en línea, en OXXO o con transferencia. ¿Te envío el enlace de pago?"
    elif intent == "soporte_tecnico":
        response_text = "Por favor intenta reiniciar tu equipo. Si el problema continúa, te canalizo con soporte técnico."
    elif intent == "portabilidad":
        response_text = (
            "Puedes cambiarte a Telcel conservando tu número. Solo necesitas tu número actual, una identificación oficial "
            "y el NIP que obtienes marcando *051 desde tu línea. ¿Quieres iniciar el proceso?"
        )
    elif intent == "ubicacion_horario":
        response_text = (
            "📍 Estamos en Av. Patria #456, Zapopan, Jalisco. Horario: L-V 9am a 6pm, Sáb 10am a 2pm. "
            "¿Te gustaría que te mande la ubicación por WhatsApp?"
        )
    elif intent == "hablar_asesor":
        response_text = "Con gusto, te conectaré con un asesor humano. Por favor espera un momento…"
    elif intent == "fallback":
        response_text = (
            "No entendí tu mensaje. ¿Podrías repetirlo o elegir una opción como: renovación, pago, portabilidad o hablar con asesor?"
        )
    else:
        response_text = "Gracias por tu mensaje. ¿En qué más puedo ayudarte?"

    return jsonify({"fulfillmentText": response_text})

if __name__ == "__main__":
    app.run(debug=True)
