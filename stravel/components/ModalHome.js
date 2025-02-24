import React from 'react';
import { Image, View, Text, StyleSheet, Dimensions } from 'react-native';

const { width } = Dimensions.get('window');
const aspectRatio = 16 / 9; 

const ModalHome = () => {
  return (

      <View style={styles.container}>
         <Image source={require('../assets/logo.png')} style={styles.backgroundImage} />

        <Text style={styles.welcomeText}>Ben Tornato. Insieme realizzeremo il viaggio dei tuoi Sogni</Text>
        
        {/* Scheda per l'agenzia di viaggi */}
        <View style={styles.card}>
          <Text style={styles.cardTitle}>S Travel</Text>
          <Text style={styles.cardText}>Agenzia di viaggi specializzata in:</Text>
          <Text style={styles.cardText}>- Pacchetti vacanze</Text>
          <Text style={styles.cardText}>- Prenotazioni voli</Text>
          <Text style={styles.cardText}>- Hotel e alloggi</Text>
          <Text style={styles.cardText}>- Tour guidati</Text>
          <Text style={styles.cardText}>Contattaci per maggiori informazioni!</Text>
        </View>
      </View>
  );
};

const styles = StyleSheet.create({
 
  backgroundImage: 
    {
        position: 'absolute',
        top: 'auto',
        left: 0,
        width: '100%',
        height: '45%', 
        aspectRatio: 1.5, 
        resizeMode: 'contain', 
    },
  container: {
    flex: 1,
    justifyContent: 'center', // Centra il contenuto verticalmente
    alignItems: 'center', // Centra il contenuto orizzontalmente
    padding: 20,
  },
  welcomeText: {
    textAlign: 'center',
    fontSize: 24,
    fontWeight: 'bold',
    color: '#000', // Colore del testo
    marginBottom: 20, // Spazio sotto il testo di benvenuto
  },
  card: {
    backgroundColor: 'rgba(255, 255, 255, 0.9)', // Sfondo bianco semi-trasparente
    borderRadius: 10,
    padding: 20,
    width: '90%', // Larghezza della scheda
    shadowColor: '#000', // Colore dell'ombra
    shadowOffset: { width: 0, height: 2 }, // Offset dell'ombra
    shadowOpacity: 0.3, // Opacità dell'ombra
    shadowRadius: 4, // Raggio dell'ombra
    elevation: 5, // Elevazione per Android
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10, // Spazio sotto il titolo della scheda
  },
  cardText: {
    fontSize: 16,
    marginBottom: 5, // Spazio sotto ogni riga di testo
  },
});

export default ModalHome;