import requests
import json
def emotion_detector(text_to_analyze):
    # URL for Emotion Predict function
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    # Headers (model info)
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    # The payload with text
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    # Send POST request
    response = requests.post(url, headers=headers, json=payload)
    # Return only the 'text' attribute from the response JSON
    return response.text
