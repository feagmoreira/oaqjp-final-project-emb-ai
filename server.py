''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''
    Function used to obtain results from IBM Watson 
    emotion detection functionality from a text passed
    as query argument in the HTTP request.

    Route: /emotionDetector

    Returns
    Error message if no text is passed as argument

    OR

    Following message:

    For the given statement, the system response is {anger}, {disgust}, \
        {fear}, {joy} and {sadness}. \
        The dominant emotion is <b>{dominant_emotion}</b>.
    
    Where the values in the {} represent Emotion : score returned from Watson.
    Dominant emotion is the name of the emotion with the biggest score

    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    formatted_results = []
    for emotion,score in emotions.items():
        formatted_results.append(f"'{emotion}': {score}")
    anger = formatted_results[0]
    disgust = formatted_results[1]
    fear = formatted_results[2]
    joy = formatted_results[3]
    sadness = formatted_results[4]
    dominant_emotion = emotions['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is {anger}, {disgust}, \
        {fear}, {joy} and {sadness}. \
        The dominant emotion is <b>{dominant_emotion}</b>."

@app.route("/")
def render_index_page():
    '''
        Function used by Flask to render initial page (index.html)
        of the Emotion Detection page

        Route: /

    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
