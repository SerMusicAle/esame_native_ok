import React from 'react';
import { View, Text, Button, StyleSheet, Modal } from 'react-native';

const ModalMenu = ({ visible, onClose, userName, email, onLogout }) => {
  return (
    <Modal
      animationType="slide"
      transparent={true}
      visible={visible}
      onRequestClose={onClose}
    >
      <View style={styles.modalView}>
        <Text style={styles.welcomeText}>Bentornato,</Text>
        <Text style={styles.nameText}>{userName}</Text>
        <Text style={styles.emailText}>La tua email:</Text>
        <Text style={styles.emailText}>{email}</Text>

        <View style={styles.logoutContainer}>
          <Button title="Disconnetti" onPress={onLogout} />
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  modalView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    padding: 20,
  },
  welcomeText: {
    fontSize: 24,
    marginBottom: 10,
    color: '#FFFFFF',
    textAlign: 'center',
  },
  nameText: {
    fontSize: 20,
    marginBottom: 10,
    color: '#FFFFFF',
    textAlign: 'center',
  },
  emailText: {
    fontSize: 18,
    marginBottom: 20,
    color: '#FFFFFF',
    textAlign: 'center',
  },
  logoutContainer: {
    marginTop: 20,
  },
});

export default ModalMenu;