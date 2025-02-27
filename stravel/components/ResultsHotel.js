import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

const ResultsHotel = ({ results }) => 
  {

  if (!results || results.length === 0) 
  {
    return (
      <View style={styles.container}>
        <Text style={styles.noResultsText}>Nessun hotel trovato.</Text>
      </View>
    );
  }


  return (
    <ScrollView style={styles.container}>

      {results.map((hotel, index) => 
      (
        <View key={index} style={styles.card}>
          <Text style={styles.hotelCity}>{hotel.città}</Text>
          <Text style={styles.hotelName}>{hotel.nome}</Text>
          <Text>Indirizzo: {hotel.indirizzo}</Text>
          <Text>Prezzo: {hotel.costostanza} €</Text>
        </View>
      ))}
    </ScrollView>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center', 
    color: '#333',
  },
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
  hotelName: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  noResultsText: {
    textAlign: 'center',
    marginTop: 20,
    fontSize: 18,
    color: '#555',
  },
});

export default ResultsHotel;