from flask import Flask, jsonify
from google.cloud import storage

app = Flask(__name__)

#ruta de la conexion
@app.route('/exito/', methods=['GET'])
def revisar_conec():
    try:
        # Crea un cliente de almacenamiento usando las credenciales
        storage_client = storage.Client.from_service_account_json('ruta/a/tu/credencial.json')

        # Intenta listar los cubos (buckets) para verificar la conexión
        buckets = list(storage_client.list_buckets())

        # Si la conexion es exitosa, responde con "200 OK"
        return jsonify({"status": "200 OK", "message": "Conexión exitosa a Google Cloud Storage"})

    except Exception as e:
        # Si hay algún error, responde con un mensaje de error
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

#Al final ejecutarlo como python (nombre de tu scrip).py

#Created by Martin - Eduardo
