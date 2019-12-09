import flask

from blueprints.docker_blueprint import docker_routes
from blueprints.jenkins_blueprint import jenkins_routes
from blueprints.ldap_blueprint import ldap_routes

#Controle de aplicação principal
app = flask.Flask(__name__)
app.secret_key = 'chave'

#Registro de rotas
app.register_blueprint(docker_routes)
app.register_blueprint(jenkins_routes)
app.register_blueprint(ldap_routes)

@app.route('/')
def index():
    if flask.session['logged']:
        pass
    else:
        flask.session['logged'] = False
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    return flask.render_template('index.jinja')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)