from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detect():
    # Get text from form
    text_to_analyze = request.form['textToAnalyze']

    # Run through our package
    response = emotion_detector(text_to_analyze)

    # If the API returns None or fails
    if response is None or response == {}:
        return "Invalid text! Please try again."

    # Format response for output
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
