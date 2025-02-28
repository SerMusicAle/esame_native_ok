// components/Copyright.js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const Copyright = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.copyrightText}>
        © 2025 S Management{'\n'}
        developer: Alessandro Sereni{'\n'}
        Tutti i diritti riservati.
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    marginTop: 20,
    padding: 10,
  },
  copyrightText: {
    fontSize: 14,
    color: 'white', 
    textAlign: 'center',
  },
});

export default Copyright;