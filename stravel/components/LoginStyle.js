import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  container: 
  {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
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
  formContainer: 
  {
    width: '80%',
    padding: 20,
    borderRadius: 10,
    elevation: 5,
    backgroundColor: 'rgba(255, 255, 255, 0.6)', // Sfondo bianco semi-trasparente
  },
  title: 
  {
    fontSize: 24,
    marginBottom: 20,
    textAlign: 'center',
    color: '#333', // Colore del testo più scuro
  },
  input: 
  {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 15,
    paddingHorizontal: 10,
    backgroundColor: 'white',
  },

  checkboxContainer: 
  {
    justifyContent: 'flex-end',
    alignItems: 'center',
    marginBottom: 15,
    borderColor: 'gray',
    borderWidth: 1,
    backgroundColor: 'white',
    
  },
  label: 
  {
    fontSize: 16,
    color: '#333',
  },
});

export default styles;