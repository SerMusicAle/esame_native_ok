import React, { useState, useEffect } from 'react';
import { Image, View, Text, Picker, StyleSheet, Button } from 'react-native';
import axios from 'axios';

const ModalTransport = () => {
  const [selectedTransport, setSelectedTransport] = useState(''); // Imposta il valore predefinito su una stringa vuota
  const [data, setData] = useState([]); // Stato per i dati recuperati
  const [error, setError] = useState(null); // Stato per gestire gli errori
  const [selectionError, setSelectionError] = useState(null); // Stato per gestire l'errore di selezione

  const fetchData = async () => {
    if (!selectedTransport) {
      setSelectionError('Effettua una selezione prima di premere cerca.'); // Imposta il messaggio di errore
      return; // Esci dalla funzione se non è stata effettuata una selezione
    }

    let url = '';
    if (selectedTransport === 'Treni') {
      url = 'http://127.0.0.1:5003/treniTutti';
    } else if (selectedTransport === 'Aerei') {
      url = 'http://127.0.0.1:5003/voliTutti';
    }

    try {
      const response = await axios.get(url);
      setData(response.data);
      setError(null); // Resetta l'errore se la richiesta ha successo
      setSelectionError(null); // Resetta l'errore di selezione
    } catch (err) {
      console.error('Errore durante il recupero dei dati:', err); // Stampa l'errore nella console
      setError('Si è verificato un errore durante il recupero dei dati.'); // Imposta un messaggio di errore
    }
  };

  useEffect(() => {
    if (selectedTransport) { // Recupera i dati solo se è selezionato un mezzo di trasporto
      fetchData();
    }
  }, [selectedTransport]);

  return (
    <View style={styles.container}>
      <Image source={require('../assets/logo.png')} style={styles.backgroundImage} />

      <View style={styles.contentContainer}>
        <Text style={styles.welcomeText}>Viaggiamo insieme...</Text>
        
        {/* Modulo di selezione per il mezzo di trasporto */}
        <View style={styles.pickerContainer}>
          <Picker
            selectedValue={selectedTransport}
            style={styles.picker}
            onValueChange={(itemValue) => {
              setSelectedTransport(itemValue);
              setSelectionError(null); // Resetta l'errore di selezione quando si cambia la selezione
            }}
          >
            <Picker.Item label="Come vuoi viaggiare?" value="" />
            <Picker.Item label="Treni" value="Treni" />
            <Picker.Item label="Aerei" value="Aerei" />
          </Picker>
        </View>

        {/* Bottone per ricaricare i dati */}
        <Button title="Ricarica Dati" onPress={fetchData} />

        {/* Mostra eventuali errori */}
        {selectionError && <Text style={styles.errorText}>{selectionError}</Text>}
        {error && <Text style={styles.errorText}>{error}</Text>}

        {/* Mostra i dati recuperati */}
        <View style={styles.dataContainer}>
          {data.length > 0 ? (
            data.map((item, index) => (
              <Text key={index} style={styles.dataText}>{JSON.stringify(item)}</Text>
            ))
          ) : (
            <Text style={styles.dataText}>Nessun dato disponibile.</Text>
          )}
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  backgroundImage: {
    position: 'absolute',
    top: 'auto',
    left: 0,
    width: '100%',
    height: '45%', 
    aspectRatio: 1.5, 
    resizeMode: 'contain', 
    zIndex: 1,
  },
  container: {
    borderColor: 'yellow',
    borderWidth: 5,
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  contentContainer: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'center',
    paddingTop: 20,
    zIndex: 2,
  },
  welcomeText: {
    textAlign: 'center',
    fontSize: 24,
    fontWeight: 'bold',
    color: '#000',
    marginBottom: 20,
  },
  picker: {
    height: 50,
    width: '100%',
    marginBottom: 20,
  },
  pickerContainer: {
    width: '100%',
  },
  errorText: {
    color: 'red',
    marginTop: 10,
  },
  dataContainer: {
    marginTop: 20,
    width: '100%',
    zIndex: 2,
  },
  dataText: {
    textAlign: 'center',
    marginVertical: 5,
  },
});

export default ModalTransport;