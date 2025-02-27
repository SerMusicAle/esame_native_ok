// components/Login.js
import React, { useState } from 'react';
import { View, TextInput, Button, Image, StyleSheet, Dimensions, Alert, Text } from 'react-native';
import styles from './LoginStyle';
import axios from 'axios';
import { CheckBox } from 'react-native-elements';

const { width } = Dimensions.get('window');

//OGGETTO LOGINDATA
const Login = ({ onLogin }) => 
{
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [userData, setUserData] = useState(null);
  const [rememberMe, setRememberMe] = useState(false);
  const [error, setError] = useState('');

  const handleLogin = async () => {
    if (!username || !password) 
    {
      setError('Entrambi i campi sono obbligatori.');
      return;
    }

    const loginData = 
    {
      email: username,
      password: password,
    };

    try 
    {
      const response = await axios.post('http://127.0.0.1:5010/login', loginData);
      if (response.status === 200) {
        setUserData(response.data.user);
        console.log(response.data.user);

        Alert.alert("Login riuscito!", response.data.message);
        onLogin(response.data.user);
        setError('');
      }
    } 
    catch (error) 
    {
      if (error.response) 
        {
        setError(error.response.data.error || "Credenziali errate.");
      }
      else 
      {
        setError("Si è verificato un errore durante il login.");
      }
    }
  };

  const handleCheckboxChange = () => {
    setRememberMe(!rememberMe);
  };

  return (
    <View style={styles.container}>
      <Image source={require('../assets/logo.png')} style={styles.backgroundImage} />
      <View style={styles.formContainer}>
        {/* <Text style={styles.title}>Login</Text> */}
        <TextInput
          style={styles.input}
          placeholder="Username"
          value={username}
          onChangeText={setUsername}
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          secureTextEntry
          value={password}
          onChangeText={setPassword}
        />
        {/* <View style={styles.checkboxContainer}>
          <CheckBox
            title="Ricordami la login"
            checked={rememberMe}
            onPress={handleCheckboxChange}
          />
        </View> */}
        <Button title="Login" onPress={handleLogin} />

        {/* Mostra l'errore, se presente */}
        {error ? <Text style={styles.errorText}>{error}</Text> : null}
      </View>
    </View>
  );
};

export default Login;
