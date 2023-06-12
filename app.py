from flask import Flask, redirect, url_for, request
from flask import render_template
import database as dbase
import schema

db = dbase.conection_db()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registro',methods=["GET", "POST"])
def registro():
    if request.method == 'POST':  
        TablaU = db['usuario']
     # Obtener las propiedades del formulario
        email = request.form['email']
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        rol = request.form['rol']

        # validando que los datos existan 
        if email and cedula and nombre and apellido and direccion and rol :
         #creando el esquema de usuario
         usuario = schema.Usuario(email,cedula,nombre,apellido,direccion,rol)
         #insertando usuario en la tabla 
         TablaU.insert_one(usuario.__dict__)

         #mensaje de confirmacion  
         mensaje = "Usuario creado correctamente"

        else:
          mensaje = "Error al crear el usuario"
          
        return redirect(url_for('login'))
    
    return render_template('registro.html')
    

@app.route("/orden")
def orden():
    return render_template('orden.html')

@app.route("/cliente")
def cliente():
    return render_template('cliente.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)