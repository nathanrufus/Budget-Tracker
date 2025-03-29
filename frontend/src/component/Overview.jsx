import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Overview = () => {
  const [data, setData] = useState({ netWorth: 0, income: 0, expenses: 0 });

  useEffect(() => {
    axios.get('http://localhost:5000/api/summary')
      .then(res => setData(res.data))
      .catch(err => console.error(err));
  }, []);

  const percent = (num) => `${num > 0 ? '+' : ''}${num.toFixed(1)}%`;

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 my-4">
      <div className="bg-green-50 p-4 rounded-xl shadow">
        <h4 className="text-sm font-semibold">Net Worth</h4>
        <p className="text-xl font-bold">${data.netWorth.toFixed(2)}</p>
        <p className="text-green-600 text-sm">{percent(5.2)}</p>
      </div>
      <div className="bg-green-50 p-4 rounded-xl shadow">
        <h4 className="text-sm font-semibold">Income</h4>
        <p className="text-xl font-bold">${data.income.toFixed(2)}</p>
        <p className="text-green-600 text-sm">{percent(2.1)}</p>
      </div>
      <div className="bg-red-50 p-4 rounded-xl shadow">
        <h4 className="text-sm font-semibold">Expenses</h4>
        <p className="text-xl font-bold">${data.expenses.toFixed(2)}</p>
        <p className="text-red-600 text-sm">{percent(-3.8)}</p>
      </div>
    </div>
  );
};

export default Overview;
