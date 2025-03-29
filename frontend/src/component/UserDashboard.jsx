import React from "react";
import Overview from "./Overview";
import Expenses from "./Expenses";
import Budgets from "./Budgets";

function UserDashboard() {
  return (
    <div className="p-6 max-w-5xl mx-auto mt-20">
      <Overview />
      <Expenses />
      <Budgets />
    </div>
  );
}

export default UserDashboard;
