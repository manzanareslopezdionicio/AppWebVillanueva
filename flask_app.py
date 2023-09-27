from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('indevx.html')

"""@app.route('/login')
def login():
    return render_template('login.html')
"""
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/orden')
def orden():
    return render_template('orden.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

@app.route('/producto')
def producto():
    return render_template('producto.html')

@app.route('/datatables')
def datatables():
    return render_template('datatables.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)