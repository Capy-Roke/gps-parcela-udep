from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Configuración con tus datos de la imagen
db_config = {
    'host': 'mysql-9zut.railway.internal',
    'user': 'root',
    'password': 'tu_password_de_la_imagen',
    'database': 'railway',
    'port': 3306
}

@app.route('/api/ruta', methods=['POST'])
def recibir_gps():
    data = request.json
    lat = data.get('Latitud')
    lng = data.get('Longitud')
    
    # Insertar en tu tabla
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Data_GPS_PME (Latitud, Longitud) VALUES (%s, %s)", (lat, lng))
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"status": "ok"}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)