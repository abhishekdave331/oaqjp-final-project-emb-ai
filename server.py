"""
Flask server for Emotion Detection Web Application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the homepage of the application.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detect():
    """
    Receive text from user input, run emotion detection,
    and return a formatted response or an error prompt.
    """

    text_to_analyze = (
        request.form.get("textToAnalyze", "")
        if request.method == "POST"
        else request.args.get("textToAnalyze", "")
    )

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    final_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return final_response


if __name__ == "__main__":
    app.run(debug=True)
