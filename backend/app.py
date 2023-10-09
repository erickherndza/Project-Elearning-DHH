from googleapiclient.discovery import build
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from backend.models import db
from backend.lesson_routes import lesson_bp
from backend.user_routes import user_bp

app.config.from_pyfile('config.py')


# Inicialización
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
login_manager = LoginManager()
login_manager.init_app(app)

# Modelo de usuario (esto debería estar en una base de datos)

# Inicializar la base de datos
db.init_app(app)

# Registrar los blueprints
app.register_blueprint(lesson_bp, url_prefix='/lessons')
app.register_blueprint(user_bp, url_prefix='/users')


class User(UserMixin):
    def __init__(self, id):
        self.id = id


if __name__ == '__main__':
    app.run(debug=True)

# Lista de lecciones (esto debería venir de una base de datos)
lecciones = [
    {'id': 1, 'titulo': 'Matemáticas Básicas'},
    {'id': 2, 'titulo': 'Ciencias Naturales'},
    # ...
]


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/')
def index():
    return render_template('index.html', lecciones=lecciones)


@app.route('/lesson/<int:leccion_id>')
@login_required
def lesson(leccion_id):
    leccion = next(
        (item for item in lecciones if item['id'] == leccion_id), None)
    if leccion is None:
        return "Lección no encontrada", 404
    return render_template('lesson.html', leccion=leccion)


@app.route('/update_points', methods=['POST'])
@login_required
def update_points():
    # Lógica para actualizar puntos
    return "Puntos actualizados"


@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form['feedback']
    # Procesar la retroalimentación aquí
    return redirect(url_for('index'))


youtube = build('youtube', 'v3', developerKey='TU_API_KEY')
request = youtube.search().list(q='tutorial de matemáticas', maxResults=1)
response = request.execute()
video_id = response['items'][0]['id']['videoId']


if __name__ == '__main__':
    app.run(debug=True)
