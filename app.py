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
        response_text = "¡Hola! 👋 Soy tu asistente Telcel. ¿En qué puedo ayudarte hoy?"

    elif intent == "planes_equipos":
        responses = [
            "📱 Tenemos planes Telcel desde $199 al mes, con equipo incluido y redes sociales ilimitadas. ¿Tienes en mente algún modelo o te gustaría que te recomiende opciones económicas?",
            "🎯 El plan más contratado es el de $299 MXN, con 4 GB de internet, redes ilimitadas y un equipo Motorola o Samsung incluido. ¿Te interesa saber qué modelos están disponibles?",
            "🔍 Puedes consultar nuestro catálogo completo aquí: 👉 Ver equipos y planes. Si me das tu presupuesto, puedo ayudarte a elegir la mejor opción.",
            "¡Podemos ayudarte a contratar un plan Telcel con equipo nuevo desde hoy! Solo necesito saber: ¿Qué equipo te interesa? ¿Cuál es tu presupuesto mensual?",
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
        ]
        response_text = random.choice(responses)

    elif intent == "renovacion":
        responses = [
            "🔄 Puedes renovar tu equipo si ya cumpliste 18 meses con tu plan actual. ¿Te gustaría que revise tu número para verificar si ya eres elegible?",
            "🎉 Si ya puedes renovar, podrás elegir un nuevo equipo con precio preferencial y conservar tu número. Tenemos opciones desde $0 pesos al contratar un plan. ¿Qué marca o modelo te interesa?",
            "🎁 Este mes tenemos promociones especiales por renovación: • Equipos con hasta 50% de descuento • Meses sin intereses • Accesorios gratis en algunas líneas. ¿Quieres que te mande el catálogo actualizado?",
            "📞 Si prefieres, uno de nuestros asesores puede revisar tu estatus y mostrarte las mejores opciones disponibles. ¿Nos compartes tu número Telcel y nombre completo?",
            "📦 También puedes renovar sin cambiar tu plan actual. Solo se requiere validarlo con tu número y una identificación oficial. ¿Quieres hacerlo en línea o en tienda?",
            "📆 Si aún no cumples los 18 meses del contrato, puedes esperar unas semanas más o revisar las opciones de renovación anticipada. ¿Te gustaría saber cuánto te falta o ver alternativas?",
            "🛍️ ¡Podemos ayudarte con tu renovación desde este mismo chat! Solo necesitamos tu número Telcel y una identificación. ¿Listo para comenzar?"
        ]
        response_text = random.choice(responses)

    elif intent == "facturacion_pagos":
        responses = [
            "💳 Puedes realizar el pago de tu plan Telcel de varias formas: • En línea desde Mi Telcel • En tiendas OXXO, 7-Eleven, Chedraui, etc. • Por transferencia bancaria. ¿Quieres que te envíe el link de pago?",
            "✅ Aquí tienes el enlace para pagar tu plan en línea con tarjeta: https://www.mitelcel.com. También puedes descargar la app Mi Telcel para Android o iOS.",
            "📅 Tu fecha de corte es generalmente el día 15 de cada mes (puede variar según tu plan). ¿Te gustaría que revise tu número para confirmar?",
            "🧾 Si necesitas factura electrónica, puedes obtenerla desde Mi Telcel o solicitárnosla aquí. Por favor, envíanos tu RFC y datos fiscales si deseas que te la generemos.",
            "Si no te ha llegado la factura, puede deberse a: • Problemas con el correo registrado • Corte reciente sin generación aún • Tu línea no tiene facturación activa. ¿Te gustaría que un asesor revise tu caso?",
            "Si realizaste tu pago recientemente, la confirmación puede tardar hasta 24 horas en reflejarse. Si ya pasaron más de 24h, por favor envíanos el comprobante para verificarlo.",
            "💰 Puedes pagar tu plan Telcel en efectivo en: • OXXO • 7-Eleven • Farmacias Guadalajara • Tiendas de autoservicio participantes. Solo necesitas tu número Telcel para hacer el pago.",
            "💳 Aceptamos pagos con tarjeta de crédito o débito desde la plataforma de Mi Telcel. ¿Quieres el link o prefieres pagar en tienda física?",
            "📄 Puedes ver tu recibo en PDF ingresando a: https://www.mitelcel.com/recibo. O desde la app Mi Telcel."
        ]
        response_text = random.choice(responses)

    elif intent == "soporte_tecnico":
        responses = [
            "📡 Si no tienes señal o red, por favor intenta lo siguiente: 1. Apaga y enciende tu equipo 2. Activa y desactiva el 'modo avión' 3. Verifica que tu chip esté bien insertado. Si el problema continúa, puedo canalizarte con soporte técnico.",
            "👀 A veces la red se puede ver afectada por saturación o mantenimiento en la zona. ¿Podrías decirme tu colonia o ubicación aproximada para verificar?",
            "🧩 Si tu chip no funciona o no es detectado por el equipo, puede estar dañado. Podemos ayudarte con una reposición. ¿Tienes tu número Telcel y una identificación oficial a la mano?",
            "Si cambiaste de equipo recientemente, asegúrate de que el teléfono sea libre o compatible con Telcel. ¿Qué marca y modelo estás usando?",
            "⚠️ Si tu teléfono se reinicia solo, no prende o tiene fallas físicas, podemos ayudarte a validar si está en garantía. ¿Lo compraste con nosotros? ¿Cuánto tiempo tiene?",
            "🚫 Si el equipo no responde o el touch está congelado, intenta reiniciarlo presionando el botón de encendido durante 10 segundos. Si no funciona, podemos orientarte con el centro de servicio más cercano.",
            "🔐 Lamentamos lo ocurrido. Podemos ayudarte a bloquear tu línea Telcel para evitar mal uso. Solo necesito confirmar tu número y algunos datos de seguridad.",
            "📋 Para recuperar tu línea después de robo o extravío, necesitas: • Tu número Telcel • Una identificación oficial • Solicitar reposición de SIM (te podemos decir dónde)",
            "📞 Parece que tu caso necesita revisión más detallada. ¿Quieres que te conecte con un asesor técnico ahora mismo?"
        ]
        response_text = random.choice(responses)

    elif intent == "portabilidad":
        responses = [
            "🔁 ¡Claro! Cambiarte a Telcel conservando tu número es muy fácil. Solo necesitas: 1. Tu número actual (activo) 2. Una identificación oficial 3. El NIP de portabilidad (lo obtienes marcando *051 desde tu línea actual). ¿Te gustaría iniciar el proceso ahora?",
            "✅ Para portarte a Telcel necesitas: • Tu número de otra compañía • Una identificación oficial vigente (INE, pasaporte, etc.) • El NIP de portabilidad (marca *051 desde tu línea actual). Nosotros nos encargamos del resto. ¡Así de fácil!",
            "⏱ El proceso de portabilidad toma entre 24 y 48 horas una vez iniciado. Mientras tanto, puedes seguir usando tu línea actual sin interrupciones.",
            "📱 Además, al portarte puedes aprovechar planes Telcel desde $199/mes con equipo incluido, redes sociales ilimitadas y muchas promos. ¿Te interesa revisar las opciones?",
            "📞 Si lo prefieres, uno de nuestros asesores puede ayudarte paso a paso. ¿Nos puedes compartir tu número para llamarte o enviarte la info por WhatsApp?",
            "🎁 Por hacer portabilidad con nosotros, puedes recibir: • Descuento en el primer mes • Bonos de bienvenida • Equipos con precio especial. ¿Te gustaría que revisemos tu caso?",
            "📩 No hay problema. Solo marca 📞 *051 desde tu número actual y recibirás tu NIP de portabilidad por SMS. Cuando lo tengas, avísame y continuamos con el proceso."
        ]
        response_text = random.choice(responses)

    elif intent == "ubicacion_horario":
        responses = [
            "📍 Nuestra sucursal principal está ubicada en: Av. Sebastian Bach #5685 int 102, Colonia La Estancia, Zapopan, Jalisco. A una cuadra del Parque Metropolitano.",
            "🕒 Nuestro horario de atención es: • Lunes a viernes de 9:00 a.m. a 6:00 p.m. • Sábados de 10:00 a.m. a 2:00 p.m. • Domingos cerramos.",
            "🗺️ Aquí tienes la ubicación en Google Maps para que llegues fácilmente: 🌐 Ver ubicación en Maps. ¿Te gustaría que te la mande también por WhatsApp?",
            "🔄 Tenemos atención en varias zonas de Guadalajara. ¿Nos puedes decir en qué colonia estás? Así te indicamos la sucursal más cercana.",
            "📦 Si vienes a recoger un equipo o hacer renovación, por favor preséntate con una identificación oficial y tu número Telcel. ¿Quieres que agendemos tu visita?",
            "🧠 También atendemos vía WhatsApp y este mismo chat si no puedes acudir presencialmente. ¿Prefieres atención en línea o en tienda?"
        ]
        response_text = random.choice(responses)

    elif intent == "hablar_asesor":
        responses = [
            "👨💼 Claro, te pondré en contacto con uno de nuestros asesores. Por favor espera unos momentos mientras revisamos tu solicitud…",
            "Para darte una mejor atención, ¿puedes indicarme tu nombre y número Telcel? Así un asesor podrá ayudarte directamente con tu caso.",
            "🚀 Canalizando tu caso al equipo de atención personalizada… Si hay alta demanda, puedes dejar tu mensaje aquí y te responderán a la brevedad.",
            "Nuestro equipo humano atiende de lunes a viernes de 9:00 a 18:00 h. Puedes dejar tu mensaje y te contactaremos en cuanto inicie la jornada.",
            "Entiendo que prefieres atención directa. Ya estoy avisando a un asesor para que continúe contigo. ¡Gracias por tu paciencia! 🙏",
            "En este momento no hay un asesor disponible, pero puedes dejar tu nombre, número y el motivo, y te contactaremos en menos de 24 h.",
            "¿Prefieres continuar la atención por teléfono, WhatsApp o correo electrónico? Indícanos tu canal favorito y te contactamos."
        ]
        response_text = random.choice(responses)

    elif intent == "fallback":
        responses = [
            "😅 Perdón, no entendí lo que quisiste decir. ¿Podrías escribirlo de otra forma o elegir una de las opciones del menú?",
            "No estoy seguro de cómo ayudarte con eso. Puedes preguntarme sobre planes, pagos, renovación o soporte técnico. ¿En qué área necesitas ayuda?",
            "No entendí bien tu mensaje. Puedes escribir alguna de estas opciones para continuar: • Planes y equipos • Renovación • Facturación y pagos • Hablar con asesor",
            "Ups, creo que me distraje un momento 😅. ¿Podrías repetirlo o decirlo de otra forma?",
            "Si prefieres, puedo canalizarte con un asesor humano para que te atienda directamente. ¿Quieres que lo haga?",
            "Recuerda que puedo ayudarte con: • Información de planes Telcel • Renovación de equipo • Facturación y pagos • Portabilidad ¿Cuál necesitas?",
            "Mmm... no entendí bien 🤔 ¿Puedes explicarme un poco mejor o elegir una opción como “renovación”, “factura” o “equipo nuevo”?"
        ]
        response_text = random.choice(responses)

    else:
        response_text = "Gracias por tu mensaje. ¿En qué más puedo ayudarte?"

    return jsonify({"fulfillmentText": response_text})

if __name__ == "__main__":
    app.run(debug=True)
