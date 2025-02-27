#CL_Client

import requests

def login(email, password):
    url = "http://127.0.0.1:5001/login"  # URL del server di autenticazione
    login_data = {
        "email": email,
        "password": password
    }
    
    try:
        response = requests.post(url, json=login_data)
        response.raise_for_status()  # Solleva un'eccezione per codici di stato HTTP 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il login: {e}")
        return None

def get_records():
    url = "http://127.0.0.1:5003/records" 
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
def get_voli():
    url = "http://127.0.0.1:5003/voliTutti"  
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
def get_hotel():
    url = "http://127.0.0.1:5003/hotelTutti"  
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
def get_hotel_citta(citta):
    url = "http://127.0.0.1:5003/cercaHotel"  # URL del server sulla porta 5003
    dati_ricerca = {
        "citta": citta
    }

    try:
        response = requests.post(url, json=dati_ricerca)
        response.raise_for_status()  # Solleva un'eccezione per codici di stato HTTP 4xx/5xx
        return response.json()  # Restituisce i risultati in formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la ricerca degli hotel: {e}")
        return None

    
def get_treni():
    url = "http://127.0.0.1:5003/treniTutti"  
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
def get_attivita():
    url = "http://127.0.0.1:5003/attivitaTutti"  
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
    
   
