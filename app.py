from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_transcript_text(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        combined_text = " ".join([item['text'] for item in transcript])
        return combined_text
    except Exception as e:
        return str(e)

@app.route('/api/transcript', methods=['GET'])
def transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({'error': 'Missing video_id parameter'}), 400
    combined_text = get_transcript_text(video_id)
    return jsonify({'transcript': combined_text})

@app.route('/')
def home():
    return "YouTube Transcript API is running!"

if __name__ == "__main__":
    app.run(debug=True)