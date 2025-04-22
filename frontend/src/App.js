import React, { Component } from "react";
import MainMenu from "./components/MainMenu";
import "./styles.css";

class App extends Component {
  render() {
    return (
      <div className="app-container">
        <h1>نظام إدارة الجباية</h1>
        <MainMenu />
      </div>
    );
  }
}

export default App;