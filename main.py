from flask import Flask, render_template, request, jsonify
import pandas as pd

#para lanzar back ejecutar en terminal: python main.py

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/registro', methods=['POST'])
def registro():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = generar_mail(nombre, apellido)
    contra = generar_contra (nombre,apellido)
    
    registro = pd.DataFrame({'Nombre': [nombre], 'Apellido': [apellido], 'Correo electrónico': [email], 'Contraseña':[contra]})

    try:
        archivo_csv = pd.read_csv('registros.csv')
        archivo_csv = archivo_csv.append(registro, ignore_index=True)
    except:
        archivo_csv = registro

    archivo_csv.to_csv('registros.csv', index=False)

    return render_template('success.html', nombre=nombre , apellido=apellido, correo=email , contraseña=contra)

def generar_mail(nombre, apellido):
    mail = (nombre + '.' + apellido).lower() + '@instituteghost.com'
    return mail

def generar_contra(nombre, apellido):
    contraseña = (nombre + apellido).lower()
    return contraseña

if __name__ == '__main__':
    app.run(debug=True)
