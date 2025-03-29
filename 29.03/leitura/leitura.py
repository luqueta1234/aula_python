from flask import Flask, jsonify, request

app = Flask(__name__)

headers = {
    'Content-Type': 'application/json'
}

@app.route('/produtos', methods=['GET'])
def leituraProdutos():
    return jsonify({'id': '1',
                    'nome': 'Computador',
                    'preco': '1200.0'})

@app.route('/produtos/submit', methods=['POST'])

def criarProdutos():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type deve ser application/json'}), 400

    data = request.get_json()
    nome = data.get('nome')
    preco = data.get('preco')

    return jsonify({'nome': nome, 'preco': preco})

if __name__ == '__main__':
    app.run(debug=True)