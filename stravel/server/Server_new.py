from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from connection.connection import get_db_connection
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Consente tutte le origini

# LOGIN ---------------------------------------------------------------------------------------
@app.route('/login', methods=['POST'])
def login():
    print("SERVER - Richiesta di login ricevuta.")
    data = request.get_json(force=True, silent=True)
    if data is None:
        return jsonify({"error": "Dati non accessibili"}), 500

    email = data.get("email")
    password = data.get("password")

    try:
        conn = get_db_connection()
        if conn is None:
            return loginJson(email, password)

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM utenti WHERE email = %s AND password = %s", (email, password))
            user = cur.fetchone()
            if user:
                user_data = {
                    "id": user[0],
                    "nome": user[3],
                    "cognome": user[4],
                    "email": user[1]
                }
                return jsonify({"message": "Login riuscito!", "user": user_data}), 200
            else:
                return jsonify({"error": "Credenziali non valide"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

def loginJson(email, password):
    try:
        with open('../data/utenti.json') as f:
            utenti = json.load(f)
        user = next((u for u in utenti if u['email'] == email and u['password'] == password), None)
        if user:
            user_data = {
                "id": user[0], 
                "nome": user[3], 
                "cognome": user[4], 
                "email": user[1]
            }
            return jsonify({"message": "Login riuscito!"}), 200
        else:
            return jsonify({"error": "Credenziali non valide"}), 401
    except Exception as e:
        return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

# UTENTI TUTTI ------------------------------------------------------------------------------------
@app.route('/records', methods=['GET'])
def get_records():
    print("SERVER - Richiesta di recupero degli utenti ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            return handle_records_with_json()

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM utenti")
            records = cur.fetchall()
            utenti = [{"id": record[0], "nome": record[3], "cognome": record[4], "email": record[1]} for record in records]
            return jsonify(utenti), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

def handle_records_with_json():
    try:
        with open('../data/utenti.json') as f:
            utenti = json.load(f)
        return jsonify(utenti), 200
    except Exception as e:
        return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

# VOLI TUTTI ------------------------------------------------------------------------------------
@app.route('/voliTutti', methods=['GET'])
def get_voli():
    print("SERVER - Richiesta di recupero dei voli ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            return handle_voli_with_json()

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM voli")
            records = cur.fetchall()
            voli = [{"id": record[0], "partenza": record[1], "arrivo": record[2], "data": record[3]} for record in records]
            return jsonify(voli), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

def handle_voli_with_json():
    try:
        with open('../data/voli.json') as f:
            voli = json.load(f)
        return jsonify(voli), 200
    except Exception as e:
        return jsonify({"error": "Errore durante la lettura del file JSON."}), 500
    
    

#VOLO CERCA --------------------------------------------------------------------------------------
@app.route('/cercaAereo', methods=['POST'])
def cercaAereo():
    print("Richiesta di ricerca aerei ricevuta.")
    
    # Estrai i parametri dal corpo della richiesta
    data = request.get_json()
    partenza = data.get("city_start", "").strip()  # Assicurati che il valore sia una stringa e rimuovi spazi
    arrivo = data.get("city_stop", "").strip() 
    
    # Costruzione della query
    query = "SELECT * FROM voli WHERE TRUE"
    params = []

    if partenza:
        query += " AND partenza ILIKE %s"  # Assicurati che il nome della colonna sia corretto
        params.append(f'%{partenza}%')
         
    if arrivo:
        query += " AND arrivo ILIKE %s"  # Assicurati che il nome della colonna sia corretto
        params.append(f'%{arrivo}%')

    try:
        # Connessione al database
        conn = get_db_connection()
        if not conn:
            print("Connessione al database fallita.")
            return jsonify({"error": "Impossibile connettersi al database"}), 500
        
        with conn.cursor() as cur:
            cur.execute(query, params)
            voli = cur.fetchall()

        # Se vengono trovati voli, restituisci i risultati in formato JSON
        if voli:
            results = [
                {
                    'compagnia': volo[1],  # Assicurati che l'indice corrisponda alla colonna giusta
                    'dataora_partenza': volo[2],
                    'dataora_arrivo': volo[3],
                    'durata': volo[4],
                    'citta_partenza': volo[5],
                    'citta_arrivo': volo[6],
                }
                for volo in voli
            ]
            print(f"Trovati {len(results)} voli.")
            return jsonify(results), 200
        
        # Se non ci sono voli, restituisci un array vuoto
        print("Nessun volo trovato per il percorso specificato.")
        return jsonify([]), 200

    except Exception as e:
        print(f"Errore durante la ricerca dei voli: {str(e)}")
        return jsonify({"error": "Errore durante l'elaborazione della richiesta"}), 500

    
# TRENI TUTTI ------------------------------------------------------------------------------------
@app.route('/treniTutti', methods=['GET'])
def get_treni():
    print("SERVER - Richiesta di recupero dei treni ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Impossibile connettersi al database"}), 500

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM treni")  # Assicurati che la tabella 'treni' esista
            records = cur.fetchall()
            treni = [
                {
                    "Compagnia": record[1],  # Assicurati che l'indice corrisponda alla colonna giusta
                    "Data/Ora Partenza": record[2],
                    "Città di partenza": record[5],
                    "Data/Ora Arrivo": record[3],
                    "Città di arrivo": record[6],
                    "Durata": record[4]
                } 
                for record in records
            ]
            return jsonify(treni), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()


#TRENO CERCA --------------------------------------------------------------------------------------
@app.route('/cercaTreno', methods=['POST'])
def cercaTreno():
    print("Richiesta di ricerca treni ricevuta.")
    
    # Estrai i parametri dal corpo della richiesta
    data = request.get_json()
    partenza = data.get("city_start", "").strip()  # Assicurati che il valore sia una stringa e rimuovi spazi
    arrivo = data.get("city_stop", "").strip() 
    
    # Costruzione della query
    query = "SELECT * FROM treni WHERE TRUE"
    params = []

    if partenza:
        query += " AND citta_partenza ILIKE %s"
        params.append(f'%{partenza}%')
         
    if arrivo:
        query += " AND citta_arrivo ILIKE %s"
        params.append(f'%{arrivo}%')

    try:
        # Connessione al database
        conn = get_db_connection()
        if not conn:
            print("Connessione al database fallita.")
            return jsonify({"error": "Impossibile connettersi al database"}), 500
        
        with conn.cursor() as cur:
            cur.execute(query, params)
            treni = cur.fetchall()

        # Se vengono trovati treni, restituisci i risultati in formato JSON
        if treni:
            results = [
                {
                    'compagnia': treno[1],  # Assicurati che l'indice corrisponda alla colonna giusta
                    'dataora_partenza': treno[2],
                    'dataora_arrivo': treno[3],
                    'durata': treno[4],
                    'citta_partenza': treno[5],
                    'citta_arrivo': treno[6],
                }
                for treno in treni
            ]
            print(f"Trovati {len(results)} treni.")
            return jsonify(results), 200
        
        # Se non ci sono treni, restituisci un array vuoto
        print("Nessun treno trovato per il percorso specificato.")
        return jsonify([]), 200

    except Exception as e:
        print(f"Errore durante la ricerca dei treni: {str(e)}")
        return jsonify({"error": "Errore durante l'elaborazione della richiesta"}), 500


#HOTEL TUTTI --------------------------------------------------------------------------            
@app.route('/hotelTutti', methods=['GET'])
def get_hotel():
    print("SERVER - Richiesta di recupero degli hotel ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            return handle_hotel_with_json()

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM hotel")
            records = cur.fetchall()
            hotel_list = [
                {
                    'città': record[2],        # Assicurati che l'indice corrisponda alla colonna giusta
                    'indirizzo': record[3],    # Assicurati che l'indice corrisponda alla colonna giusta
                    'nome': record[1],         # Assicurati che l'indice corrisponda alla colonna giusta
                    'costostanza': record[4]   # Assicurati che l'indice corrisponda alla colonna giusta
                } 
                for record in records
            ]
            return jsonify(hotel_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
            
            
# HOTEL CERCA -----------------------------------------------------------------------------------
@app.route('/cercaHotel', methods=['POST'])
def cercaHotel():
    print("Richiesta di ricerca hotel ricevuta.")
    
    # Estrai i parametri dal corpo della richiesta
    data = request.get_json()
    citta = data.get("citta", "").strip()  # Assicurati che il valore sia una stringa e rimuovi spazi
    minPrice = data.get("minPrice") 
    maxPrice = data.get("maxPrice") 
    
    # Costruzione della query
    query = "SELECT * FROM hotel WHERE TRUE"
    params = []

    if citta:
        query += " AND citta ILIKE %s"
        params.append(f'%{citta}%')
         
    if minPrice is not None:
        query += " AND costostanza >= %s"
        params.append(minPrice)

    if maxPrice is not None:
        query += " AND costostanza <= %s"
        params.append(maxPrice)
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
                    'città': hotel[1],        # Città
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


#ATTIVITA TUTTE ------------------------------------------------------------------------------------------
@app.route('/attivitaTutti', methods=['GET'])
def get_attivita():
    print("SERVER - Richiesta di recupero delle attività ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            return handle_attivita_with_json()

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM attivita")  # Assicurati che la tabella 'attivita' esista
            records = cur.fetchall()
            attivita_list = [
                {
                    'città': record[0],         # Assicurati che l'indice corrisponda alla colonna giusta
                    'nomeattivita': record[1],  # Assicurati che l'indice corrisponda alla colonna giusta
                    'durata': record[2],        # Assicurati che l'indice corrisponda alla colonna giusta
                    'prezzo': record[3]         # Assicurati che l'indice corrisponda alla colonna giusta
                } 
                for record in records
            ]
            return jsonify(attivita_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

def handle_attivita_with_json():
    try:
        with open('../data/attivita.json') as f:
            attivita = json.load(f)
        return jsonify(attivita), 200
    except Exception as e:
        return jsonify({"error": "Errore durante la lettura del file JSON."}), 500

           
# ATTIVITA CERCA -----------------------------------------------------------------------------------
@app.route('/cercaAttivita', methods=['POST'])
def cercaAttivita():
    print("Richiesta di ricerca hotel ricevuta.")
    
    # Estrai i parametri dal corpo della richiesta
    data = request.get_json()
    citta = data.get("citta", "").strip()  # Assicurati che il valore sia una stringa e rimuovi spazi
    minPrice = data.get("minPrice") 
    maxPrice = data.get("maxPrice") 
    
    # Costruzione della query
    query = "SELECT * FROM attivita WHERE TRUE"
    params = []

    if citta:
        query += " AND citta ILIKE %s"
        params.append(f'%{citta}%')
         
    if minPrice is not None:
        query += " AND prezzo >= %s"
        params.append(minPrice)

    if maxPrice is not None:
        query += " AND prezzo <= %s"
        params.append(maxPrice)
    try:
        # Connessione al database
        conn = get_db_connection()
        if not conn:
            print("Connessione al database fallita.")
            return jsonify({"error": "Impossibile connettersi al database"}), 500
        
        with conn.cursor() as cur:
            cur.execute(query, params)
            hotels = cur.fetchall()

        if hotels:
            results = [
                {
                    'Città': hotel[1],
                    'Tipo Attività': hotel[2], 
                    'Durata': hotel[3],  
                    'Prezzo': hotel[4]
                }
                for hotel in hotels
            ]
            print(f"Trovate {len(results)} attività.")
            return jsonify(results), 200
        

        print("Nessuna attività trovata per la città specificata.")
        return jsonify([]), 200

    except Exception as e:
        print(f"Errore durante la ricerca delle attività: {str(e)}")
        return jsonify({"error": "Errore durante l'elaborazione della richiesta"}), 500


# AVVIA IL SERVER --------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)