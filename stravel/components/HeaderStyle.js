import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 10,
    backgroundColor: '#6200EE',
  },
  menuButton: {
    fontSize: 24,
    color: '#FFFFFF',
  },
  logo: {
    width: 50,
    height: 50,
    resizeMode: 'contain',
  },
  titleContainer: {
    flex: 1, // Permette al contenitore di occupare lo spazio disponibile
    alignItems: 'center', // Allinea il testo al centro
    justifyContent: 'center', // Centra verticalmente
  },
  welcomeText: {
    fontSize: 18,
    color: 'white',
  },
  nameText: {
    fontSize: 16,
    color: '#FFFFFF',
  },
});

export default styles;