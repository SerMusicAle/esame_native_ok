// components/Footer.js
import React from 'react';
import { View, TouchableOpacity, Text } from 'react-native';
import styles from './FooterStyle';


const Footer = (
  { 
    setSearchVisible, 
    setTrainVisible, 
    setCartVisible, 
    setActivityVisible,
    setActiveComponent 
  }) => 
    {
      return (
        <View style={styles.footer}>
          <TouchableOpacity 
            style={styles.footerButton} 
            onPress={() => setSearchVisible(true)}>
            <Text>🏨</Text>
          </TouchableOpacity>
          
          <TouchableOpacity 
            style={styles.footerButton} 
            onPress={() => setTrainVisible(true)}>
            <Text>🚆</Text>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.footerButton} 
            onPress={() => setActivityVisible(true)}>
              <Text>🎲</Text>
          </TouchableOpacity>
        </View>
      );
    };

export default Footer;