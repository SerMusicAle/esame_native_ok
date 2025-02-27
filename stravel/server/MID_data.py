from flask import Flask, jsonify, request
import requests
from flask_cors import CORS 
import json 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Consente tutte le origini

@app.before_request
def handle_preflight():
    if request.method == 'OPTIONS':
        response = jsonify({"message": "Preflight request handled"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response

# TUTTI UTENTI ------------------------------------------------------------------------------------
@app.route('/records', methods=['GET'])
def get_records():
    print("SERVER - Richiesta di recupero dei record ricevuta.")
    try:
        response = requests.get('http://localhost:5005/records')  # Inoltra la richiesta al server principale
        print(f"SERVER - Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
        if response.status_code != 200:
            print("SERVER - Errore nella risposta dal server principale.")
            return jsonify({"error": "Errore durante il recupero dei record."}), response.status_code
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("SERVER - Si è verificato un errore durante il recupero dei record Utenti:", str(e))
        return jsonify({"error": "Errore durante il recupero dei record."}), 500

# TUTTI I VOLI ------------------------------------------------------------------------------------
@app.route('/voliTutti', methods=['GET'])
def get_voli():
    print("SERVER - Richiesta di recupero dei record voli ricevuta.")
    try:
        response = requests.get('http://localhost:5005/voliTutti')  # Inoltra la richiesta al server principale
        print(f"SERVER - Risposta dal secondo server per i record: {response.status_code} - {response.text}")
        
        if response.status_code != 200:
            print("SERVER - Errore nella risposta dal server principale.")
            return jsonify({"error": "Errore durante il recupero dei record."}), response.status_code
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("SERVER - Si è verificato un errore durante il recupero dei record Voli:", str(e))
        return jsonify({"error": str(e)}), 500

# TUTTI I HOTEL ------------------------------------------------------------------------------------
@app.route('/hotelTutti', methods=['GET'])
def get_hotel():
    print("SERVER - Richiesta di recupero dei record hotel ricevuta.")
    try:
        response = requests.get('http://localhost:5005/hotelTutti')  # Inoltra la richiesta al server principale
        print(f"SERVER - Risposta dal secondo server per i record Hotel: {response.status_code} - {response.text}")
        
        if response.status_code != 200:
            print("SERVER - Errore nella risposta dal server principale.")
            return jsonify({"error": "Errore durante il recupero dei record."}), response.status_code
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("SERVER - Si è verificato un errore durante il recupero dei record hotel:", str(e))
        return jsonify({"error": str(e)}), 500

# CERCA HOTEL ------------------------------------------------------------------------------------
@app.route('/cercaHotel', methods=['POST'])
def cercaHotel():
    print("SERVER - Richiesta di ricerca hotel ricevuta.")
    try:
        # Ricevi i dati JSON dal client
        data = request.get_json()
        print("SERVER - Dati ricevuti dal client:", data)

        # Inoltra i dati al server sulla porta 5002
        print("SERVER - Inoltro dei dati al server sulla porta 5002...")
        response = requests.post('http://localhost:5005/cercaHotel', json=data)
        print(f"SERVER - Risposta dal server 5002: {response.status_code} - {response.text}")

        if response.status_code != 200:
            print("SERVER - Errore nella risposta dal server principale.")
            return jsonify({"error": "Errore durante la ricerca degli hotel."}), response.status_code

        # Restituisci la risposta del server 5002 al client
        print("SERVER - Restituzione della risposta al client...")
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("SERVER - Si è verificato un errore durante l'elaborazione della richiesta:", str(e))
        return jsonify({"error": str(e)}), 500

# TUTTI I TRENI ------------------------------------------------------------------------------------
@app.route('/treniTutti', methods=['GET'])
def get_treni():
    print("SERVER - Richiesta di recupero dei record treni ricevuta.")
    try:
        response = requests.get('http://localhost:5002/treniTutti')  # Inoltra la richiesta al server principale
        print (f"SERVER - Risposta dal secondo server per i record Treni: {response.status_code} - {response.text}")
        
        if response.status_code != 200:
            print("SERVER - Errore nella risposta dal server principale.")
            return jsonify({"error": "Errore durante il recupero dei record."}), response.status_code
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("SERVER - Si è verificato un errore durante il recupero dei record treni:", str(e))
        return jsonify({"error": str(e)}), 500

# CERCA TRENI ------------------------------------------------------------------------------------
@app.route('/cercaTreno', methods=['POST'])
def get_trenoCerca():
    print("SERVER - Richiesta di ricerca treno ricevuta.")
    try:
        # Ricevi i dati JSON dal client
        data = request.get_json()
        print("SERVER - Dati ricevuti dal client:", data)

        # Inoltra i dati al server sulla porta 5002
        print("SERVER - Inoltro dei dati al server sulla porta 5002...")
        response = requests.post('http://localhost:5002/cercaTreno', json=data)
        print(f"SERVER - Risposta dal server 5002: {response.status_code} - {response.text}")

        if response.status_code != 200:
            print("SERVER - Errore nella risposta dal server principale.")
            return jsonify({"error": "Errore durante la ricerca dei treni."}), response.status_code

        # Restituisci la risposta del server 5002 al client
        print("SERVER - Restituzione della risposta al client...")
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("SERVER - Si è verificato un errore durante l'elaborazione della richiesta:", str(e))
        return jsonify({"error": str(e)}), 500

# TUTTE LE ATTIVITA ------------------------------------------------------------------------------------
@app.route('/attivitaTutti', methods=['GET'])
def get_attivita():
    print("SERVER - Richiesta di recupero delle attività ricevuta.")
    try:
        response = requests.get('http://localhost:5002/attivitaTutti')  # Inoltra la richiesta al server principale
        print(f"SERVER - Risposta dal secondo server per i record Attività: {response.status_code} - {response.text}")
        
        if response.status_code != 200:
            print("SERVER - Errore nella risposta dal server principale.")
            return jsonify({"error": "Errore durante il recupero delle attività."}), response.status_code
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print("SERVER - Si è verificato un errore durante il recupero delle attività:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("SERVER - Avvio del server di richiesta dati...")
    app.run(host='0.0.0.0', port=5007, debug=True)