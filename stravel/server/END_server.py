#END SERVER ---------------------------------------------------------
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
CORS(app)

def check_timeout():
    time.sleep(3)
    # Esegui il file Python
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
        if data is None:
            return jsonify({"error": "Dati non accessibili"}), 500
    except Exception as e:
        print("Errore durante il recupero dei dati:", str(e))
        return jsonify({"error": "Dati non accessibili"}), 500

    email = data.get("email")
    password = data.get("password")

    print(f"Email ricevuta: {email}")
    print(f"Password ricevuta: {password}")

    try:
        print("Tentativo di connessione al database...")
        conn = get_db_connection()
        if conn is None:
            print("Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/utenti.json') as f:
                    utenti = json.load(f)
                user = next((u for u in utenti if u['email'] == email and u['password'] == password), None)
                if user:
                    print("Login riuscito per l'utente:", user)
                    return jsonify({"message": "Login riuscito!"}), 200
                else:
                    print("Credenziali non valide per l'email:", email)
                    return jsonify({"error": "Credenziali non valide"}), 401
            except Exception as e:
                print("Errore durante la lettura del file JSON:", str(e))
                return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

        with conn.cursor() as cur:
            print("Esecuzione della query per verificare le credenziali...")
            cur.execute("SELECT * FROM utenti WHERE email = %s AND password = %s", (email, password))
            user = cur.fetchone()
            if user:
                user_data = {
                    "id": user[0],
                    "nome": user[3],
                    "cognome": user[4],
                    "email": user[1]
                }
                print("Login riuscito per l'utente:", user_data)
                return jsonify({"message": "Login riuscito!", "user": user_data}), 200
            else:
                print("Credenziali non valide per l'email:", email)
                return jsonify({"error": "Credenziali non valide"}), 401
    except Exception as e:
        print("Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("Chiusura della connessione al database.")
            conn.close()
        else:
            print("Nessuna connessione da chiudere.")

# UTENTI TUTTI ------------------------------------------------------------------------------------
@app.route('/records', methods=['GET'])
def get_records():
    try:
        print("Richiesta di recupero degli utenti ricevuta.")
        conn = get_db_connection()
        if conn is None:
            print("Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/utenti.json') as f:
                    utenti = json.load(f)
                return jsonify(utenti), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("Errore durante la lettura del file JSON:", str(e))
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
            return jsonify(utenti), 200
    except Exception as e:
        print("Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("Chiusura della connessione al database.")
            conn.close()

# VOLI TUTTI ------------------------------------------------------------------------------------
@app.route('/voliTutti', methods=['GET'])
def get_voli():
    try:
        print("Richiesta di recupero dei voli ricevuta.")
        conn = get_db_connection()
        if conn is None:
            print("Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/voli.json') as f:
                    voli = json.load(f)
                return jsonify(voli), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("Errore durante la lettura del file JSON:", str(e))
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
            return jsonify(voli), 200
    except Exception as e:
        print("Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("Chiusura della connessione al database.")
            conn.close()

# HOTEL TUTTI ------------------------------------------------------------------------------------
@app.route('/hotelTutti', methods=['GET'])
def get_hotel():
    try:
        print("Richiesta di recupero degli hotel ricevuta.")
        conn = get_db_connection()
        if conn is None:
            print("Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/hotel.json') as f:
                    hotel = json.load(f)
                return jsonify(hotel), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("Errore durante la lettura del file JSON:", str(e))
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
            return jsonify(hotel), 200
    except Exception as e:
        print("Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("Chiusura della connessione al database.")
            conn.close()

# TRENI TUTTI ------------------------------------------------------------------------------------
@app.route('/treniTutti', methods=['GET'])
def get_treni():
    try:
        print("Richiesta di recupero dei treni ricevuta.")
        conn = get_db_connection()
        if conn is None:
            print("Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/treni.json') as f:
                    treni = json.load(f)
                return jsonify(treni), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("Errore durante la lettura del file JSON:", str(e))
                return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM treni")  # Modifica la query in base alle tue esigenze
            records = cur.fetchall()
            treni = []
            for record in records:
                treni.append({
                    "id": record[0],
                    "partenza": record[1],
                    "arrivo": record[2],
                    "data": record[3]
                })
            return jsonify(treni), 200
    except Exception as e:
        print("Si è verificato un errore:", str(e))
        return jsonify ({"error": str(e)}), 500
    finally:
        if conn:
            print("Chiusura della connessione al database.")
            conn.close()

# ATTIVITA TUTTI ------------------------------------------------------------------------------------
@app.route('/attivitaTutti', methods=['GET'])
def get_attivita():
    try:
        print("Richiesta di recupero delle attività ricevuta.")
        conn = get_db_connection()
        if conn is None:
            print("Errore: connessione al database fallita. Provo a leggere dal file JSON.")
            try:
                with open('../data/attivita.json') as f:
                    attivita = json.load(f)
                return jsonify(attivita), 200  # Restituisci i dati dal file JSON
            except Exception as e:
                print("Errore durante la lettura del file JSON:", str(e))
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
            return jsonify(attivita), 200
    except Exception as e:
        print("Si è verificato un errore:", str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            print("Chiusura della connessione al database.")
            conn.close()

    
if __name__ == '__main__':
    print("Avvio del server finale...")
    app.run(host='0.0.0.0', port=5002, debug=True)