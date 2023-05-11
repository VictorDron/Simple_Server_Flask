from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

# Rota raiz, retorna uma mensagem simples
@app.route('/')
def hello_world():
    return 'Olá, mundo!'

# Rota para criar um novo usuário
@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    users.append(user)
    return 'Usuário criado com sucesso.', 201

# Rota para listar todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Rota para buscar um usuário pelo ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id >= len(users):
        return 'Usuário não encontrado.', 404
    return jsonify(users[user_id])

# Rota para atualizar um usuário existente
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id >= len(users):
        return 'Usuário não encontrado.', 404
    user = request.json
    users[user_id] = user
    return 'Usuário atualizado com sucesso.'

# Rota para excluir um usuário existente
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id >= len(users):
        return 'Usuário não encontrado.', 404
    users.pop(user_id)
    return 'Usuário excluído com sucesso.'

if __name__ == '__main__':
    app.run(debug=True)
