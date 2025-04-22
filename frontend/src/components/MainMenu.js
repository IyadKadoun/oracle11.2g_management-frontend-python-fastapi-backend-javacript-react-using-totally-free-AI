import React, { Component } from "react";
import MenuItem1 from "./MenuItem1";
import MenuItem2 from "./MenuItem2";

class MainMenu extends Component {
  render() {
    return (
      <div className="main-menu">
        <ul>
          <li>
            <strong>القائمة الرئيسية</strong>
            <ul>
              <MenuItem1 />
              <MenuItem2 />
            </ul>
          </li>
        </ul>
      </div>
    );
  }
}

export default MainMenu;