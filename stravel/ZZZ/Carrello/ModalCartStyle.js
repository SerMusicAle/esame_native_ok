import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
    modalView: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      padding: 20,
    },
    modalText: {
      textAlign: 'center',
      fontSize: 24,
      marginBottom: 20,
      color: '#FFFFFF',
    },
    cartItem: {
      flexDirection: 'row',
      alignItems: 'center',
      marginBottom: 10,
    },
    cartImage: {
      width: 50,
      height: 50,
      resizeMode: 'contain',
      marginRight: 10,
    },
    cartDetails: {
      flex: 1,
    },
    cartTitle: {
      fontWeight: 'bold',
    },
});

export default styles;