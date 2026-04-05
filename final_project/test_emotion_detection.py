import unittest
import json
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # 1. Prueba para Alegría
        # Usamos json.loads() para convertir el texto en un diccionario real
        result_1 = json.loads(emotion_detector("I am glad this happened"))
        # Verificamos que la respuesta contenga datos (no sea nula)
        self.assertIsNotNone(result_1)

        # 2. Prueba para Ira
        result_2 = json.loads(emotion_detector("I am really mad about this"))
        self.assertIsNotNone(result_2)

        # 3. Prueba para Disgusto
        result_3 = json.loads(emotion_detector("I am feel disgusted just hearing about this"))
        self.assertIsNotNone(result_3)

        # 4. Prueba para Tristeza
        result_4 = json.loads(emotion_detector("I am so sad about this"))
        self.assertIsNotNone(result_4)

        # 5. Prueba para Miedo
        result_5 = json.loads(emotion_detector("I am really afraid that this will happen"))
        self.assertIsNotNone(result_5)

if __name__ == "__main__":
    unittest.main()