import React, { useState } from 'react';
import { View, Text, Button, StyleSheet, Modal, TextInput, Picker } from 'react-native';
import axios from 'axios';
import ResultsHotel from './ResultsHotel';

const ModalHotel = ({ visible, onClose, setActiveComponent }) => {
  const [city, setCity] = useState('');
  const [minPrice, setMinPrice] = useState('');
  const [maxPrice, setMaxPrice] = useState('');

  const handleSearch = async () => {
    const searchData = {
      city,
      minPrice,
      maxPrice,
    };

    try {
      await axios.post('http://localhost:5003/hotelCerca', searchData);
      console.log('Dati inviati al server con successo', searchData);
      
      // Imposta il componente attivo a ResultsHotel
      setActiveComponent({ component: ResultsHotel, props: { city, minPrice, maxPrice } });
    } catch (error) {
      console.error('Errore nell\'invio dei dati:', error);
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
        <Text style={styles.modalText}>Cerca Hotel</Text>
        
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

        <TextInput
          style={styles.input}
          placeholder="Prezzo minimo"
          value={minPrice}
          onChangeText={setMinPrice}
          keyboardType="numeric"
        />
        <TextInput
          style={styles.input}
          placeholder="Prezzo massimo"
          value={maxPrice}
          onChangeText={setMaxPrice}
          keyboardType="numeric"
        />

        <Button title="Cerca" onPress={handleSearch} />
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

export default ModalHotel;