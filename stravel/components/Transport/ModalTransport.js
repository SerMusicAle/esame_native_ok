import React, { useState, useEffect } from 'react';
import { View, Text, Button, StyleSheet, Modal, Picker, Alert } from 'react-native';
import axios from 'axios';
import ResultsTreno from './ResultsTreno';
import ResultsAereo from './ResultsAereo';



const ModalTransport = ({ visible, onClose, setActiveComponent }) => {
  const [city_start, setCityStart] = useState('');
  const [city_stop, setCityStop] = useState('');
  const [transportType, setTransportType] = useState('treno');
  const [errorMessage, setErrorMessage] = useState('');
  const [showErrorPopup, setShowErrorPopup] = useState(false);

  const trainSearch = async () => {
    const searchData = {
      city_start,
      city_stop,
      transportType,
    };

    if (!transportType) {
      setErrorMessage('Seleziona un mezzo di trasporto.');
      setShowErrorPopup(true);
      return;
    }

    if (!city_start || !city_stop) {
      setErrorMessage('Non sono state selezionate città di partenza e  di destinazione.');
      setShowErrorPopup(true);
      return;
    }

    try {
      let response;
      if (transportType === "treno") {
        response = await axios.post('http://localhost:5010/cercaTreno', searchData);
      } else if (transportType === "aereo") {
        response = await axios.post('http://localhost:5010/cercaAereo', searchData);
      }
      console.log('Dati inviati al server con successo', searchData);
      console.log('Risposta del server:', response.data);

      if (response.data.length === 0) {
        setErrorMessage('Non sono stati trovati risultati per la tua ricerca.'); // Alert
        setShowErrorPopup(true);
      return;
      }

      const resultsComponent = transportType === "treno" ? ResultsTreno : ResultsAereo;
      setActiveComponent({ component: resultsComponent, props: { city_start, city_stop, transportType } });
      onClose();
    } catch (error) {
      console.error('Errore nell\'invio dei dati:', error);
    }
  };


  useEffect(() => {
    if (showErrorPopup) {
      const timer = setTimeout(() => {
        setShowErrorPopup(false);
        setErrorMessage('');
      }, 5000);
      return () => clearTimeout(timer);
    }
  }, [showErrorPopup]);


  return (
    <Modal
      animationType="slide"
      transparent={true}
      visible={visible}
      onRequestClose={onClose}
    >
      <View style={styles.modalView}>
        <Text style={styles.modalText}>Seleziona mezzo di Trasporto</Text>

        {/* Picker per il tipo di trasporto */}
        <Picker
          selectedValue={transportType}
          style={styles.picker}
          onValueChange={(itemValue) => setTransportType(itemValue)}
        >
          <Picker.Item label="Seleziona Trasporto" value="" />
          <Picker.Item label="Treno" value="treno" />
          <Picker.Item label="Aereo" value="aereo" />
        </Picker>

        <Picker
          selectedValue={city_start}
          style={styles.picker}
          onValueChange={(itemValue) => setCityStart(itemValue)}
        >
          <Picker.Item label="Seleziona città di partenza" value="" />
          <Picker.Item label="Roma" value="Roma" />
          <Picker.Item label="Milano" value="Milano" />
          <Picker.Item label="Napoli" value="Napoli" />
          <Picker.Item label="Firenze" value="Firenze" />

        </Picker>

        <Picker
          selectedValue={ city_stop}
          style={styles.picker}
          onValueChange={(itemValue) => setCityStop(itemValue)}
        >
          <Picker.Item label="Seleziona città di arrivo" value="" />
          <Picker.Item label="Roma" value="Roma" />
          <Picker.Item label="Milano" value="Milano" />
          <Picker.Item label="Napoli" value="Napoli" />
          <Picker.Item label="Firenze" value="Firenze" />

        </Picker>

        <Button title="Cerca" onPress={trainSearch} />
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
  button: {
    marginVertical: 10,
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

export default ModalTransport;