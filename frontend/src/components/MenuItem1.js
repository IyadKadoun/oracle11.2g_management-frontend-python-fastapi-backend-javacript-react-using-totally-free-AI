import React, { Component } from "react";
import JabicenterWindow from "../windows/JabicenterWindow";
import CollectorWindow from "../windows/CollectorWindow";

class MenuItem1 extends Component {
  state = {
    showJabicenter: false,
    showCollector: false,
  };

  openJabicenter = () => this.setState({ showJabicenter: true });
  openCollector = () => this.setState({ showCollector: true });

  closeAllWindows = () => this.setState({ showJabicenter: false, showCollector: false });

  render() {
    const { showJabicenter, showCollector } = this.state;

    return (
      <li>
        قائمة الجباية
        <ul>
          <li>
            <button onClick={this.openJabicenter}>مراكز الجباة</button>
            {showJabicenter && <JabicenterWindow onClose={this.closeAllWindows} />}
          </li>
          <li>
            <button onClick={this.openCollector}>الجباة</button>
            {showCollector && <CollectorWindow onClose={this.closeAllWindows} />}
          </li>
        </ul>
      </li>
    );
  }
}

export default MenuItem1;