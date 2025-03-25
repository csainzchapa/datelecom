from flask import Flask, request, jsonify
import random

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
        response_text = "Tenemos planes desde $199 al mes con equipo incluido. ¿Te gustaría conocerlos?",
                        "📱 Tenemos planes Telcel desde $199 al mes, con equipo incluido y redes sociales ilimitadas. ¿Tienes en mente algún modelo o te gustaría que te recomiende opciones económicas?",
                        "🎯 El plan más contratado es el de $299 MXN, con 4 GB de internet, redes ilimitadas y un equipo Motorola o Samsung incluido. ¿Te interesa saber qué modelos están disponibles?",
                        "🔍 Puedes consultar nuestro catálogo completo aquí: 👉 Ver equipos y planes Si me das tu presupuesto, puedo ayudarte a elegir la mejor opción.",
                        "¡Podemos ayudarte a contratar un plan Telcel con equipo nuevo desde hoy! Solo necesito saber: •	¿Qué equipo te interesa? •	¿Cuál es tu presupuesto mensual?",
                        "Todos nuestros planes incluyen llamadas ilimitadas y acceso a redes sociales como WhatsApp, Facebook, Twitter, Instagram y más. ¿Te gustaría conocer los planes con más datos?",
                        "📦 Contamos con una amplia gama de planes Telcel, desde los más básicos hasta los más completos. ¿Buscas un plan con más datos, redes sociales ilimitadas o un equipo en particular?",
                        "💰 Si buscas algo económico, tenemos planes desde $199 pesos al mes, con llamadas ilimitadas y acceso a WhatsApp, Facebook y más sin costo adicional.",
                        "📲 Si ya tienes un equipo en mente como iPhone, Samsung o Motorola, dime cuál es y te comparto las opciones que tenemos con ese modelo.",
                        "🎁 Este mes tenemos promociones en planes con equipo incluido y meses sin intereses. ¿Te gustaría que un asesor revise cuál es el mejor plan para ti?",
                        "🔁 ¿Te estás cambiando de otra compañía? Con portabilidad, puedes conservar tu número y aprovechar descuentos exclusivos al contratar un plan nuevo.",
                        "📶 ¿Buscas un plan con muchos datos? Tenemos opciones con 5, 10, hasta 20 GB mensuales, ideales para navegar, redes y ver videos sin preocuparte por tu saldo.",
                        "Si ya eres cliente Telcel, también podemos revisar si puedes renovar tu plan con un nuevo equipo. Solo necesito tu número para verificar tu estatus.",
                        "🗂 Si lo prefieres, te puedo enviar un catálogo con los planes y equipos más recientes. ¿Te lo mando por WhatsApp o prefieres el enlace aquí?",
                        "🧩 También contamos con planes sin equipo, ideales si ya tienes un celular. ¿Te gustaría conocer esas opciones más accesibles?",
                        "🧑💼 ¿Buscas líneas para tu empresa o varios empleados? Tenemos paquetes especiales para negocios con facturación y soporte personalizado."
        

    elif intent == "renovacion":
        renovacion_responses = [
            "🔄 Puedes renovar tu equipo si ya cumpliste 18 meses con tu plan actual.\n¿Te gustaría que revise tu número para verificar si ya eres elegible?",
            "🎉 Si ya puedes renovar, podrás elegir un nuevo equipo con precio preferencial y conservar tu número.\nTenemos opciones desde $0 pesos al contratar un plan.\n¿Qué marca o modelo te interesa?",
            "🎁 Este mes tenemos promociones especiales por renovación:\n• Equipos con hasta 50% de descuento\n• Meses sin intereses\n• Accesorios gratis en algunas líneas\n¿Quieres que te mande el catálogo actualizado?",
            "📞 Si prefieres, uno de nuestros asesores puede revisar tu estatus y mostrarte las mejores opciones disponibles.\n¿Nos compartes tu número Telcel y nombre completo?",
            "📦 También puedes renovar sin cambiar tu plan actual.\nSolo se requiere validarlo con tu número y una identificación oficial.\n¿Quieres hacerlo en línea o en tienda?",
            "📆 Si aún no cumples los 18 meses del contrato, puedes esperar unas semanas más o revisar las opciones de renovación anticipada.\n¿Te gustaría saber cuánto te falta o ver alternativas?",
            "🛍️ ¡Podemos ayudarte con tu renovación desde este mismo chat!\nSolo necesitamos tu número Telcel y una identificación.\n¿Listo para comenzar?"
        ]
        response_text = random.choice(renovacion_responses)

    elif intent == "facturacion_pagos":
        response_text = "Puedes pagar en línea, en OXXO o con transferencia. ¿Te envío el enlace de pago?",
                        "💳 Puedes realizar el pago de tu plan Telcel de varias formas: •	En línea desde Mi Telcel •	En tiendas OXXO, 7-Eleven, Chedraui, etc. •	Por transferencia bancaria. ¿Quieres que te envíe el link de pago?",
                        "✅ Aquí tienes el enlace para pagar tu plan en línea con tarjeta: https://www.mitelcel.com También puedes descargar la app Mi Telcel para Android o iOS.",
                        "📅 Tu fecha de corte es generalmente el día 15 de cada mes (puede variar según tu plan). ¿Te gustaría que revise tu número para confirmar?",
                        "🧾 Si necesitas factura electrónica, puedes obtenerla desde Mi Telcel o solicitárnosla aquí. Por favor, envíanos tu RFC y datos fiscales si deseas que te la generemos.",
                        "Si no te ha llegado la factura, puede deberse a: •	Problemas con el correo registrado •	Corte reciente sin generación aún •	Tu línea no tiene facturación activa ¿Te gustaría que un asesor revise tu caso?",
                        "Si realizaste tu pago recientemente, la confirmación puede tardar hasta 24 horas en reflejarse. Si ya pasaron más de 24h, por favor envíanos el comprobante para verificarlo.",
                        "💰 Puedes pagar tu plan Telcel en efectivo en: •	OXXO •	7-Eleven •	Farmacias Guadalajara •	Tiendas de autoservicio participantes Solo necesitas tu número Telcel para hacer el pago.",
                        "💳 Aceptamos pagos con tarjeta de crédito o débito desde la plataforma de Mi Telcel. ¿Quieres el link o prefieres pagar en tienda física?",
                        "📄 Puedes ver tu recibo en PDF ingresando a: https://www.mitelcel.com/recibo O desde la app Mi Telcel."


    elif intent == "soporte_tecnico":
        response_text = "📡 Si no tienes señal o red, por favor intenta lo siguiente:\n1. Apaga y enciende tu equipo\n2. Activa y desactiva el 'modo avión'\n3. Verifica que tu chip esté bien insertado\nSi el problema continúa, puedo canalizarte con soporte técnico.", \
                        '👀 A veces la red se puede ver afectada por saturación o mantenimiento en la zona.\n¿Podrías decirme tu colonia o ubicación aproximada para verificar?', \
                        '🧩 Si tu chip no funciona o no es detectado por el equipo, puede estar dañado.\nPodemos ayudarte con una reposición.\n¿Tienes tu número Telcel y una identificación oficial a la mano?', \
                        'Si cambiaste de equipo recientemente, asegúrate de que el teléfono sea libre o compatible con Telcel.\n¿Qué marca y modelo estás usando?', \
                        '⚠️ Si tu teléfono se reinicia solo, no prende o tiene fallas físicas, podemos ayudarte a validar si está en garantía.\n¿Lo compraste con nosotros? ¿Cuánto tiempo tiene?', \
                        '🚫 Si el equipo no responde o el touch está congelado, intenta reiniciarlo presionando el botón de encendido durante 10 segundos.\nSi no funciona, podemos orientarte con el centro de servicio más cercano.', \
                        '🔐 Lamentamos lo ocurrido. Podemos ayudarte a bloquear tu línea Telcel para evitar mal uso.\nSolo necesito confirmar tu número y algunos datos de seguridad.', \
                        '📋 Para recuperar tu línea después de robo o extravío, necesitas:\n• Tu número Telcel\n• Una identificación oficial\n• Solicitar reposición de SIM (te podemos decir dónde)',
                        '📞 Parece que tu caso necesita revisión más detallada.\n¿Quieres que te conecte con un asesor técnico ahora mismo?'"]

    elif intent == "portabilidad":
        portabilidad_responses = [
            "🔁 ¡Claro! Cambiarte a Telcel conservando tu número es muy fácil.\nSolo necesitas:\n1. Tu número actual (activo)\n2. Una identificación oficial\n3. El NIP de portabilidad (lo obtienes marcando *051 desde tu línea actual)\n¿Te gustaría iniciar el proceso ahora?",
            "✅ Para portarte a Telcel necesitas:\n• Tu número de otra compañía\n• Una identificación oficial vigente (INE, pasaporte, etc.)\n• El NIP de portabilidad (marca *051 desde tu línea actual)\nNosotros nos encargamos del resto. ¡Así de fácil!",
            "⏱ El proceso de portabilidad toma entre 24 y 48 horas una vez iniciado.\nMientras tanto, puedes seguir usando tu línea actual sin interrupciones.",
            "📱 Además, al portarte puedes aprovechar planes Telcel desde $199/mes con equipo incluido, redes sociales ilimitadas y muchas promos.\n¿Te interesa revisar las opciones?",
            "📞 Si lo prefieres, uno de nuestros asesores puede ayudarte paso a paso.\n¿Nos puedes compartir tu número para llamarte o enviarte la info por WhatsApp?",
            "🎁 Por hacer portabilidad con nosotros, puedes recibir:\n• Descuento en el primer mes\n• Bonos de bienvenida\n• Equipos con precio especial\n¿Te gustaría que revisemos tu caso?",
            "📩 No hay problema. Solo marca 📞 *051 desde tu número actual y recibirás tu NIP de portabilidad por SMS.\nCuando lo tengas, avísame y continuamos con el proceso."
        ]
        response_text = random.choice(portabilidad_responses)

    elif intent == "ubicacion_horario":
        ubicacion_responses = [
            "📍 Nuestra sucursal principal está ubicada en:\nAv. Sebastian Bach #5685 int 102, Colonia La Estancia, Zapopan, Jalisco.\nA una cuadra del Parque Metropolitano.",
            "🕒 Nuestro horario de atención es:\n• Lunes a viernes de 9:00 a.m. a 6:00 p.m.\n• Sábados de 10:00 a.m. a 2:00 p.m.\n• Domingos cerramos.",
            "🗺️ Aquí tienes la ubicación en Google Maps para que llegues fácilmente:\n🌐 Ver ubicación en Maps\n¿Te gustaría que te la mande también por WhatsApp?",
            "🔄 Tenemos atención en varias zonas de Guadalajara. ¿Nos puedes decir en qué colonia estás?\nAsí te indicamos la sucursal más cercana.",
            "📦 Si vienes a recoger un equipo o hacer renovación, por favor preséntate con una identificación oficial y tu número Telcel.\n¿Quieres que agendemos tu visita?",
            "🧠 También atendemos vía WhatsApp y este mismo chat si no puedes acudir presencialmente.\n¿Prefieres atención en línea o en tienda?"
        ]
        response_text = random.choice(ubicacion_responses)

    elif intent == "hablar_asesor":
        hablar_asesor_responses = [
            "👨💼 Claro, te pondré en contacto con uno de nuestros asesores.\nPor favor espera unos momentos mientras revisamos tu solicitud…",
            "Para darte una mejor atención, ¿puedes indicarme tu nombre y número Telcel?\nAsí un asesor podrá ayudarte directamente con tu caso.",
            "🚀 Canalizando tu caso al equipo de atención personalizada…\nSi hay alta demanda, puedes dejar tu mensaje aquí y te responderán a la brevedad.",
            "Nuestro equipo humano atiende de lunes a viernes de 9:00 a 18:00 h.\nPuedes dejar tu mensaje y te contactaremos en cuanto inicie la jornada.",
            "Entiendo que prefieres atención directa. Ya estoy avisando a un asesor para que continúe contigo.\n¡Gracias por tu paciencia! 🙏",
            "En este momento no hay un asesor disponible, pero puedes dejar tu nombre, número y el motivo, y te contactaremos en menos de 24 h.",
            "¿Prefieres continuar la atención por teléfono, WhatsApp o correo electrónico?\nIndícanos tu canal favorito y te contactamos."
        ]
        response_text = random.choice(hablar_asesor_responses)

    elif intent == "fallback":
        fallback_responses = [
            "😅 Perdón, no entendí lo que quisiste decir. ¿Podrías escribirlo de otra forma o elegir una de las opciones del menú?",
            "No estoy seguro de cómo ayudarte con eso.\nPuedes preguntarme sobre planes, pagos, renovación o soporte técnico. ¿En qué área necesitas ayuda?",
            "No entendí bien tu mensaje.\nPuedes escribir alguna de estas opciones para continuar:\n• Planes y equipos\n• Renovación\n• Facturación y pagos\n• Hablar con asesor",
            "Ups, creo que me distraje un momento 😅. ¿Podrías repetirlo o decirlo de otra forma?",
            "Si prefieres, puedo canalizarte con un asesor humano para que te atienda directamente. ¿Quieres que lo haga?",
            "Recuerda que puedo ayudarte con:\n• Información de planes Telcel\n• Renovación de equipo\n• Facturación y pagos\n• Portabilidad\n¿Cuál necesitas?",
            "Mmm... no entendí bien 🤔 ¿Puedes explicarme un poco mejor o elegir una opción como “renovación”, “factura” o “equipo nuevo”?"
        ]
        response_text = random.choice(fallback_responses)

    else:
        response_text = "Gracias por tu mensaje. ¿En qué más puedo ayudarte?"

    return jsonify({"fulfillmentText": response_text})

if __name__ == "__main__":
    app.run(debug=True)
