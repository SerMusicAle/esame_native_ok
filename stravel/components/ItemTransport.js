// ItemTransport.js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const ItemTransport = ({ item }) => {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>{item.compagnia}</Text>
      <Text>Partenza: {item.dataora_partenza}</Text>
      <Text>Arrivo: {item.dataora_arrivo}</Text>
      <Text>Durata: {item.durata}</Text>
      <Text>Città di partenza: {item.città_partenza}</Text>
      <Text>Città di arrivo: {item.città_arrivo}</Text>
    </View>
  );
};

<ScrollView style={styles.container}>
      <Text style={styles.title}>{city}</Text>
      {hotels.map((hotel, index) => (
        <View key={index} style={styles.card}>
          <Text style={styles.hotelName}>{hotel.nome}</Text>
          <Text>Indirizzo: {hotel.indirizzo}</Text>
          <Text>Prezzo: {hotel.costostanza} €</Text>
        </View>
      ))}
    </ScrollView>
const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    padding: 15,
    marginVertical: 10,
    borderRadius: 8,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.2,
    shadowRadius: 2,
    elevation: 1,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
});

export default ItemTransport;