import jwt
import datetime
from flask import Flask, jsonify, request, render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

SECRET_KEY = "mysecretkey"

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()


# Função para gerar um token JWT para o usuário
def gerar_token(usuario_id):
    payload = {
        'id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Situações para Token ausente, inválido ou expirado
def verificar_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'erro': 'Token é necessário.'}), 401
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'erro': 'Token expirado.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'erro': 'Token inválido.'}), 401
        return f(*args, **kwargs)
    return decorator


# Rota para login de usuário autorizado e geração de token
@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    usuario = dados.get('usuario')
    senha = dados.get('senha')
    usuario = "admin"
    senha = "1234"

    # Validação de dados
    if usuario == "admin" and senha == "1234":
        token = gerar_token(usuario)
        return jsonify({'token': token})
    return jsonify({'erro': 'Credenciais inválidas.'}), 401

# Rotas protegidas pelo token
@app.route('/tarefas', methods=['GET'])
@verificar_token
def retornarProdutos():
    tarefas = Tarefa.query.all()
    return jsonify([{'id': t.id, 'nome': t.nome} for t in tarefas])


@app.route('/tarefas', methods=['POST'])
@verificar_token
def adicionarProdutos():
    tarefa_data = request.get_json()  
    nova_tarefa = Tarefa(nome=tarefa_data.get('nome'))
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify({'id': nova_tarefa.id, 'nome': nova_tarefa.nome})

@app.route('/tarefas/<int:id>', methods=['PUT'])
@verificar_token
def atualizarProdutos(id):
    tarefa = Tarefa.query.get(id)

    if tarefa:
        dados = request.json
        tarefa.nome = dados.get('nome', tarefa.nome)
        db.session.commit()
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada."})

@app.route('/tarefas/<int:id>', methods=['DELETE'])
@verificar_token
def deletarProdutos(id):
    tarefa = Tarefa.query.get(id)

    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({"mensagem": "Tarefa removida com sucesso"})
    else:
        return jsonify({"erro": "Tarefa não encontrada."})

@app.route('/')
def index():
    return render_template('index.html')

# Manipuladores de erros
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"erro": "Recurso não encontrado."}), 404

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"erro": "Requisição inválida."}), 400

if __name__ == '__main__':
    app.run(debug=True)