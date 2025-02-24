# db_connection.py

import psycopg2
from connection.config import db_config


def get_db_connection():
    print("f_get_db_connection chiamata da server (connection.py)")  
    try:
        conn = psycopg2.connect(**db_config)
        print("f_get_db_connection chiamata diretta(connection.py)")
        return conn
    except Exception as e:
        print(f"-- Error connecting to the database: {e}")
        return None
    

# def get_db_session():
#     print ("f_gt_db_session chiamata (connection.py)")
#     return Session()

# Blocca di avvio (main)
if __name__ == "__main__":
    print("-- Esecuzione di db_connection.py come script principale")
    conn = get_db_connection()
    if conn:
        print("---- Connessione al database riuscita!")
        conn.close()
    else:
        print("---- Errore di connessione al database.")