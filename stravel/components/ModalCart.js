import React from 'react';
import { View, Text, Button, StyleSheet, ScrollView, Image, Modal } from 'react-native';
import styles from './ModalCartStyle';

const ModalCart = ({ visible, onClose, cartItems }) => {
  return (
    <Modal
      animationType="slide"
      transparent={true}
      visible={visible}
      onRequestClose={onClose}
    >
      <View style={styles.modalView}>
        <ScrollView>
          <Text style={styles.modalText}>Carrello</Text>
          {cartItems.map(item => (
            <View key={item.id} style={styles.cartItem}>
              <Image source={item.image} style={styles.cartImage} />
              <View style={styles.cartDetails}>
                <Text style={styles.cartTitle}>{item.title}</Text>
                <Text>{item.description}</Text>
              </View>
            </View>
          ))}
          <Button title="Chiudi" onPress={onClose} />
        </ScrollView>
      </View>
    </Modal>
  );
};

export default ModalCart;