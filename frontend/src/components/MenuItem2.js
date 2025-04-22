import React, { Component } from "react";
import ClearanceTypeWindow from "../windows/ClearanceTypeWindow";

class MenuItem2 extends Component {
  state = {
    showClearanceType: false,
  };

  openClearanceType = () => this.setState({ showClearanceType: true });
  closeClearanceType = () => this.setState({ showClearanceType: false });

  render() {
    const { showClearanceType } = this.state;

    return (
      <li>
        <button onClick={this.openClearanceType}>نوع براءة الذمة</button>
        {showClearanceType && <ClearanceTypeWindow onClose={this.closeClearanceType} />}
      </li>
    );
  }
}

export default MenuItem2;