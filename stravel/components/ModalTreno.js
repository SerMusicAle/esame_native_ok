import React, { useState } from 'react';
import { View, Text, Button, StyleSheet, Modal, Picker } from 'react-native';
import axios from 'axios';
import ResultsTreno from './ResultsTreno';

const ModalTreno = ({ visible, onClose, setActiveComponent }) => {
  const [city_start, setCityStart] = useState('');
  const [city_stop, setCityStop] = useState('');
  const [transportType, setTransportType] = useState('treno'); // Stato per il tipo di trasporto

  const trainSearch = async () => {
    const searchData = {
      city_start,
      city_stop,
      transportType,
    };

    try {
      if (transportType === "treno") {
        await axios.post('http://localhost:5010/cercaTreno', searchData);
        console.log('Dati inviati al server con successo', searchData);
      } else if (transportType === "aereo") {
        await axios.post('http://localhost:5010/cercaAereo', searchData);
        console.log('Dati inviati al server con successo', searchData);
      }

      // Imposta il componente attivo a ResultsTreno
      setActiveComponent({ component: ResultsTreno, props: { city_start, city_stop, transportType } });
      onClose(); // Chiudi il modal dopo aver impostato il componente attivo
    } catch (error) {
      console.error('Errore nell\'invio dei dati:', error);
    }
  };

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
          <Picker.Item label="Venezia" value="Venezia" />
          <Picker.Item label="Genova" value="Genova" />
          <Picker.Item label="Palermo" value="Palermo" />
          <Picker.Item label="Catania" value="Catania" />
          <Picker.Item label="Lecce" value="Lecce" />
          <Picker.Item label="Rimini" value="Rimini" />
          <Picker.Item label="Torino" value="Torino" />
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
          <Picker.Item label="Venezia" value="Venezia" />
          <Picker.Item label="Genova" value="Genova" />
          <Picker.Item label="Palermo" value="Palermo" />
          <Picker.Item label="Catania" value="Catania" />
          <Picker.Item label="Lecce" value="Lecce" />
          <Picker.Item label="Rimini" value="Rimini" />
          <Picker.Item label="Torino" value="Torino" />
        </Picker>

        <Button title="Cerca" onPress={trainSearch} />
        <View style={styles.buttonSpacer} />
        <Button title="Chiudi" onPress={onClose} />
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
});

export default ModalTreno;