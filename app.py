# create a hello world app with flask

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/json')
def json():
    return {'hello': 'world'}

@app.route('/image')
def image():
    return send_file(
        'static/image.jpg',
        mimetype='image/jpeg'
        )

@app.route('/video')
def video():
    return send_file(
        'static/video.mp4',
        mimetype='video/mp4'
        )

@app.route('/html')
def html():
    return render_template('index.html')
