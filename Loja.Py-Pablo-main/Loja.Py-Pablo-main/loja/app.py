from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo para os produtos
especies = [
    {"id": 1, "nome": "Píton Real", "preco": 2578.99, "imagem": "pitonreal.jpeg"},
    {"id": 2, "nome": "Jiboia Arco-íris", "preco": 3198.51, "imagem": "jiboiaarcoiris.jpeg"},
    {"id": 3, "nome": "Gecko Leopardo", "preco": 3679.85, "imagem": "geckoleopardo.jpeg"},
    {"id": 4, "nome": "Sapo-de-chifre Argentino", "preco": 1500.00, "imagem": "sapodechifreargentino.jpeg"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/especies')
def mostrar_especies():
    return render_template('especies.html', especies=especies)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)