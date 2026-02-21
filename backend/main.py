""" Importar módulos necesarios """
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector


""" Crear app flask """
app = Flask(__name__)
CORS(app)


""" Configurar base de datos """
def encender_bd():
    conectar = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "bd_final_pi"
    )
    return conectar
    

""" Definir las rutas solicitadas """
#ruta get
@app.route('/developer' , methods=['GET'])
def get_developer():
    conexion =encender_bd()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM developer")
    datos = cursor.fetchall()
    conexion.close()
    return jsonify(datos)
    
#ruta put
@app.route('/developer/<int:id>', methods=['PUT'])        
def actualizar_developers(id):
    datos = request.get_json()
    conexion =encender_bd()
    cursor = conexion.cursor()
    sql = "UPDATE developer SET name= %s, skills= %s, salary= %s, avatar= %s WHERE id= %s"
    valores = (datos['name'],datos['skills'],datos['salary'],datos['avatar'], id)
    cursor.execute(sql, valores)
    conexion.commit()
    return jsonify({"mensaje" : "Producto actualizado"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    

