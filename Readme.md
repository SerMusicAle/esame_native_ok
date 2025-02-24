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

APPLICAZIONE
Component Login
- Login: 
    email: maurizio.nataloni@stravel.it
    password: uforobot

S Travel
S Travel è un'applicazione che offre un servizio per la ricerca di hotel e la prenotazione di mezzi di trasporto (voli e treni) in diverse città italiane. Grazie a un'interfaccia semplice e intuitiva, gli utenti possono trovare opzioni di viaggio, selezionare la destinazione, e prenotare servizi come voli o treni, tutto tramite un'applicazione React.

Tecnologie utilizzate
React: Per il frontend dell'applicazione (app mobile).
Axios: Per la gestione delle richieste HTTP verso il backend.
JSON: Per la gestione dei dati e la comunicazione tra client e server.
Python (Flask): Per i server middleware che gestiscono le richieste e risposte al database.
Database relazionale: Per la gestione dei dati, come informazioni sugli utenti e sulle disponibilità di voli e hotel.
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
Passaggi di installazione
Clona il repository:

bash
Copia codice
git clone <URL del progetto>
Installa le dipendenze per il frontend:

bash
Copia codice
cd client
npm install
Installa le dipendenze per il backend (server finale e server middleware):

bash
Copia codice
cd backend
pip install -r requirements.txt
Avvia i server:

Server finale: python app.py
Server middleware autorizzazioni: python auth_server.py
Server middleware gestione dati: python data_server.py
Avvia il client:

bash
Copia codice
npm start
Licenza
S Travel è un progetto gratuito. Puoi utilizzarlo e modificarlo a tuo piacimento.

Contributi
Se desideri contribuire al progetto, puoi fare un fork, creare una branch e inviare una pull request. Ogni contributo è benvenuto!

