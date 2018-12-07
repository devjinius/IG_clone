import React from 'react';
import styles from './styles.scss';

const Footer = (props, context) => (
  <footer className={styles.footer}>
    <div className={styles.column}>
      <nav className={styles.nav}>
        <ul className={styles.list}>
          <li className={styles.listItem}>ABOUT US</li>
          <li className={styles.listItem}>SUPPORT</li>
          <li className={styles.listItem}>BLOG</li>
          <li className={styles.listItem}>PRESS</li>
          <li className={styles.listItem}>API</li>
          <li className={styles.listItem}>JOBS</li>
          <li className={styles.listItem}>PRIVACY</li>
          <li className={styles.listItem}>TERMS</li>
          <li className={styles.listItem}>DIRECTORY</li>
          <li className={styles.listItem}>LANGUAGE</li>
        </ul>
      </nav>
    </div>
    <div className={styles.column}>
      <span className={styles.copyright}>@ 2018 IGCLONE</span>
    </div>
  </footer>
);

export default Footer;
