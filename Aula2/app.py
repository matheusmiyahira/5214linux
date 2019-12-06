# #!/usr/bin/env python3

# import flask

# app = flask.Flask(__name__)

# dados = {
#     'acesso':'Ok'
# }
# #Configurando rotas
# @app.route('/')
# def index():
#     return flask.jsonify(dados)

# #Configurando tipo de requisição
# @app.route("/api?<any('id','nome'):string>=<int:id>,methods=['POST'])
# def index_get_id(id):
#     dados = {'nome':f'nome do id: {id}'}
#     return flask.jsonify(dados)

# @app.route('/teste/teste')
# def teste_teste():
#     return 'Teste_teste'

# app.run(host='0.0.0.0',debug=True,port=80)