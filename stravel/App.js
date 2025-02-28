import styles from './AppStyle';
import React, { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import Header from './components/Header/Header';


import Utente from './components/Utente/Utente';

import Login from './components/Login/Login';
import ModalHotel from './components/Hotel/ModalHotel';

import ModalHome from './components/Home/ModalHome';
import ModalTransport from './components/Transport/ModalTransport';
import ModalActivity from './components/Attività/ModalActivity';

import Footer from './components/Footer/Footer';


const App = () => {
  const [modalVisible, setModalVisible] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const [searchVisible, setSearchVisible] = useState(false);
  const [searchResults, setSearchResults] = useState([]); 
  const [searchType, setSearchType] = useState('hotel');

  const [trainVisible, setTrainVisible] = useState(false);
  const [trainResults, setTrainResults] = useState([]); 
  const [trainType, setTrainType] = useState('treno');

  const [activityVisible, setActivityVisible] = useState(false);
  const [activityResults, setActivityResults] = useState([]); 
  const [activityType, setActivityType] = useState('activity'); 

  const [cartVisible, setCartVisible] = useState(false);

  const [userData, setUserData] = useState(null);
  const [activeComponent, setActiveComponent] = useState({ component: ModalHome, props: {} });
  

  const handleLogin = (user) => {
    setIsLoggedIn(true);
    setUserData(user);
  };

  const handleSearch = (results, type) => {
    setSearchResults(results); 
    setSearchType(type); 
    setSearchVisible(false);
  };

  const trainSearch = (results, type) =>
  {
    setTrainResults(results);
    setTrainType(type); 
    setTrainVisible(false);
  }

  const activitySearch = (results, type) =>
    {
      setActivityResults(results);
      setActivityType(type); 
      setActivityVisible(false);
    }

  return (
    <View style={styles.container}>
      {!isLoggedIn ? (
        <Login onLogin={handleLogin} />
      ) : (
        <>
          {/* Barra superiore */}
          <Header 
            onMenuPress={() => setModalVisible(true)} 
            nome={userData.nome}
            cognome={userData.cognome}
          />

          {/* Modulo menu a scomparsa */}
          <Utente 
            visible={modalVisible} 
            onClose={() => setModalVisible(false)} 
            userName={`${userData.nome} ${userData.cognome}`} 
            email={userData.email} 
            onLogout={() => {
              setIsLoggedIn(false);
              setUserData(null);
              setModalVisible(false);
            }} 
/>



          {activeComponent && React.createElement(activeComponent.component, activeComponent.props)}
          {/* Barra inferiore */}
          <Footer 
            setSearchVisible={setSearchVisible}
            setTrainVisible={setTrainVisible}
            setCartVisible={setCartVisible}
            setActivityVisible={setActivityVisible}
            setActiveComponent={setActiveComponent}
          />

          {/* Modulo Carrello */}
          {/* <ModalCart 
            visible={cartVisible} 
            onClose={() => setCartVisible(false)} 
            cartItems={cartItems} 
          />
           */}
          {/* Modulo Ricerca Hotel */}
          <ModalHotel
            visible={searchVisible} 
            onClose={() => setSearchVisible(false)} 
            setActiveComponent={setActiveComponent}
          />

          {/* Modulo Ricerca Viaggi */}
          <ModalTransport
            visible={trainVisible} 
            onClose={() => setTrainVisible(false)} 
            setActiveComponent={setActiveComponent}
          />

          {/* Modulo Ricerca Attività */}
          <ModalActivity
            visible={activityVisible} 
            onClose={() => setActivityVisible(false)} 
            setActiveComponent={setActiveComponent}
          />
          </>
          
      )}
    


    </View>
  );
};

export default App;