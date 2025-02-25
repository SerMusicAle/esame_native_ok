#MID_data.py ---------------------------------------------

from flask import Flask, jsonify, request
import requests
from flask_cors import CORS 
import json 

app = Flask(__name__)
CORS(app)


# TUTTI UTENTI ------------------------------------------------------------------------------------
@app.route('/records', methods=['GET'])
def get_records():
    try:
        print("Richiesta di recupero dei record ricevuta.")
        response = requests.get('http://localhost:5002/records')  # Inoltra la richiesta al server principale
        print(f"Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("Si è verificato un errore durante il recupero dei record Utenti:", str(e))
        
    try:
        with open('data/utenti.json') as f:
            utenti = json.load(f)
            print("Dati letti dal file JSON.", utenti)
            return jsonify(utenti), 200
    except Exception as json_error:
        print("Si è verificato un errore durante la lettura del file JSON:", str(json_error))
        return jsonify({"error": "Errore durante il recupero dei record."}), 500

# TUTTI I VOLI ------------------------------------------------------------------------------------
@app.route('/voliTutti', methods=['GET'])
def get_voli():
    try:
        print("Richiesta di recupero dei record ricevuta.")
        response = requests.get('http://localhost:5002/voliTutti')  # Inoltra la richiesta al server principale
        print(f"Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("Si è verificato un errore durante il recupero dei record Voli:", str(e))
        return jsonify({"error": str(e)}), 500
    
    
# TUTTI I HOTEL ------------------------------------------------------------------------------------
@app.route('/hotelTutti', methods=['GET'])
def get_hotel():
    try:
        print("Richiesta di recupero dei record ricevuta.")
        response = requests.get('http://localhost:5002/hotelTutti')  # Inoltra la richiesta al server principale
        print(f"Risposta dal secondo server per i record Hotel: {response.status_code} - {response.text}")
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("Si è verificato un errore durante il recupero dei record:", str(e))
        return jsonify({"error": str(e)}), 500
    
# CERCA HOTEL ------------------------------------------------------------------------------------
@app.route('/hotelCerca', methods=['POST'])
def get_hotelCerca():
    try:
        # Ricevi i dati JSON dal client
        data = request.get_json()
        print("AX_DATA - Dati ricevuti dal client:", data)

        # Inoltra i dati al server sulla porta 5002
        response = requests.post('http://localhost:5002/hotelCerca', json=data)
        print(f"AX_DATA - Risposta dal server 5002: {response.status_code} - {response.text}")

        # Restituisci la risposta del server 5002 al client
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("Si è verificato un errore durante l'elaborazione della richiesta:", str(e))
        return jsonify({"error": str(e)}), 500
    
    
# TUTTI I TRENI------------------------------------------------------------------------------------
@app.route('/treniTutti', methods=['GET'])
def get_treni():
    try:
        print("Richiesta di recupero dei record ricevuta.")
        response = requests.get('http://localhost:5002/treniTutti')  # Inoltra la richiesta al server principale
        print(f"Risposta dal secondo server per i record Treni: {response.status_code} - {response.text}")
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("Si è verificato un errore durante il recupero dei record:", str(e))
        return jsonify({"error": str(e)}), 500
    
    
# TUTTE LE ATTIVITA ------------------------------------------------------------------------------------
@app.route('/attivitaTutti', methods=['GET'])
def get_attivita():
    try:
        print("Richiesta di recupero dei record ricevuta.")
        response = requests.get('http://localhost:5002/attivitaTutti')  # Inoltra la richiesta al server principale
        print(f"Risposta dal secondo server per i record Attività: {response.status_code} - {response.text}")
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("Si è verificato un errore durante il recupero dei record:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Avvio del server di autenticazione...")
    app.run(host='0.0.0.0', port=5003, debug=True)