import requests  # Este es el "mensajero" que enviará tu solicitud
import json      # Para organizar la respuesta que recibamos

def emotion_detector(text_to_analyze):
    # 1. La URL que te proporcionaron
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # 2. Los Headers (Cabeceras) que te piden
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # 3. El Formato JSON de entrada (donde ponemos tu variable de texto)
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # 4. Enviamos la solicitud POST
    # Usamos requests.post y le pasamos la URL, el JSON y los Headers
    response = requests.post(url, json=myobj, headers=header)
    
    # 5. Retornamos el texto de la respuesta que nos da Watson
    return response.text

# --- PARTE PARA PROBARLO Y GENERAR LA SALIDA DEL TERMINAL ---
if __name__ == "__main__":
    print(emotion_detector("Estoy muy feliz de estar haciendo esto."))