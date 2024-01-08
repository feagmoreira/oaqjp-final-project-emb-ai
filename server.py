from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    formatted_results = []
    for item in emotions:
        formatted_results.append("'{}': {}".format(item, emotions[item]))
    anger = formatted_results[0]
    disgust = formatted_results[1]
    fear = formatted_results[2]
    joy = formatted_results[3]
    sadness = formatted_results[4]
    dominant_emotion = emotions['dominant_emotion']
    return f"For the given statement, the system response is {anger}, {disgust}, {fear}, {joy} and {sadness}. \
     The dominant emotion is <b>{dominant_emotion}</b>."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)