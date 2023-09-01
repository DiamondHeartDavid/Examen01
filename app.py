# Se importan las librerias necesarias (flask, pyodbc)
from flask import Flask, render_template
import pyodbc

# Se crea una instancia de la aplicación Flask
app = Flask(__name__)

# Se configura la cadena de conexión a la base de datos Access
connection_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\david\Documents\BuenasPracticas\Examen1\TallerDB.accdb"

# Función para conectarse a la base de datos
def connect_db():
    return pyodbc.connect(connection_string)

# Creé un html para la página de bienvenida
@app.route("/")
def index():
    return render_template("index.html")

# Se hace la ruta para el listado de todos los estudiantes
@app.route('/estudiantes')
def lista_estudiantes():
    con = connect_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM Estudiantes')
    estudiantes = cur.fetchall()
    con.close()
    #Se retorna el html de los estudiantes
    return render_template('estudiantes.html', estudiantes=estudiantes)

# Se hace la ruta para el listado de todos los cursos
@app.route('/cursos')
def lista_cursos():
    con = connect_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM Cursos')
    cursos = cur.fetchall()
    con.close()
    #Se retorna el html de los cursos
    return render_template('cursos.html', cursos=cursos)

if __name__ == '__main__':
    app.run(debug=True)
