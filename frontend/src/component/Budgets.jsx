import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Budgets = () => {
  const [budgets, setBudgets] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/budgets')
      .then(res => setBudgets(res.data.budgets))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="my-6">
      <h3 className="text-lg font-semibold mb-2">Budgets</h3>
      {budgets.map(budget => {
        const percent = Math.min((budget.spent / budget.amount) * 100, 100).toFixed(0);
        return (
          <div key={budget.id} className="mb-4">
            <div className="flex justify-between mb-1 text-sm">
              <span className="font-medium">{budget.category}</span>
              <span>{`$${budget.spent} / $${budget.amount}`}</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div className="bg-black h-2 rounded-full" style={{ width: `${percent}%` }}></div>
            </div>
            <div className="text-xs text-gray-600 text-right mt-1">{percent}%</div>
          </div>
        );
      })}
    </div>
  );
};

export default Budgets;
