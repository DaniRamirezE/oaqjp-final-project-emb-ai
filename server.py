from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Si la respuesta ya es un diccionario (caso de error 400)
    if isinstance(response, dict):
        full_response = response
    else:
        full_response = json.loads(response)
        # Extraer emociones del formato de Watson
        emotions = full_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        full_response = {**emotions, 'dominant_emotion': dominant_emotion}

    # Lógica de manejo de errores solicitada
    if full_response['dominant_emotion'] is None:
        return "¡Texto no válido! ¡Por favor inténtalo de nuevo!"

    # Respuesta normal
    return (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'ira': {full_response['anger']}, 'disgusto': {full_response['disgust']}, "
        f"'miedo': {full_response['fear']}, 'alegría': {full_response['joy']} y "
        f"'tristeza': {full_response['sadness']}. "
        f"La emoción dominante es {full_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)