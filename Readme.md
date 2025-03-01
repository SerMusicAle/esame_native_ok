# LOGICA S TRAVEL

S Travel offre nelle città in cui opera
- ricerca di 
    - hotel
    - voli
    - viaggi in treno
    - attività 

Il progetto è svilippato in questa versione dimostrativa su:
- un server in grado di gestire le richieste dello sviluppo client su React.
- applicazione React Native come interfaccia utente


# Tecnologie utilizzate per lo sviluppo
- React: Per il frontend dell'applicazione (app mobile).
- Axios: Per la gestione delle richieste HTTP verso il backend.
- JSON: Per la gestione di interfacce, dati e la comunicazione tra client e server.
- Python: Per la gestione delle route del server per la gestione  delle richieste e delle risposte al database.
- Database relazionale (MySQL/PostgreSQL): Per la gestione dei dati, come informazioni sugli utenti e sulle disponibilità di voli e hotel.

# Librerie Frontend (React Native)
- React: La libreria principale per costruire l'interfaccia utente dell'applicazione mobile.
- Axios: Utilizzato per effettuare richieste HTTP al server backend per recuperare e inviare dati.
- React Navigation: Gestisce la navigazione tra le diverse schermate dell'applicazione.
- @react-navigation/native: Fornisce le funzionalità di navigazione di base.
- @react-navigation/stack: Implementa la navigazione a stack per gestire le schermate.
- React Native Screens: Ottimizza le prestazioni della navigazione in React Native.
- React Native Safe Area Context: Gestisce le aree sicure per il layout dell'applicazione, garantendo che il contenuto non venga sovrapposto da notch o barre di stato.
- @react-native-community/viewpager: Fornisce un componente ViewPager per la navigazione tra le pagine.
- React Native Gesture Handler: Gestisce i gesti dell'utente in modo più efficiente rispetto ai gesti predefiniti di React Native.
- React Native Reanimated: Fornisce animazioni fluide e performanti per l'interfaccia utente.
- React Native Modal: Permette di visualizzare modali per interazioni utente.
- React Native Paper: Fornisce componenti UI Material Design per un aspetto coerente e moderno.
- Redux e React-Redux: Gestiscono lo stato globale dell'applicazione, consentendo una gestione centralizzata dei dati.

# Librerie Backend (Python)
- Flask: Un framework web leggero per Python, utilizzato per costruire l'API del server.
- Flask-CORS: Abilita il Cross-Origin Resource Sharing (CORS) per consentire richieste da domini diversi.
- Psycopg2: Un driver PostgreSQL per Python, utilizzato per interagire con il database relazionale.



# Struttura dell'applicazione
Header:
- Logo
- messaggio di benvenuto
- Richiamo nominativo utente
- Pulsante menu utente
    - dati utente
    - dati copyright
    - pulsante disconnetti

Footer (Pulsanti dedicati per le funzionalità principali)
- Ricerca hotel: secondo parametri di città e fascia di prezzo.
- Ricerca di voli e treni:secondo il parametro di città.
- Ricerca di attività: secondo il parametro di città e fascia di prezzo


# INSTALLAZIONE

01. Clona la repository:
- bash: git clone <URL del progetto>


# Come usare il progetto 
01. Installazione dei pacchetti Node.js
- sudo apt-get update
- sudo apt-get install nodejs
- sudo apt-get install npm

02. Installazione delle dipendenze Node.js
- npm install
- npm install @react-navigation/native @react-navigation/stack
- npm install react-native-screens
- npm install react-native-safe-area-context
- npm install @react-native-community/viewpager
- npm install react-native-gesture-handler react-native-reanimated
- npm install react-native-modal
- npm install react-native-paper
- npm install axios
- npm install redux react-redux

03. Installazione dei pacchetti Python
- sudo apt-get install python3-pip
- pip3 install Flask
- pip3 install flask-cors
- pip3 install psycopg2
- pip3 install psycopg2-binary

04. Avvio del server: Il progetto richiede l'avvio di un server:
- bash01: python cartellaProgetto/stravel/server/server.py

05. Avvio dell'interfaccia client
- bash02: cd cartellaProgetto/stravel
- bash02: npm run web



# UTILIZZO DELL'APPLICAZIONE
01. Login:
- email: maurizio.nataloni@stravel.it
- password: uforobot