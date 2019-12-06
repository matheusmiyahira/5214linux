import flask
import random

random_blueprint = flask.Blueprint('random',__name__,url_prefix='/random')

@random_blueprint.route('/')
def index():
    return str(random.randint(1,100))