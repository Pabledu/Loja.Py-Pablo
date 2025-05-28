from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo para os produtos
especies = [
    {"id": 1, "nome": "Píton Real", "preco": 49.90, "imagem": "pitonreal.jpeg"},
    {"id": 2, "nome": "Jiboia Arco-íris", "preco": 129.90, "imagem": "jiboiaarcoiris.jpeg"},
    {"id": 3, "nome": "Vestido Elegante", "preco": 199.90, "imagem": "vestido.jpg"},
    {"id": 4, "nome": "Jaqueta de Couro", "preco": 299.90, "imagem": "jaqueta.jpg"},
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