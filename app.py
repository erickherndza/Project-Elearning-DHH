from flask import Flask, render_template
from flask import Flask, render_template, url_for, request, redirect

from googleapiclient.discovery import build


# Function to get video based on user feedback
def get_video_based_on_feedback(feedback):
    query = feedback + ' tutorial'
    request = youtube.search().list(q=query, maxResults=1)
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    return video_id


app = Flask(__name__)

# Lista de lecciones (esto podría venir de una base de datos)
lecciones = [
    {'id': 1, 'titulo': 'Matemáticas Básicas'},
    {'id': 2, 'titulo': 'Ciencias Naturales'},
    # ...
]


@app.route('/')
def index():
    return render_template('index.html', lecciones=lecciones)


@app.route('/lesson/<int:leccion_id>')
@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form['feedback']
    video_id = get_video_based_on_feedback(user_feedback)
    # Now you can use this video_id to display the video on your platform
    return redirect(url_for('index'))


def lesson(leccion_id):
    leccion = next(
        (item for item in lecciones if item['id'] == leccion_id), None)
    if leccion is None:
        return "Lección no encontrada", 404
    return render_template('lesson.html', leccion=leccion)


# Initialize YouTube API
youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')


@app.route('/get_video', methods=['GET'])
def get_video():
    request = youtube.search().list(q='tutorial de matemáticas', maxResults=1)
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    return video_id


if __name__ == '__main__':
    app.run(debug=True)
