from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

print(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        num1 = int(request.form['numero1'])
        num2 = float(request.form['numero2'])

        soma = num1 + num2
        sub = num1 - num2
        mult = num1 * num2
        div = num1 / num2

        # redireciona para outra rota
        # url_for chama a função, não a rota
        return redirect(url_for('exibir_resultado', nome = nome, soma = soma, sub = sub, mult = mult, div = div))                                

    return render_template('formulario.html')

@app.route('/exibir')
def exibir_resultado():
    nome = request.args.get('nome')
    soma = request.args.get('soma')
    sub = request.args.get('sub')
    mult = request.args.get('mult')
    div = request.args.get('div')

    return render_template('exibir.html', nome = nome, soma = soma, sub = sub, mult = mult, div = div)

# @app.route('/var')
# def variavel():
#     palavra = 'Colé'
#     return f'<h1> Adicionado texto de var: {palavra}</h1>'

# @app.route('/idade/<int:ano>')
# def idade(ano):
#     calculoIdade = 2026 - ano
#     return f'Você tem {calculoIdade} anos!'

# @app.route('/salvar/<nome>/produtos')
# def salvar(nome):
#     return f'Você salvou o produto [ {nome} ] com sucesso'

# @app.route('/html')
# def pagina_html():
#     return render_template('index.html')

# @app.route('/rota')
# def pagina_rota():
#     return render_template('rota.html')

# @app.route('/calcular/<nome>/<int:ano>')
# def calcular(nome, ano):
#     ano_atual = datetime.now().year
#     idade = ano_atual - ano

#     if idade > 18:
#         status = 'Maior de idade'
#     elif idade == 18:
#         status = 'Maior de idade'
#     else:
#         status = 'Menor de idade'

#     return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, 
#                            nascimento = ano, idade = idade, status = status)

# @app.route('/dicionario')
# def dicionario():
#     dados = {
#         'chave': 'valor',
#         'curso': 'GTI',
#         'local': 'Fatec Jahu',
#         'semestre': 4
#     }
#     return render_template('dicionario.html', **dados)

# @app.route('/condicao/<int:valor>')
# def condicao(valor):
#     return render_template('condicao.html', valor =valor)

# @app.route('/perfil/<nome>')
# def perfil(nome):
#     usuarios = {
#         'admin': {
#             'nome': 'Administrador',
#             'email': 'admin@fatec.br',
#             'nivel': 'administrador',
#             'ativo': True,
#             'posts': 47
#         },
#         'joao':{
#             'nome': 'João Silva',
#             'email': 'joao@email.com',
#             'nivel': 'usuario',
#             'ativo': True,
#             'posts': 12

#         },
#         'maria':{
#             'nome': 'Maria Souza',
#             'email': 'maria@email.com',
#             'nivel': 'moderador',
#             'ativo': False,
#             'posts': 31
#         }
#     }

#     usuario = usuarios.get(nome)

#     return render_template('perfil.html', usuario=usuario, nome=nome)




# Última coisa
if __name__ == '__main__':
    app.run(debug=True)