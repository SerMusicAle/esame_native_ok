import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

const ResultsActivity = ({ results }) => {
  // Stampa l'oggetto ricevuto nel terminale
  console.log('Oggetto ricevuto:', results);

  if (!results || results.length === 0) {
    return (
      <View style={styles.container}>
        <Text style={styles.noResultsText}>Nessuna attività trovata.</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container}>
      {results && results.length > 0 ? (
        <>
          {results.map((attivita, index) => (
            <View key={index} style={styles.card}>
              <Text style={styles.activityName}>{attivita["Tipo Attività"]}</Text>
              <Text>Durata: {attivita.Durata}</Text>
              <Text>Prezzo: {attivita.Prezzo} €</Text>
              <Text>Città: {attivita.Città}</Text>
            </View>
          ))}
        </>
      ) : (
        <Text style={styles.noResultsText}>Nessuna attività trovata.</Text>
      )}
  
      {/* Stampa l'oggetto ricevuto come testo visibile */}
      {/* <View style={styles.debugContainer}>
        <Text style={styles.debugText}>Oggetto ricevuto: {JSON.stringify(results, null, 2)}</Text>
      </View> */}
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
  activityName: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  noResultsText: {
    textAlign: 'center',
    marginTop: 20,
    fontSize: 18,
    color: '#555',
  },
  debugContainer: {
    marginTop: 20,
    padding: 10,
    backgroundColor: '#e0e0e0',
    borderRadius: 8,
  },
  debugText: {
    fontSize: 14,
    color: '#333',
  },
});

export default ResultsActivity;