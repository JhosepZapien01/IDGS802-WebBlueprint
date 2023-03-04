import flask 
from Alumnos.routes import alumno
from Directivos.routes import dir
from Maestros.routes import maestros


app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route("/",methods=['GET'])
def home():
    return flask.jsonify({'principal':'Home'})

app.register_blueprint(alumno)
app.register_blueprint(dir)
app.register_blueprint(maestros)
if __name__ == '__main__':
    app.run()