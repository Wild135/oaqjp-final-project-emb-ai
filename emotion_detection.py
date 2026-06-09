import requests
import json

def emotion_detector(text_to_analyze):
    """
    Runs emotion detection on the provided text and returns the response text.
    """
    # Replace this URL with the actual endpoint of your Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Replace this header with the specific headers required by your API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Constructing the payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending the POST request to the Emotion Detection service
    response = requests.post(url, json=myobj, headers=headers)
    
    # 1. Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # 2. Extract the emotions block from the nested dictionary structure
    # Note: This path mirrors the standard IBM Watson NLP emotion prediction output structure
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # 3. Extract individual emotion scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 4. Define a localized dictionary of the target emotions to find the highest score
    target_emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # 5. Find the dominant emotion (the key with the maximum value)
    dominant_emotion = max(target_emotions, key=target_emotions.get)
    
    # 6. Format the final output dictionary
    output_format = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output_format