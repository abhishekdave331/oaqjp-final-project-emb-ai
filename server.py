from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detect():
    if request.method == "POST":
        text_to_analyze = request.form['textToAnalyze']
    else:
        text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Please enter valid text to analyze."

    response = emotion_detector(text_to_analyze)

    if not response:
        return "Invalid input or model error."

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
