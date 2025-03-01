import React, { useState } from 'react';
import { View, Text, Button, StyleSheet, Modal, TextInput, Picker } from 'react-native';
import axios from 'axios';
import ResultsActivity from './ResultsActivity'; 

const ModalActivity = ({ visible, onClose, setActiveComponent }) => {
  const [city, setCity] = useState('');
  const [minPrice, setMinPrice] = useState('');    
  const [maxPrice, setMaxPrice] = useState('');
  const [activityResults, setActivityResults] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');
  const [showErrorPopup, setShowErrorPopup] = useState(false);

  const activitySearch = async () => {
    const results = {
      citta: city,  
      minPrice: minPrice ? parseFloat(minPrice) : undefined,
      maxPrice: maxPrice ? parseFloat(maxPrice) : undefined,
    };

    // Controllo degli errori
    if (!city) {
      setErrorMessage('Seleziona una città.');
      setShowErrorPopup(true);
      return;
    }

    if (minPrice === '' || maxPrice === '') {
      setErrorMessage('Inserisci sia il prezzo minimo che il prezzo massimo.');
      setShowErrorPopup(true);
      return;
    }

    if (isNaN(minPrice) || isNaN(maxPrice)) {
      setErrorMessage('I prezzi devono essere numeri validi.');
      setShowErrorPopup(true);
      return;
    }

    if (parseFloat(minPrice) > parseFloat(maxPrice)) {
      setErrorMessage('Il prezzo minimo non può essere maggiore del prezzo massimo.');
      setShowErrorPopup(true);
      return;
    }

    try {
      const response = await axios.post('http://localhost:5010/cercaAttivita', results);
      console.log('Dati ricevuti dal server:', response.data);
      
      // Controllo se non ci sono risultati
      if (response.data.length === 0) {
        setErrorMessage('Non sono stati trovati risultati per la tua ricerca.');
        setShowErrorPopup(true);
        return;
      }

      setActivityResults(response.data);
      setActiveComponent({ component: ResultsActivity, props: { results: response.data } });
    } catch (error) {
      console.error('Errore nell\'invio dei dati:', error);
      setErrorMessage('Si è verificato un errore durante la ricerca delle attività.');
      setShowErrorPopup(true);
    }

    onClose(); 
  };

  return (
    <Modal
      animationType="slide"
      transparent={true}
      visible={visible}
      onRequestClose={onClose}
    >
      <View style={styles.modalView}>
        <Text style={styles.modalText}>Cerca Attività</Text>
        
        {/* Picker per la città */}
        <Picker
          selectedValue={city}
          style={styles.picker}
          onValueChange={(itemValue) => setCity(itemValue)}
        >
          <Picker.Item label="Seleziona città" value="" />
          <Picker.Item label="Roma" value="Roma" />
          <Picker.Item label="Milano" value="Milano" />
          <Picker.Item label="Napoli" value="Napoli" />
          <Picker.Item label="Firenze" value="Firenze" />
          <Picker.Item label="Venezia" value="Venezia" />
          <Picker.Item label="Genova" value="Genova" />
          <Picker.Item label="Palermo" value="Palermo" />
          <Picker.Item label="Catania" value="Catania" />
          <Picker.Item label="Lecce" value="Lecce" />
          <Picker.Item label="Rimini" value="Rimini" />
          <Picker.Item label="Torino" value="Torino" />
        </Picker>

        {/* Input per il prezzo minimo */}
        <TextInput
          style={styles.input}
          placeholder="Prezzo minimo"
          value={minPrice}
          onChangeText={setMinPrice}
          keyboardType="numeric"
        />

        {/* Input per il prezzo massimo */}
        <TextInput
          style={styles.input}
          placeholder="Prezzo massimo"
          value={maxPrice}
          onChangeText={setMaxPrice}
          keyboardType="numeric"
        />

        {/* Bottone per la ricerca */}
        <Button title="Cerca" onPress={activitySearch} />

        {/* Separator e bottone per chiudere */}
        <View style={styles.buttonSpacer} />
        <Button title="Chiudi" onPress={onClose} />

        {/* Popup di errore */}
        {showErrorPopup && (
          <View style={styles.errorPopup}>
            <Text style={styles.errorText}>{errorMessage}</Text>
          </View>
        )}
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  modalView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    padding: 20,
  },
  modalText: {
    fontSize: 24,
    marginBottom: 20,
    color: '#FFFFFF',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingLeft: 8,
    width: '100%',
    backgroundColor: '#FFFFFF',
  },
  picker: {
    height: 50,
    width: '100%',
    marginBottom: 10,
  },
  buttonSpacer: {
    height: 10,
  },
  errorPopup: {
    position: 'absolute',
    bottom: 50,
    left: 20,
    right: 20,
    backgroundColor: 'red',
    padding: 10,
    borderRadius: 5,
  },
  errorText: {
    color: '#FFFFFF',
    textAlign: 'center',
  },
});

export default ModalActivity;