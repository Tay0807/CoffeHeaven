from flask import Flask, redirect, request, render_template
lista = []
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']
    mensagem = [nome, email, mensagem]
    lista.append(mensagem)
    print(lista)
    return redirect('/')

if __name__ == '__main__':
    app.run()
