import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Expenses = () => {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/expense')
      .then(res => setExpenses(res.data.expenses))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="my-6">
      <h3 className="text-lg font-semibold mb-2">Expenses</h3>
      <div className="border rounded-lg">
        <div className="flex justify-between font-semibold p-2 border-b">
          <span className="w-1/4">Date</span>
          <span className="w-1/4">Category</span>
          <span className="w-1/4">Description</span>
          <span className="w-1/4 text-right">Amount</span>
        </div>
        {expenses.map(exp => (
          <div key={exp.id} className="flex justify-between p-2 border-b text-sm">
            <span className="w-1/4">{exp.date}</span>
            <span className="w-1/4 font-medium">{exp.category}</span>
            <span className="w-1/4">{exp.description}</span>
            <span className="w-1/4 text-right">${parseFloat(exp.amount).toFixed(2)}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Expenses