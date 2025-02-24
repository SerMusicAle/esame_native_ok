// components/TravelPack.js
import React from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';
import { Colors } from 'react-native/Libraries/NewAppScreen';

const TravelPack = () => {
  return (
    <View style={styles.card}>
      <Image 
        source={require('../assets/travel-image.jpg')} // Sostituisci con il percorso della tua immagine
        style={styles.image}
        resizeMode="cover"
      />
      <View style={styles.content}>
        <Text style={styles.label}>Tratta:</Text>
        <Text style={styles.value}>Tratta di un viaggio</Text>

        <Text style={styles.label}>Pernotto:</Text>
        <Text style={styles.value}>Hotel</Text>

        <Text style={styles.label}>Viaggio:</Text>
        <Text style={styles.value}>Aereo</Text>

        <Text style={styles.label}>Prenotazione:</Text>
        <Text style={styles.value}>Car sharing</Text>

        <Text style={styles.label}>Prezzo:</Text>
        <Text style={styles.value}>€600</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    borderRadius: 10,
    elevation: 3,
    margin: 10,
    overflow: 'hidden',
  },
  image: {
    width: '100%',
    height: 200,
  },
  content: {
    padding: 10,
  },
  label: {
    fontWeight: 'bold',
    fontSize: 16,
  },
  value: {
    fontSize: 14,
    marginBottom: 5,
  },

});

export default TravelPack;