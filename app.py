from flask import flask

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return '<h1>Olá</h1>'

@app.route('/')
def pagina_inicial():
    return '<p>Colé</p>'

if __name__ == '__main__'
    app.run(debug=True)