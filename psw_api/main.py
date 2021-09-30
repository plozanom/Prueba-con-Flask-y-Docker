from flask import Flask
from psw_armed import *

app = Flask(__name__)#Creando aplicación de servidor
#El servidor corre en http://127.0.0.1:5000 o localhost:5000

@app.route('/')#Ruta donde se encuentra la API (http://127.0.0.1:5000)
def getpsw():
    pssw = psw(armador_psw(lista_numeros()))
    return pssw

if __name__ == '__main__':#Inicializando el servidor
    app.run(debug=True)