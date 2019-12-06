import flask

from blueprints.docker_blueprint import docker_routes
from blueprints.jenkins_blueprint import jenkins_routes

#Controle de aplicação principal
app = flask.Flask(__name__)

#Registro de rotas
app.register_blueprint(docker_routes)
app.register_blueprint(jenkins_routes)

@app.route('/')
def index():
    return flask.render_template('index.jinja')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)