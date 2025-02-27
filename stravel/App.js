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
import ModalTreno from './components/ModalTreno';
import ModalActivity from './components/ModalActivity';

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
  
  
  // Dati del carrello
  // const cartItems = [
  //   { id: 1, title: "Elemento 1", description: "Descrizione dell'elemento 1", image: require('./assets/logo.png') },
  //   { id: 2, title: "Elemento 2", description: "Descrizione dell'elemento 2", image: require('./assets/logo.png') },
  //   { id: 3, title: "Elemento 3", description: "Descrizione dell'elemento 3", image: require('./assets/logo.png') },
  //   { id: 4, title: "Elemento 4", description: "Descrizione dell'elemento 1", image: require('./assets/logo.png') },
  //   { id: 5, title: "Elemento 5", description: "Descrizione dell'elemento 2", image: require('./assets/logo.png') },
  //   { id: 6, title: "Elemento 6", description: "Descrizione dell'elemento 3", image: require('./assets/logo.png') },
  // ];

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
          <ModalTreno
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