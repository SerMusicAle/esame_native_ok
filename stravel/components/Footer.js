// components/Footer.js
import React from 'react';
import { View, TouchableOpacity, Text } from 'react-native';
import styles from './FooterStyle';
import ModalTransport from './ModalTransport';

const Footer = ({ setSearchVisible, setCartVisible, setActiveComponent }) => {
  return (
    <View style={styles.footer}>
      <TouchableOpacity 
        style={styles.footerButton} 
        onPress={() => setSearchVisible(true)}>
        <Text>🏨</Text>
      </TouchableOpacity>
      
      <TouchableOpacity 
        style={styles.footerButton} 
        onPress={() => 
        setActiveComponent({
          component:ModalTransport,
          props: {}
        })
        }> 
        <Text>✈️</Text>
      </TouchableOpacity>
      
    </View>
  );
};

export default Footer;