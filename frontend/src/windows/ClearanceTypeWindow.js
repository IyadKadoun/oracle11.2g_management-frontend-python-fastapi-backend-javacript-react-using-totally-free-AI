import React, { Component } from "react";
import axiosInstance from "../axiosInstance";

class ClearanceTypeWindow extends Component {
  state = {
    clearanceTypes: [],
    searchName: "",
    newName: "",
    newNB: "",
  };

  componentDidMount() {
    this.fetchData();
  }

  fetchData = () => {
    axiosInstance.get("/clearancetyp")
      .then((res) => this.setState({ clearanceTypes: res.data }))
      .catch((err) => console.error(err));
  };

  handleSearch = () => {
    const { searchName } = this.state;
    axiosInstance.get(`/clearancetyp?name=${searchName}`)
      .then((res) => this.setState({ clearanceTypes: res.data }))
      .catch((err) => console.error(err));
  };

  handleAdd = () => {
    const { newNB, newName } = this.state;
    axiosInstance.post("/clearancetyp", { NB: newNB, NAME: newName })
      .then(() => this.fetchData())
      .catch((err) => console.error(err));
  };

  handleDelete = (nb) => {
    axiosInstance.delete(`/clearancetyp/${nb}`)
      .then(() => this.fetchData())
      .catch((err) => console.error(err));
  };

  render() {
    const { clearanceTypes, searchName, newName, newNB } = this.state;

    return (
      <div className="window">
        <h2>نوع براءة الذمة</h2>
        <input
          type="text"
          placeholder="ابحث بالاسم"
          value={searchName}
          onChange={(e) => this.setState({ searchName: e.target.value })}
        />
        <button onClick={this.handleSearch}>بحث</button>

        <h3>إضافة نوع جديد</h3>
        <input
          type="number"
          placeholder="رقم النوع"
          value={newNB}
          onChange={(e) => this.setState({ newNB: e.target.value })}
        />
        <input
          type="text"
          placeholder="اسم النوع"
          value={newName}
          onChange={(e) => this.setState({ newName: e.target.value })}
        />
        <button onClick={this.handleAdd}>إضافة</button>

        <table>
          <thead>
            <tr>
              <th>رقم النوع</th>
              <th>اسم النوع</th>
              <th>إجراءات</th>
            </tr>
          </thead>
          <tbody>
            {clearanceTypes.map((clearance) => (
              <tr key={clearance.NB}>
                <td>{clearance.NB}</td>
                <td>{clearance.NAME}</td>
                <td>
                  <button>تعديل</button>
                  <button onClick={() => this.handleDelete(clearance.NB)}>حذف</button>
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

export default ClearanceTypeWindow;