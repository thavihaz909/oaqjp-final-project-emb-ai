import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = myobj, headers=header)  

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        scores = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = scores['anger']
        disgust_score = scores['disgust']
        fear_score = scores['fear']
        joy_score = scores['joy']
        sadness_score = scores['sadness']

        dominant_emotion = ''
        highest_score = 0
        for index, (key, value) in enumerate(scores.items()):
            if value > highest_score:
                highest_score = value
                dominant_emotion = key

    elif response.status_code == 400:            
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}    