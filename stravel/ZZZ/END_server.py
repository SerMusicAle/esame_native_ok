from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from connection.connection import get_db_connection
import threading
import time
import subprocess
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Consente tutte le origini


def check_timeout():
    time.sleep(3)
    try:
        print("CONNESSIONE FALLITA - DATABASE JSON ALTERNATIVO")
        subprocess.run(["python", "JS_server.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore nell'esecuzione del file Python: {e}")

# LOGIN ---------------------------------------------------------------------------------------
@app.route('/login', methods=['POST'])
def login():
    print("SERVER - Richiesta di login ricevuta.")
    data = None
    try:
        data = request.get_json(force=True, silent=True)
        print(f"SERVER - Dati ricevuti: {data}")
        if data is None:
            print("SERVER - Dati non accessibili.")
            return jsonify({"error": "Dati non accessibili"}), 500
    except Exception as e:
        print("SERVER - Errore durante il recupero dei dati:", str(e))
        return jsonify({"error": "Dati non accessibili"}), 500

    email = data.get("email")
    password = data.get("password")
    print(f"SERVER - Email ricevuta: {email}")
    print(f"SERVER - Password ricevuta: {password}")

    try:
        print("SERVER - Tentativo di connessione al database...")
        conn = get_db_connection()
        if conn is None:
            print("SERVER - Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/utenti.json') as f:
                    utenti = json.load(f)
                user = next((u for u in utenti if u['email'] == email and u['password'] == password), None)
                if user:
                    print("SERVER - Login riuscito per l'utente:", user)
                    return jsonify({"message": "Login riuscito!"}), 200
                else:
                    print("SERVER - Credenziali non valide per l'email:", email)
                    return jsonify({"error": "Credenziali non valide"}), 401
            except Exception as e:
                print("SERVER - Errore durante la lettura del file JSON:", str(e))
                return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

        with conn.cursor() as cur:
            print("SERVER - Esecuzione della query per verificare le credenziali...")
            cur.execute("SELECT * FROM utenti WHERE email = %s AND password = %s", (email, password))
            user = cur.fetchone()
            if user:
                user_data = {
                    "id": user[0],
                    "nome": user[3],
                    "cognome": user[4],
                    "email": user[1]
                }
                print("SERVER - Login riuscito per l'utente:", user_data)
                return jsonify({"message": "Login riuscito!", "user": user_data}), 200
            else:
                print("SERVER - Credenziali non valide per l'email:", email)
                return jsonify({"error": "Credenziali non valide"}), 401
    except Exception as e:
        print("SERVER - Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("SERVER - Chiusura della connessione al database.")
            conn.close()
        else:
            print("SERVER - Nessuna connessione da chiudere.")

# UTENTI TUTTI ------------------------------------------------------------------------------------
@app.route('/records', methods=['GET'])
def get_records():
    print("SERVER - Richiesta di recupero degli utenti ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            print("SERVER - Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/utenti.json') as f:
                    utenti = json.load(f)
                print("SERVER - Dati letti dal file JSON:", utenti)
                return jsonify(utenti), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("SERVER - Errore durante la lettura del file JSON:", str(e))
                return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM utenti")  # Modifica la query in base alle tue esigenze
            records = cur.fetchall()
            utenti = []
            for record in records:
                utenti.append({
                    "id": record[0],
                    "nome": record[3],
                    "cognome": record[4],
                    "email": record[1]
                })
            print("SERVER - Dati recuperati dal database:", utenti)
            return jsonify(utenti), 200
    except Exception as e:
        print("SERVER - Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("SERVER - Chiusura della connessione al database.")
            conn.close()

# VOLI TUTTI ------------------------------------------------------------------------------------
@app.route('/voliTutti', methods=['GET'])
def get_voli():
    print("SERVER - Richiesta di recupero dei voli ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            print("SERVER - Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/voli.json') as f:
                    voli = json.load(f)
                print("SERVER - Dati letti dal file JSON:", voli)
                return jsonify(voli), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("SERVER - Errore durante la lettura del file JSON:", str(e))
                return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM voli")  # Modifica la query in base alle tue esigenze
            records = cur.fetchall()
            voli = []
            for record in records:
                voli.append({
                    "id": record[0],
                    "partenza": record[1],
                    "arrivo": record[2],
                    "data": record[3]
                })
            print("SERVER - Dati recuperati dal database:", voli)
            return jsonify(voli), 200
    except Exception as e:
        print("SERVER - Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("SERVER - Chiusura della connessione al database.")
            conn.close()

# HOTEL TUTTI ------------------------------------------------------------------------------------
@app.route('/hotelTutti', methods=['GET'])
def get_hotel():
    print("SERVER - Richiesta di recupero degli hotel ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            print("SERVER - Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/hotel.json') as f:
                    hotel = json.load(f)
                print("SERVER - Dati letti dal file JSON:", hotel)
                return jsonify(hotel), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("SERVER - Errore durante la lettura del file JSON:", str(e))
                return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM hotel")  # Modifica la query in base alle tue esigenze
            records = cur.fetchall()
            hotel = []
            for record in records:
                hotel.append({
                    "id": record[0],
                    "nome": record[1],
                    "città": record[2],
                    "prezzo": record[3]
                })
            print("SERVER - Dati recuperati dal database:", hotel)
            return jsonify(hotel), 200
    except Exception as e:
        print("SERVER - Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("SERVER - Chiusura della connessione al database.")
            conn.close()

# HOTEL CERCA -----------------------------------------------------------------------------------
@app.route('/cercaHotel', methods=['POST'])
def cercaHotel():
    print("Richiesta di ricerca hotel ricevuta.")
    
    # Estrai i parametri dal corpo della richiesta
    data = request.get_json()
    citta = data.get("citta", "").strip()  # Assicurati che il valore sia una stringa e rimuovi spazi

    # Costruzione della query
    query = "SELECT * FROM hotel WHERE TRUE"
    params = []

    if citta:
        query += " AND citta ILIKE %s"
        params.append(f'%{citta}%')  # Aggiungi il parametro per la città

    try:
        # Connessione al database
        conn = get_db_connection()
        if not conn:
            print("Connessione al database fallita.")
            return jsonify({"error": "Impossibile connettersi al database"}), 500
        
        with conn.cursor() as cur:
            cur.execute(query, params)
            hotels = cur.fetchall()

        # Se vengono trovati hotel, restituisci i risultati in formato JSON
        if hotels:
            results = [
                {
                    'citta': hotel[1],        # Città
                    'indirizzo': hotel[2],    # Indirizzo
                    'nome': hotel[3],         # Nome
                    'costostanza': hotel[4]   # Costo
                }
                for hotel in hotels
            ]
            print(f"Trovati {len(results)} hotel.")
            return jsonify(results), 200
        
        # Se non ci sono hotel, restituisci un array vuoto
        print("Nessun hotel trovato per la città specificata.")
        return jsonify([]), 200

    except Exception as e:
        print(f"Errore durante la ricerca degli hotel: {str(e)}")
        return jsonify({"error": "Errore durante l'elaborazione della richiesta"}), 500

            

# TRENI TUTTI ------------------------------------------------------------------------------------
@app.route('/treniTutti', methods=['GET'])
def get_treni():
    print("SERVER - Richiesta di recupero dei treni ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            print("SERVER - Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/treni.json') as f:
                    treni = json.load(f)
                print("SERVER - Dati letti dal file JSON:", treni)
                return jsonify(treni), 200
            except Exception as e:
                print("SERVER - Errore durante la lettura del file JSON:", str(e))
                return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM treni")
            records = cur.fetchall()
            treni = []
            for record in records:
                treni.append({
                    "id": record[0],
                    "partenza": record[1],
                    "arrivo": record[2],
                    "data": record[3]
                })
            print("SERVER - Dati recuperati dal database:", treni)
            return jsonify(treni), 200
    except Exception as e:
        print("SERVER - Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("SERVER - Chiusura della connessione al database.")
            conn.close()

# CERCA TRENO -----------------------------------------------------------------------------------
@app.route('/trenoCerca', methods=['POST'])
def cercaTreno():
    print("SERVER - Richiesta di ricerca treno ricevuta.")
    try:
        data = request.get_json()
        print(f"SERVER - Dati ricevuti per la ricerca treno: {data}")
        partenza = data.get('partenza')
        arrivo = data.get('arrivo')
        data_treno = data.get('data')

        query = "SELECT * FROM treni WHERE TRUE"
        params = []

        if partenza:
            query += " AND partenza ILIKE %s"
            params.append(f'%{partenza}%')
        if arrivo:
            query += " AND arrivo ILIKE %s"
            params.append(f'%{arrivo}%')
        if data_treno:
            query += " AND data = %s"
            params.append(data_treno)

        print(f"SERVER - Query costruita: {query} con parametri: {params}")

        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute(query, params)
            treni = cur.fetchall()

        results = [
            {
                'id': treno[0],
                'partenza': treno[1],
                'arrivo': treno[2],
                'data': treno[3]
            }
            for treno in treni
        ]

        print(f"SERVER - Risultati della ricerca treno: {results}")
        return jsonify(results), 200

    except Exception as e:
        print("SERVER - Si è verificato un errore durante l'elaborazione della richiesta:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("SERVER - Chiusura della connessione al database.")
            conn.close()

# ATTIVITA TUTTI ------------------------------------------------------------------------------------
@app.route('/attivitaTutti', methods=['GET'])
def get_attivita():
    print("SERVER - Richiesta di recupero delle attività ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            print("SERVER - Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/attivita.json') as f:
                    attivita = json.load(f)
                print("SERVER - Dati letti dal file JSON:", attivita)
                return jsonify(attivita), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("SERVER - Errore durante la lettura del file JSON:", str(e))
                return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM attivita")  # Modifica la query in base alle tue esigenze
            records = cur.fetchall()
            attivita = []
            for record in records:
                attivita.append({
                    "id": record[0],
                    "nome": record[1],
                    "descrizione": record[2],
                    "prezzo": record[3]
                })
            print("SERVER - Dati recuperati dal database:", attivita)
            return jsonify(attivita), 200
    except Exception as e:
        print("SERVER - Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("SERVER - Chiusura della connessione al database.")
            conn.close()

if __name__ == '__main__':
    print("SERVER - Avvio del server finale...")
    app.run(host='0.0.0.0', port=5005, debug=True)