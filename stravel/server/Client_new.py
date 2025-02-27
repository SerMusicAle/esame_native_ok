import requests

def login(email, password):
    url = "http://127.0.0.1:5010/login"  # URL del server di autenticazione
    login_data = {
        "email": email,
        "password": password
    }
    
    try:
        response = requests.post(url, json=login_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il login: {e}")
        return None

def get_records():
    url = "http://127.0.0.1:5010/records" 
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
def get_voli():
    url = "http://127.0.0.1:5010/voliTutti"  
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
def get_hotel():
    url = "http://127.0.0.1:5010/hotelTutti"  
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
def get_hotel_citta(citta):
    url = "http://127.0.0.1:5010/cercaHotel"  
    dati_ricerca = {
        "citta": citta
    }

    try:
        response = requests.post(url, json=dati_ricerca)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la ricerca degli hotel: {e}")
        return None

def get_treni():
    url = "http://127.0.0.1:5010/treniTutti"  
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None
    
def get_attivita():
    url = "http://127.0.0.1:5010/attivitaTutti"  
    try:
        response = requests .get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il recupero dei record: {e}")
        return None

if __name__ == "__main__":
    print("Client di autenticazione avviato.")
    
    while True:
        print("Scegli quale operazione eseguire:")
        print("1. Login (richiede email e password)")
        print("2. Recupera dati tabella")
        print("3. Torna tutti i voli")
        print("4. Torna tutti gli hotel")
        print("5. Torna tutti i treni")
        print("6. Torna tutte le attività")
        print("7. Cerca hotel in base alla città")

        scelta = input("Inserisci il numero della tua scelta (1..7): ")

        if scelta == "1":
            email = input("Inserisci la mail: ")
            password = input("Inserisci la password: ")

            data = login(email, password)
            if data is not None:
                print("Response:", data) 
            else:
                print("Login fallito.")
        
        elif scelta == "2":
            data = get_records()
            if data is not None:
                print("Dati della tabella:")
                for record in data:
                    print(record) 
            else:
                print("Errore durante il recupero dei dati.")
        
        elif scelta == "3":
            data = get_voli()
            if data is not None:
                print("Dati della tabella:")
                for record in data:
                    print(record) 
            else:
                print("Errore durante il recupero dei dati.")
        
        elif scelta == "4":
            data = get_hotel()
            if data is not None:
                print("Dati della tabella:")
                for record in data:
                    print(record) 
            else:
                print("Errore durante il recupero dei dati.")
                
        elif scelta == "5":
            data = get_treni()
            if data is not None:
                print("Dati della tabella:")
                for record in data:
                    print(record) 
            else:
                print("Errore durante il recupero dei dati.")
        
        elif scelta == "6":
            data = get_attivita()
            if data is not None:
                print("Dati della tabella:")
                for record in data:
                    print(record) 
            else:
                print("Errore durante il recupero dei dati.")
        
        elif scelta == "7":
            citta = input("Inserisci il nome della città per la ricerca degli hotel: ")
            data = get_hotel_citta(citta)
            if data is not None:
                print("Hotel trovati nella città:", citta)
                for hotel in data:
                    print(hotel)
            else:
                print("Errore durante la ricerca degli hotel.")
        
        else:
            print("Scelta non valida. Inserisci da 1 a 7.")

        continue_choice = input("Vuoi continuare? (s/n): ")
        if continue_choice.lower() != 's':
            break