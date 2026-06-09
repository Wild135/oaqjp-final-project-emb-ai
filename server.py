"""
Server module for the Emotion Detection web application.
Provides endpoints for rendering the interface and analyzing text inputs.
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_detector  # pylint: disable=import-error

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes incoming text arguments for emotional content.
    Returns a formatted string containing emotion scores or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the primary index HTML interface page for the user layout.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    