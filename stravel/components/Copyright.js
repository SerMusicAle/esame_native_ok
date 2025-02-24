// components/Copyright.js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const Copyright = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.copyrightText}>
        © 2025 S Management. Sviluppato da Alessandro Sereni. Tutti i diritti riservati.
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
    fontSize: 12,
    color: '#888',
  },
});

export default Copyright;