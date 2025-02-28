import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, ActivityIndicator } from 'react-native';
import axios from 'axios';

const ResultsHotel = ({ city, minPrice, maxPrice }) => {
  const [hotels, setHotels] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchHotels = async () => {
      try {
        const response = await axios.post('http://localhost:5003/hotelCerca', {
          city,
          minPrice,
          maxPrice,
        });
        setHotels(response.data);
      } catch (err) {
        setError('Errore nel recupero dei dati degli hotel.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchHotels();
  }, [city, minPrice, maxPrice]);

  if (loading) {
    return <ActivityIndicator size="large" color="#0000ff" />;
  }

  if (error) {
    return (
      <View style={styles.container}>
        <Text style={styles.errorText}>{error}</Text>
      </View>
    );
  }

  return (
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
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
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
  errorText: {
    color: 'red',
    textAlign: 'center',
    marginTop: 20,
  },
});

export default ResultsHotel;