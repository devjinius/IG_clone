import React, { Component } from 'react';
import styles from './styles.scss';
import Footer from 'components/Footer';
import 'reset-css/reset.css';

class App extends Component {
  render() {
    return (
      <div className={styles.App}>
        <Footer />
      </div>
    );
  }
}

export default App;
