

from flask import Flask, jsonify, request
from flask_cors import CORS
from urllib.parse import urlparse, parse_qs
import json


app = Flask(__name__)
CORS(app)

@app.route("/captions", methods=["POST"])
def send_controls():

    video_id = request.json.get("video_id")

    parsed_url = urlparse(video_id)
    video_id = parse_qs(parsed_url.query)['v'][0]

    srt = YouTubeTranscriptApi.get_transcript(video_id)

    text = ""
    list = []
    count = 0
    for i in srt:
        text += i["text"] + " "
        if count == 100:
            list.append(text)
            text = ""
            count = 0
        count += 1
    list.append(text)

    return jsonify(list)

if __name__ == "__main__":
    app.run(port=5000)





