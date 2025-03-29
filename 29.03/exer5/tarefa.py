from flask import Flask, jsonify, request, render_template, render_template_string

app = Flask(__name__)

tarefas = [{'id': 1, 'nome': 'teste'}]


@app.route('/tarefas', methods=['GET'])
def retornarProdutos():
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def adicionarProdutos():
    tarefa_data = request.get_json()

    nova_tarefa = {
        'id': len(tarefas) + 1,
        'nome': tarefa_data.get('nome')
    }

    tarefas.append(nova_tarefa)

    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizarProdutos(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if tarefa:
        dados = request.json
        tarefa.update(dados)
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada."})

# MUDAR O PUT (ESTÁ ERRADO)

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletarProdutos(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if tarefa:
        tarefa.remove(tarefa)
        return jsonify({"mensagem": "Tarefa removida com sucesso"})
    else:
        return jsonify({"erro": "Tarefa não encontrada."})

if __name__ == '__main__':
app.run(debug=True)