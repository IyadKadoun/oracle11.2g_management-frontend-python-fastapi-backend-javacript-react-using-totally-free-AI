import React, { Component } from "react";
import axiosInstance from "../axiosInstance";

class JabicenterWindow extends Component {
  state = {
    centers: [],
    searchName: "",
    newName: "",
    newNB: "",
  };

  componentDidMount() {
    this.fetchData();
  }

  fetchData = () => {
    axiosInstance.get("/jabicenter")
      .then((res) => this.setState({ centers: res.data }))
      .catch((err) => console.error(err));
  };

  handleSearch = () => {
    const { searchName } = this.state;
    axiosInstance.get(`/jabicenter?name=${searchName}`)
      .then((res) => this.setState({ centers: res.data }))
      .catch((err) => console.error(err));
  };

  handleAdd = () => {
    const { newNB, newName } = this.state;
    axiosInstance.post("/jabicenter", { NB: newNB, NAME: newName })
      .then(() => this.fetchData())
      .catch((err) => console.error(err));
  };

  handleDelete = (nb) => {
    axiosInstance.delete(`/jabicenter/${nb}`)
      .then(() => this.fetchData())
      .catch((err) => console.error(err));
  };

  render() {
    const { centers, searchName, newName, newNB } = this.state;

    return (
      <div className="window">
        <h2>مراكز الجباة</h2>
        <input
          type="text"
          placeholder="ابحث بالاسم"
          value={searchName}
          onChange={(e) => this.setState({ searchName: e.target.value })}
        />
        <button onClick={this.handleSearch}>بحث</button>

        <h3>إضافة مركز جديد</h3>
        <input
          type="number"
          placeholder="رقم المركز"
          value={newNB}
          onChange={(e) => this.setState({ newNB: e.target.value })}
        />
        <input
          type="text"
          placeholder="اسم المركز"
          value={newName}
          onChange={(e) => this.setState({ newName: e.target.value })}
        />
        <button onClick={this.handleAdd}>إضافة</button>

        <table>
          <thead>
            <tr>
              <th>رقم المركز</th>
              <th>اسم المركز</th>
              <th>إجراءات</th>
            </tr>
          </thead>
          <tbody>
            {centers.map((center) => (
              <tr key={center.NB}>
                <td>{center.NB}</td>
                <td>{center.NAME}</td>
                <td>
                  <button>تعديل</button>
                  <button onClick={() => this.handleDelete(center.NB)}>حذف</button>
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

export default JabicenterWindow;