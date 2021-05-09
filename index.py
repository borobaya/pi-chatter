from flask import Flask, render_template, request
from aiy.voice import tts

app = Flask(__name__)

@app.route('/')
def index():
    text_to_say = request.args.get('say')
    if text_to_say:
        tts.say(text_to_say)
    return render_template('index.html', say=text_to_say)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
