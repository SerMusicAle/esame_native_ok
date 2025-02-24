import styles from './AppStyle';
import React, { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import Header from './components/Header';
import ModalCart from './components/ModalCart';
import Footer from './components/Footer';
import ModalMenu from './components/ModalMenu';
import BodyContent from './components/BodyContent';
import Login from './components/Login';
import ModalHotel from './components/ModalHotel';
import ModalTransport from './components/ModalTransport';
import ModalHome from './components/ModalHome';

const App = () => {
  const [modalVisible, setModalVisible] = useState(false);
  const [searchVisible, setSearchVisible] = useState(false);
  const [cartVisible, setCartVisible] = useState(false);
  const [activeComponent, setActiveComponent] = useState({ component: ModalHome, props: {} });
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [searchResults, setSearchResults] = useState([]); 
  const [searchType, setSearchType] = useState('hotel');
  const [userData, setUserData] = useState(null);

  // Dati del carrello
  const cartItems = [
    { id: 1, title: "Elemento 1", description: "Descrizione dell'elemento 1", image: require('./assets/logo.png') },
    { id: 2, title: "Elemento 2", description: "Descrizione dell'elemento 2", image: require('./assets/logo.png') },
    { id: 3, title: "Elemento 3", description: "Descrizione dell'elemento 3", image: require('./assets/logo.png') },
    { id: 4, title: "Elemento 4", description: "Descrizione dell'elemento 1", image: require('./assets/logo.png') },
    { id: 5, title: "Elemento 5", description: "Descrizione dell'elemento 2", image: require('./assets/logo.png') },
    { id: 6, title: "Elemento 6", description: "Descrizione dell'elemento 3", image: require('./assets/logo.png') },
  ];

  const handleLogin = (user) => {
    setIsLoggedIn(true);
    setUserData(user);
  };

  const handleSearch = (results, type) => {
    setSearchResults(results); 
    setSearchType(type); 
    setSearchVisible(false);
  };

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
          <ModalMenu 
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

          {/* Contenuto centrale */}
          {/* <BodyContent activeComponent={activeComponent} /> */}
          {activeComponent && React.createElement(activeComponent.component, activeComponent.props)}
          {/* Barra inferiore */}
          <Footer 
            setSearchVisible={setSearchVisible}
            setCartVisible={setCartVisible}
            setActiveComponent={setActiveComponent}
          />

          {/* Modulo Carrello */}
          <ModalCart 
            visible={cartVisible} 
            onClose={() => setCartVisible(false)} 
            cartItems={cartItems} 
          />
          
          {/* Modulo Ricerca Viaggi */}
          <ModalHotel
            visible={searchVisible} 
            onClose={() => setSearchVisible(false)} 
            setActiveComponent={setActiveComponent}
          />
          </>
      )}

    </View>
  );
};

export default App;