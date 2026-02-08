"""
This module provides a function for emotion detection
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyze the emotion of the provided text from the query string.

    Query parameter:
    - textToAnalyze: str -- text to analyze for emotions

    Returns:
    - str: HTML describing emotion scores and the dominant emotion,
           or an error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    scores = emotion_detector(text_to_analyze)

    if scores['dominant_emotion'] is None:
        return "<b>Invalid input! Try again.</b>"
    return (
        f"For the given statement, the system response is "
         f"'anger': {scores['anger']}, 'disgust': {scores['disgust']}, "
        f"'fear': {scores['fear']}, 'joy': {scores['joy']}, and "
        f"'sadness': {scores['sadness']}. "
        f"The dominant emotion is <b>{scores['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
    - Response: rendered index.html template
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
