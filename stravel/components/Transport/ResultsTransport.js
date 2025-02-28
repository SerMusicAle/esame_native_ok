import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, ActivityIndicator } from 'react-native';
import axios from 'axios';

const ResultsTreno = ({ city_start, city_stop, transportType }) => {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const endpoint = transportType === 'treno' ? 'cercaTreno' : 'cercaAereo';
        const response = await axios.post(`http://localhost:5010/${endpoint}`, {
          city_start,
          city_stop,
        });
        setResults(response.data);
      } catch (err) {
        setError('Errore nel recupero dei dati.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [city_start, city_stop, transportType]);

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
      {results.map((item, index) => (
        <View key={index} style={styles.card}>
          <Text style={styles.trenoName}>{transportType === 'treno' ? item.compagnia : item.compagnia}</Text>
          <Text>{transportType === 'treno' ? `Partenza: ${item.dataora_partenza}` : `Partenza: ${item.dataora_partenza}`}</Text>
          <Text>{transportType === 'treno' ? `Arrivo: ${item.dataora_arrivo}` : `Arrivo: ${item.dataora_arrivo}`}</Text>
          <Text>{transportType === 'treno' ? `Durata: ${item.durata}` : `Durata: ${item.durata}`}</Text>
          <Text>{transportType === 'treno' ? `Città di Partenza: ${item.citta_partenza}` : `Città di Partenza: ${item.citta_partenza}`}</Text>
          <Text>{transportType === 'treno' ? `Città di Arrivo: ${item.citta_arrivo}` : `Città di Arrivo: ${item.citta_arrivo}`}</Text>
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
  trenoName: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  errorText: {
    color: 'red',
    textAlign: 'center',
    marginTop: 20,
  },
});

export default ResultsTreno;