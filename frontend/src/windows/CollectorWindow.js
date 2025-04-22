import React, { Component } from "react";
import axiosInstance from "../axiosInstance";

class CollectorWindow extends Component {
  state = {
    collectors: [],
    searchUsername: "",
    newUsername: "",
    newTopMargin: "",
    newLeftMargin: "",
  };

  componentDidMount() {
    this.fetchData();
  }

  fetchData = () => {
    axiosInstance.get("/collector")
      .then((res) => this.setState({ collectors: res.data }))
      .catch((err) => console.error(err));
  };

  handleSearch = () => {
    const { searchUsername } = this.state;
    axiosInstance.get(`/collector?username=${searchUsername}`)
      .then((res) => this.setState({ collectors: res.data }))
      .catch((err) => console.error(err));
  };

  handleAdd = () => {
    const { newUsername, newTopMargin, newLeftMargin } = this.state;
    axiosInstance.post("/collector", {
      USERNAME: newUsername,
      TOPMARGIN: newTopMargin,
      LEFTMARGIN: newLeftMargin,
    })
      .then(() => this.fetchData())
      .catch((err) => console.error(err));
  };

  handleDelete = (username) => {
    axiosInstance.delete(`/collector/${username}`)
      .then(() => this.fetchData())
      .catch((err) => console.error(err));
  };

  render() {
    const { collectors, searchUsername, newUsername, newTopMargin, newLeftMargin } = this.state;

    return (
      <div className="window">
        <h2>الجباة</h2>
        <input
          type="text"
          placeholder="ابحث بالاسم"
          value={searchUsername}
          onChange={(e) => this.setState({ searchUsername: e.target.value })}
        />
        <button onClick={this.handleSearch}>بحث</button>

        <h3>إضافة جباة جديد</h3>
        <input
          type="text"
          placeholder="اسم المستخدم"
          value={newUsername}
          onChange={(e) => this.setState({ newUsername: e.target.value })}
        />
        <input
          type="number"
          placeholder="هامش العلو"
          value={newTopMargin}
          onChange={(e) => this.setState({ newTopMargin: e.target.value })}
        />
        <input
          type="number"
          placeholder="هامش اليسار"
          value={newLeftMargin}
          onChange={(e) => this.setState({ newLeftMargin: e.target.value })}
        />
        <button onClick={this.handleAdd}>إضافة</button>

        <table>
          <thead>
            <tr>
              <th>اسم المستخدم</th>
              <th>هامش العلو</th>
              <th>هامش اليسار</th>
              <th>إجراءات</th>
            </tr>
          </thead>
          <tbody>
            {collectors.map((collector) => (
              <tr key={collector.USERNAME}>
                <td>{collector.USERNAME}</td>
                <td>{collector.TOPMARGIN}</td>
                <td>{collector.LEFTMARGIN}</td>
                <td>
                  <button>تعديل</button>
                  <button onClick={() => this.handleDelete(collector.USERNAME)}>حذف</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <button onClick={this.props.onClose}>إغلاق</button>
      </div>
    );
  }
}

export default CollectorWindow;