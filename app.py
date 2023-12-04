from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

ALLOWED_EXTENSION= ['mp4']

def allowed_file(filename) :
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION

@app.route('/upload', methods=["POST"])

def upload():
    video = request.files['video']
    if 'video' not in request.files:
        return "NO video is found"
    if video.filename == "":
        return "No video file selected"
    if video and allowed_file(video.filename):
        video.save('static/videos/' + video.filename)
        return render_template('Result.html',video = video.filename)
    return "invalid formate"



if __name__ == "__main__":
    app.run(debug=True)