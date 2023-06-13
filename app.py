from flask import Flask, redirect, url_for, request, flash
from flask import render_template
import database as dbase
import schema

db = dbase.conection_db()

app = Flask(__name__)

app.secret_key = 'LOL'

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

        #verificando si el usuario ya existe 
        if TablaU.find_one({'email': email}):
           flash('El usuario ya existe', 'error')
           return render_template('registro.html')
        
        # validando que los datos existan 
        if email and cedula and nombre and apellido and direccion and rol :
         #creando el esquema de usuario
         usuario = schema.Usuario(email,cedula,nombre,apellido,direccion,rol)
         #insertando usuario en la tabla 

         TablaU.insert_one(usuario.__dict__)

         #mensaje de confirmacion  
         flash('El usuario se creo correctamen', 'success')
         redirect(url_for('login'))
        else:
          flash('Todos los datos son necesarios', 'error')
          return redirect(url_for('registro'))
        
    
    return render_template('registro.html')
    

@app.route("/orden")
def orden():
    return render_template('orden.html')

@app.route("/cliente")
def cliente():
    return render_template('cliente.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)