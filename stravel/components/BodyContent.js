// components/BodyContent.js
import React from 'react';
import ModalHome from './ModalHome';
import ModalTransport from './ModalTransport';

const BodyContent = ({ activeComponent }) => {
  switch (activeComponent) {
    case 'ModalHome':
      return <ModalHome />;
    case 'ModalTransport':
      return <ModalTransport />;
    // Aggiungi altri casi per altri componenti
    default:
      return <ModalHome />;
  }
};

export default BodyContent;