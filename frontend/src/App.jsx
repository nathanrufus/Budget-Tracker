import React from "react";
import Navbar from "./component/Navbar";
import Dashboard from "./component/Dashboard";
import Signup from "./component/Signup";
import Login from "./component/Login";
import UserDashboard from "./component/UserDashboard";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <div className="main-content">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/signin" element={<Login />} />
          <Route path="/userdashboard" element={<UserDashboard />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;


