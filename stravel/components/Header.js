import React from 'react';
import { View, Text, TouchableOpacity, Image, StyleSheet } from 'react-native';
import styles from './HeaderStyle';

const Header = ({ onMenuPress, nome, cognome }) => 
{
  return (
    <View style={styles.header}>
      <TouchableOpacity onPress={onMenuPress}>
        <Text style={styles.menuButton}>☰</Text>
      </TouchableOpacity>
      
      <View style={styles.titleContainer}>
        <Text style={styles.welcomeText}>S travel, viaggiamo Sereni</Text>
        <Text style={styles.nameText}>{nome} {cognome}</Text>
      </View>

      <Image 
        source={require('../assets/logo.png')} 
        style={styles.logo} 
        resizeMode="contain" 
      />
    </View>
  );
};

export default Header;