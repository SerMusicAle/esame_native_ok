from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from connection.connection import get_db_connection
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 



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
    print("SERVER - Funzione loginJson avviata.")
    
    try:
        print(f"SERVER - Tentativo di apertura del file utenti.json.")
        with open('../data/utenti.json') as f:
            utenti = json.load(f)
        print(f"SERVER - File utenti.json caricato correttamente.")

        # Eseguiamo il filtro dei dati JSON
        utenti_filtrati = [utente for utente in utenti if utente['email'] == email and utente['password'] == password]
        
        # Verifica se sono stati trovati utenti con le credenziali
        if utenti_filtrati:
            print(f"SERVER - Login riuscito per l'utente: {email}")
            return jsonify({"message": "Login riuscito!", "user": utenti_filtrati[0]}), 200
        else:
            print(f"SERVER - Nessun utente trovato con le credenziali fornite: {email}")
            return jsonify({"error": "Credenziali non valide"}), 401

    except FileNotFoundError:
        print("SERVER - Errore: il file utenti.json non è stato trovato.")
        return jsonify({"error": "File utenti non trovato."}), 500
    except json.JSONDecodeError:
        print("SERVER - Errore nel formato del file JSON.")
        return jsonify({"error": "Errore nel formato del file JSON."}), 500
    except Exception as e:
        print(f"SERVER - Errore durante la lettura del file JSON: {str(e)}")
        return jsonify({"error": f"Errore durante la lettura del file JSON: {str(e)}"}), 500




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
            voli = [
                {
                    "id": record[0], 
                    "partenza": record[1], 
                    "arrivo": record[2], 
                    "data": record[3]
                } 
                for record in records
            ]
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
    

    data = request.get_json()
    partenza = data.get("city_start", "").strip() 
    arrivo = data.get("city_stop", "").strip() 
    

    query = "SELECT * FROM voli WHERE TRUE"
    params = []

    if partenza:
        query += " AND partenza ILIKE %s" 
        params.append(f'%{partenza}%')
         
    if arrivo:
        query += " AND arrivo ILIKE %s"  
        params.append(f'%{arrivo}%')

    try:

        conn = get_db_connection()
        if not conn:
            print("Connessione al database fallita.")
            return aereoJson(partenza, arrivo)
            print("Risultato restituito da trenoJson:", result.get_json())
            return result
        
        with conn.cursor() as cur:
            cur.execute(query, params)
            voli = cur.fetchall()


        if voli:
            results = [
                {
                    'compagnia': volo[1],
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
        

        print("Nessun volo trovato per il percorso specificato.")
        return jsonify([]), 200

    except Exception as e:
        print(f"Errore durante la ricerca dei voli: {str(e)}")
        return jsonify({"error": "Errore durante l'elaborazione della richiesta"}), 500


        
def aereoJson(citta_partenza, citta_arrivo):
    try:
        with open('../data/voli.json', 'r') as file:
            voli = json.load(file)
    except FileNotFoundError:
        print("Errore: il file voli.json non è stato trovato.")
        return jsonify({"error": "File non trovato"}), 404
    except json.JSONDecodeError:
        print("Errore: il file JSON non è valido.")
        return jsonify({"error": "JSON non valido"}), 400

    risultatiAttivita = []
    for volo in voli:
        try:
            if (not citta_partenza or volo['citta_partenza'].lower() == citta_partenza.lower()) and \
               (not citta_arrivo or volo['citta_arrivo'].lower() == citta_arrivo.lower()):
                risultatiAttivita.append({
                    'compagnia': volo['compagnia'],
                    'dataora_partenza': volo['dataora_partenza'],
                    'dataora_arrivo': volo['dataora_arrivo'],
                    'durata': volo['durata'],
                    'citta_partenza': volo['citta_partenza'],
                    'citta_arrivo': volo['citta_arrivo'],
                })
        except KeyError as e:
            print(f"Errore: chiave mancante nel treno {volo}: {str(e)}")

    if risultatiAttivita:
        return jsonify(risultatiAttivita)  
    else:
        return jsonify([]) 
    
    
    
# TRENI TUTTI ------------------------------------------------------------------------------------
@app.route('/treniTutti', methods=['GET'])
def get_treni():
    print("SERVER - Richiesta di recupero dei treni ricevuta.")
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Impossibile connettersi al database"}), 500

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM treni")  
            records = cur.fetchall()
            treni = [
                {
                    "Compagnia": record[1], 
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


#TRENO CERCA -----------------------------------------------------------------------------------------------------------------------------
@app.route('/cercaTreno', methods=['POST'])
def cercaTreno():
    print("Richiesta di ricerca treni ricevuta.")
    

    data = request.get_json()
    partenza = data.get("city_start", "").strip()  
    arrivo = data.get("city_stop", "").strip() 
    

    query = "SELECT * FROM treni WHERE TRUE"
    params = []

    if partenza:
        query += " AND citta_partenza ILIKE %s"
        params.append(f'%{partenza}%')
         
    if arrivo:
        query += " AND citta_arrivo ILIKE %s"
        params.append(f'%{arrivo}%')

    try:

        conn = get_db_connection()
        if not conn:
            print("Connessione al database fallita.")
            return trenoJson(partenza, arrivo)
            print("Risultato restituito da trenoJson:", result.get_json())
            return result
        
        with conn.cursor() as cur:
            cur.execute(query, params)
            treni = cur.fetchall()


        if treni:
            results = [
                {
                    'compagnia': treno[1],  
                    'dataora_partenza': treno[2],
                    'dataora_arrivo': treno[3],
                    'durata': treno[4],
                    'citta_partenza': treno[5],
                    'citta_arrivo': treno[6],
                }
                for treno in treni
            ]
            print(f"Trovati {len(results)} treni.")
            print("Risultato restituito da cercaTreni (database):", jsonify(results).get_json())  
            return jsonify(results), 200
        

        print("Nessun treno trovato per il percorso specificato.")
        return jsonify([]), 200

    except Exception as e:
        print(f"Errore durante la ricerca dei treni: {str(e)}")
        return jsonify({"error": "Errore durante l'elaborazione della richiesta"}), 500

         
def trenoJson(citta_partenza, citta_arrivo):
    try:
        with open('../data/treni.json', 'r') as file:
            treni = json.load(file)
    except FileNotFoundError:
        print("Errore: il file treno.json non è stato trovato.")
        return jsonify({"error": "File non trovato"}), 404
    except json.JSONDecodeError:
        print("Errore: il file JSON non è valido.")
        return jsonify({"error": "JSON non valido"}), 400

    risultatiAttivita = []
    for treno in treni:
        try:
            if (not citta_partenza or treno['citta_partenza'].lower() == citta_partenza.lower()) and \
               (not citta_arrivo or treno['citta_arrivo'].lower() == citta_arrivo.lower()):
                risultatiAttivita.append({
                    'compagnia': treno['compagnia'],
                    'dataora_partenza': treno['dataora_partenza'],
                    'dataora_arrivo': treno['dataora_arrivo'],
                    'durata': treno['durata'],
                    'citta_partenza': treno['citta_partenza'],
                    'citta_arrivo': treno['citta_arrivo'],
                })
        except KeyError as e:
            print(f"Errore: chiave mancante nel treno {treno}: {str(e)}")

    if risultatiAttivita:
        return jsonify(risultatiAttivita)  
    else:
        return jsonify([]) 
   
            
# HOTEL CERCA ---------------------------------------------------------------------------------------------------------------------------
@app.route('/cercaHotel', methods=['POST'])
def cercaHotel():
    print("Richiesta di ricerca hotel ricevuta.")
    

    data = request.get_json()
    citta = data.get("citta", "").strip()  
    minPrice = data.get("minPrice") 
    maxPrice = data.get("maxPrice") 

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

        conn = get_db_connection()
        if not conn:
            print("Connessione al database fallita.")
            # return jsonify({"error": "Impossibile connettersi al database"}), 500
            return hotelJson(citta, minPrice, maxPrice)
            print("Risultato restituito da hotelJson:", result.get_json())  # Stampa il risultato
            return result
        
        with conn.cursor() as cur:
            cur.execute(query, params)
            hotels = cur.fetchall()


        if hotels:
            results = [
                {
                    'citta': hotel[1],        
                    'indirizzo': hotel[2],    
                    'nome': hotel[3],        
                    'costostanza': hotel[4]  
                }
                for hotel in hotels
            ]
            print(f"Trovati {len(results)} hotel.")
            print("Risultato restituito da cercaHotel (database):", jsonify(results).get_json())  
            return jsonify(results), 200

        print("Nessun hotel trovato per la citta specificata.")
        return jsonify([]), 200

    except Exception as e:
        print(f"Errore durante la ricerca degli hotel: {str(e)}")
        return jsonify({"error": "Errore durante l'elaborazione della richiesta"}), 500


def hotelJson(citta, minPrice, maxPrice):
    try:
        # Carica i dati dal file JSON
        with open('../data/hotel.json', 'r') as file:
            hotels = json.load(file)
    except FileNotFoundError:
        print("Errore: il file hotel.json non è stato trovato.")
        return jsonify([])  # Restituisce una lista vuota come JSON
    except json.JSONDecodeError:
        print("Errore: il file JSON non è valido.")
        return jsonify([])  # Restituisce una lista vuota come JSON

    # Filtrare gli hotel in base alla citta e al range di prezzo
    risultatiHotel = []
    for hotel in hotels:
        if hotel['citta'].lower() == citta.lower() and minPrice <= hotel['costostanza'] <= maxPrice:
            risultatiHotel.append({
                'citta': hotel['citta'],
                'indirizzo': hotel['indirizzo'],
                'nome': hotel['nome'],
                'costostanza': hotel['costostanza']
            })


    if risultatiHotel:
        return jsonify(risultatiHotel)  
    else:
        return jsonify([]) 



           
# ATTIVITA CERCA -------------------------------------------------------------------------------------------------------------------------
@app.route('/cercaAttivita', methods=['POST'])
def cercaAttivita():
    print("Richiesta di ricerca attività ricevuta.")
    
    data = request.get_json()
    citta = data.get("citta", "").strip()
    minPrice = data.get("minPrice") 
    maxPrice = data.get("maxPrice") 

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
        conn = get_db_connection()
        if not conn:
            print("Connessione al database fallita.")
            return attivitaJson(citta, minPrice, maxPrice)
            print("Risultato restituito da attivitaJson:", result.get_json())  # Stampa il risultato
            return result
        
        with conn.cursor() as cur:
            cur.execute(query, params)
            attivitas = cur.fetchall()

        if attivitas:
            results = [
                {
                    'citta': attivita[1],  
                    'nomeattivita': attivita[2], 
                    'durata': attivita[3], 
                    'prezzo': attivita[4]  
                }
                for attivita in attivitas
            ]
            print(f"Trovate {len(results)} attività.")
            print("Risultato restituito da cercaHotel (database):", jsonify(results).get_json())  
            return jsonify(results), 200

        print("Nessuna attività trovata per la città specificata.")
        return jsonify([]), 200

    except Exception as e:
        print(f"Errore durante la ricerca delle attività: {str(e)}")
        return jsonify({"error": "Errore durante l'elaborazione della richiesta"}), 500


def attivitaJson(citta, minPrice, maxPrice):
    try:
        with open('../data/attivita.json', 'r') as file:
            attivitas = json.load(file)
    except FileNotFoundError:
        print("Errore: il file attivita.json non è stato trovato.")
        return jsonify([])
    except json.JSONDecodeError:
        print("Errore: il file JSON non è valido.")
        return jsonify([])  

    risultatiAttivita = []
    for attivita in attivitas:
        if attivita['citta'].lower() == citta.lower() and minPrice <= attivita['prezzo'] <= maxPrice:
            risultatiAttivita.append({
                'citta': attivita['citta'],
                'nomeattivita': attivita['nomeattivita'],
                'durata': attivita['durata'],
                'prezzo': attivita['prezzo']
            })


    if risultatiAttivita:
        return jsonify(risultatiAttivita)  
    else:
        return jsonify([]) 



# AVVIA IL SERVER --------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
    
    
    
# # UTENTI TUTTI ------------------------------------------------------------------------------------
# @app.route('/records', methods=['GET'])
# def get_records():
#     print("SERVER - Richiesta di recupero degli utenti ricevuta.")
#     try:
#         conn = get_db_connection()
#         if conn is None:
#             return handle_records_with_json()

#         with conn.cursor() as cur:
#             cur.execute("SELECT * FROM utenti")
#             records = cur.fetchall()
#             utenti = [{"id": record[0], "nome": record[3], "cognome": record[4], "email": record[1]} for record in records]
#             return jsonify(utenti), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         if conn:
#             conn.close()

# def handle_records_with_json():
#     try:
#         with open('../data/utenti.json') as f:
#             utenti = json.load(f)
#         return jsonify(utenti), 200
#     except Exception as e:
#         return jsonify({"error": "Errore durante la lettura del file JSON."}), 500




# #HOTEL TUTTI --------------------------------------------------------------------------            
# @app.route('/hotelTutti', methods=['GET'])
# def get_hotel():
#     print("SERVER - Richiesta di recupero degli hotel ricevuta.")
#     try:
#         conn = get_db_connection()
#         if conn is None:
#             return handle_hotel_with_json()

#         with conn.cursor() as cur:
#             cur.execute("SELECT * FROM hotel")
#             records = cur.fetchall()
#             hotel_list = [
#                 {
#                     'citta': record[2],        
#                     'indirizzo': record[3],   
#                     'nome': record[1],         
#                     'costostanza': record[4]  
#                 } 
#                 for record in records
#             ]
#             return jsonify(hotel_list), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         if conn:
#             conn.close()



# #ATTIVITA TUTTE ------------------------------------------------------------------------------------------
# @app.route('/attivitaTutti', methods=['GET'])
# def get_attivita():
#     print("SERVER - Richiesta di recupero delle attività ricevuta.")
#     try:
#         conn = get_db_connection()
#         if conn is None:
#             return handle_attivita_with_json()

#         with conn.cursor() as cur:
#             cur.execute("SELECT * FROM attivita")  
#             records = cur.fetchall()
#             attivita_list = [
#                 {
#                     'citta': record[0],         
#                     'nomeattivita': record[1],  
#                     'durata': record[2],        
#                     'prezzo': record[3]       
#                 } 
#                 for record in records
#             ]
#             return jsonify(attivita_list), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         if conn:
#             conn.close()

# def handle_attivita_with_json():
#     try:
#         with open('../data/attivita.json') as f:
#             attivita = json.load(f)
#         return jsonify(attivita), 200
#     except Exception as e:
#         return jsonify({"error": "Errore durante la lettura del file JSON."}), 500