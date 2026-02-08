from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    scores = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"anger': {scores['anger']}, disgust': {scores['disgust']}, fear': {scores['fear']}, joy': {scores['joy']}, "
        f"and 'sadness': {scores['sadness']}. The dominant emotion is <b>{scores['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
