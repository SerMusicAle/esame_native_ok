#MID_auth
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Consente tutte le origini



# login ---------------------------------------------------------------------------------------
@app.route('/login', methods=['POST'])
def login():
    print("SRV AUTH -Richiesta di login ricevuta.")
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    print(f"email ricevuto: {email}")
    print(f"Password ricevuta: {password}")

    # Inoltra i dati al secondo server
    try:
        print("Inoltro dei dati al secondo server...")
        response = requests.post('http://localhost:5005/login', json={"email": email, "password": password})
        print(f"Risposta dal secondo server: {response.status_code} - {response.text}")
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("Si è verificato un errore durante l'inoltro della richiesta:", str(e))
        return jsonify({"error": "Errore durante l'inoltro della richiesta."}), 500
    


if __name__ == '__main__':
    print("Avvio del server di autenticazione...")
    app.run(host='0.0.0.0', port=5006, debug=True)
    
    
    
# # TUTTI UTENTI ------------------------------------------------------------------------------------
# @app.route('/records', methods=['GET'])
# def get_records():
#     try:
#         print("Richiesta di recupero dei record ricevuta.")
#         response = requests.get('http://localhost:5002/records')  # Inoltra la richiesta al server principale
#         print(f"Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
#         return jsonify(response.json()), response.status_code
#     except Exception as e:
#         print("Si è verificato un errore durante il recupero dei record:", str(e))
#         return jsonify({"error": str(e)}), 500
    
# # TUTTI I VOLI ------------------------------------------------------------------------------------
# @app.route('/voliTutti', methods=['GET'])
# def get_voli():
#     try:
#         print("Richiesta di recupero dei record ricevuta.")
#         response = requests.get('http://localhost:5002/voliTutti')  # Inoltra la richiesta al server principale
#         print(f"Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
#         return jsonify(response.json()), response.status_code
#     except Exception as e:
#         print("Si è verificato un errore durante il recupero dei record:", str(e))
#         return jsonify({"error": str(e)}), 500
    
# # TUTTI I HOTEL ------------------------------------------------------------------------------------
# @app.route('/hotelTutti', methods=['GET'])
# def get_hotel():
#     try:
#         print("Richiesta di recupero dei record ricevuta.")
#         response = requests.get('http://localhost:5002/hotelTutti')  # Inoltra la richiesta al server principale
#         print(f"Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
#         return jsonify(response.json()), response.status_code
#     except Exception as e:
#         print("Si è verificato un errore durante il recupero dei record:", str(e))
#         return jsonify({"error": str(e)}), 500
    
# # TUTTI I TRENI------------------------------------------------------------------------------------
# @app.route('/treniTutti', methods=['GET'])
# def get_treni():
#     try:
#         print("Richiesta di recupero dei record ricevuta.")
#         response = requests.get('http://localhost:5002/treniTutti')  # Inoltra la richiesta al server principale
#         print(f"Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
#         return jsonify(response.json()), response.status_code
#     except Exception as e:
#         print("Si è verificato un errore durante il recupero dei record:", str(e))
#         return jsonify({"error": str(e)}), 500
    
# # TUTTE LE ATTIVITA ------------------------------------------------------------------------------------
# @app.route('/attivitaTutti', methods=['GET'])
# def get_attivita():
#     try:
#         print("Richiesta di recupero dei record ricevuta.")
#         response = requests.get('http://localhost:5002/attivitaTutti')  # Inoltra la richiesta al server principale
#         print(f"Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
#         return jsonify(response.json()), response.status_code
#     except Exception as e:
#         print("Si è verificato un errore durante il recupero dei record:", str(e))
#         return jsonify({"error": str(e)}), 500
