from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Configuración con los datos de tu captura de Railway
db_config = {
    'host': 'mysql-9zut.railway.internal',
    'user': 'root',
    'password': 'woJtnntqGoBHOsLWhXuSNhqZaFTHoDlA',
    'database': 'railway',
    'port': 3306
}

@app.route('/api/ruta', methods=['POST'])
def recibir_gps():
    try:
        data = request.json
        lat = data.get('Latitud')
        lng = data.get('Longitud')
        
        # Conexión a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Insertar en tu tabla Data_GPS_PME
        query = "INSERT INTO Data_GPS_PME (Latitud, Longitud) VALUES (%s, %s)"
        cursor.execute(query, (lat, lng))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Railway asigna el puerto automáticamente, pero usamos el 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)