from flask import Flask, send_file
import time

app = Flask(__name__)

# Endpoint to serve the video file
@app.route('/video/v1')
def stream_video():
    return send_file('video.mp4', mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
