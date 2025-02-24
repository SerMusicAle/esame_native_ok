LOGICA S Travel

S Travel offre
- ricerca di hotel 
- prenotazione di mezzi di trasporto (voli e treni) in diverse città italiane. 

Tecnologie utilizzate
- React: Per il frontend dell'applicazione (app mobile).
- Axios: Per la gestione delle richieste HTTP verso il backend.
- JSON: Per la gestione dei dati e la comunicazione tra client e server.
- Python (Flask): Per i server middleware che gestiscono le richieste e risposte al database.
- Database relazionale: Per la gestione dei dati, come informazioni sugli utenti e sulle disponibilità di voli e hotel.

Funzionalità principali
Ricerca hotel: Trova hotel nelle città in cui il servizio è attivo.
Prenotazione di voli e treni: Prenota voli aerei e treni tra diverse città italiane.
Selezione dei servizi: Gli utenti possono selezionare facilmente il servizio di interesse (hotel, voli, treni) tramite pulsanti situati nella parte inferiore dello schermo.
Autenticazione e gestione utenti: Il sistema prevede un middleware per l'autenticazione degli utenti.
Come usare il progetto
1. Setup del server
Il progetto richiede l'avvio di tre server:

Server finale: Gestisce le richieste del client e le interazioni con il database.
Server middleware per le autorizzazioni: Gestisce l'autenticazione e la registrazione degli utenti.
Server middleware per la gestione dei dati: Gestisce la ricerca e la prenotazione di voli, treni e hotel.
2. Setup del client
Client React: Fornisce un'interfaccia utente per la navigazione tra i servizi di ricerca e prenotazione.
3. Avviare il progetto
Esegui il server finale e i due server middleware.
Avvia il client React per interagire con l'applicazione.
Installazione
Requisiti
Node.js
Python
Database relazionale (MySQL/PostgreSQL)

INSTALLAZIONE

Clona il repository:
bash: git clone <URL del progetto>

Aprire la cartella di progetto
se ci si trova dentro la cartella esame_native_ok 
    cd stravel
verificare si sia dentro la cartella stravel

# Installazione dei pacchetti Node.js
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm

# Installazione delle dipendenze Node.js
npm install
npm install @react-navigation/native @react-navigation/stack
npm install react-native-screens
npm install react-native-safe-area-context
npm install @react-native-community/viewpager
npm install react-native-gesture-handler react-native-reanimated
npm install react-native-modal
npm install react-native-paper
npm install axios
npm install redux react-redux

# Installazione dei pacchetti Python
sudo apt-get install python3-pip
pip3 install Flask
pip3 install flask-cors
pip3 install psycopg2
pip3 install psycopg2-binary


Avvia i server:

Server finale: python app.py
Server middleware autorizzazioni: python auth_server.py
Server middleware gestione dati: python data_server.py
Avvia il client:



AVVIO
- Avvio terminale 1: 
    cd stravel
    cd server
    python3 AX_server.py
- Avvio terminale 2: 
    cd stravel
    cd server
    python3 AX_auth.py
- Avvio terminale 3:
    cd stravel
    cd server
    python3 AX_data.py
- Avvio terminale 4
    cd stravel
    npm run web



UTILIZZO APPLICAZIONE
Component Login
- Login: 
    email: maurizio.nataloni@stravel.it
    password: uforobot