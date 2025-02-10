import React from "react";
import Display from "./assets/display.webp"

function Services() {
  return (
    <div className="py-16 px-8 bg-white">
      {/* Heading Section */}
      <div className="text-center mb-16">
        <h1 className="text-4xl font-serif font-bold text-gray-800">Our Services</h1>
        <p className="text-lg text-gray-600 mt-2">Welcome to Our Services Page</p>
        {/* Feature Tabs */}
        <div className="mt-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">
        {/* Expense Tracking Card */}
        <div className="bg-white shadow-md rounded-lg p-6 hover:bg-purple-600 hover:text-white transition group">
          <h3 className="text-lg font-bold mb-2 group-hover:text-white">Expense Tracking</h3>
          <p className="text-sm text-gray-600 group-hover:text-white">
            Easily log your daily expenses.
          </p>
        </div>

        {/* Budget Management Card */}
        <div className="bg-purple-600 text-white shadow-md rounded-lg p-6 hover:scale-105 transition group">
          <h3 className="text-lg font-bold mb-2">Budget Management</h3>
          <p className="text-sm">
            Set limits by category and monitor progress.
          </p>
        </div>

        {/* Goal Setting Card */}
        <div className="bg-white shadow-md rounded-lg p-6 hover:bg-purple-600 hover:text-white transition group">
          <h3 className="text-lg font-bold mb-2 group-hover:text-white">Goal Setting</h3>
          <p className="text-sm text-gray-600 group-hover:text-white">
            Plan and achieve your savings targets.
          </p>
        </div>

        {/* Reports & Trends Card */}
        <div className="bg-white shadow-md rounded-lg p-6 hover:bg-purple-600 hover:text-white transition group">
          <h3 className="text-lg font-bold mb-2 group-hover:text-white">Reports & Trends</h3>
          <p className="text-sm text-gray-600 group-hover:text-white">
            Get detailed insights into your spending habits.
          </p>
        </div>

        {/* Notifications Card */}
        <div className="bg-white shadow-md rounded-lg p-6 hover:bg-purple-600 hover:text-white transition group">
          <h3 className="text-lg font-bold mb-2 group-hover:text-white">Notifications</h3>
          <p className="text-sm text-gray-600 group-hover:text-white">
            Stay on top of your finances with timely alerts.
          </p>
        </div>
      </div>

      </div>

      {/* Main Content Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center bg-gray-100 shadow-lg ">
        {/* Left Side - Text Content */}
        <div className="space-y-6  p-10">
          <h2 className="text-2xl font-bold text-gray-800">
            Our Users Save More and Stress Less:
          </h2>
          <p className="text-gray-600">
           <span className=" block">By using our app, users have reduced</span>  overspending by <span className="font-bold">83%</span> and gained better <span className=" block">control over their finances.</span>
          </p>
          <p className="text-gray-500 text-sm italic">
           <span className=" block"> Our intuitive tools have also helped users reach their</span> savings goals 3x faster, giving them the confidence to <span className=" block">manage their budgets and plan for the future.</span>
          </p>
          <div className="flex items-center space-x-4">
            <button className="px-6 py-3 bg-purple-600 text-white font-bold rounded shadow-lg hover:bg-purple-700 hover:shadow-xl transition">
              Get Started
            </button>
            <a
              href="#case-study"
              className="text-purple-600 font-semibold hover:underline hover:text-purple-800 transition"
            >
              Get the Case Study
            </a>
          </div>
        </div>

        {/* Right Side - Image and Statistics */}
        <div className="flex flex-row items-center justify-center">
          {/* Statistics Section */}
          <div className="flex flex-col ">
            <div className="bg-green-100 text-green-600 p-6 text-center shadow-md h-40">
              <h3 className="text-4xl font-bold">83%</h3>
              <p className="text-lg font-medium">Cost Savings</p>
              <p className="text-sm text-gray-500 mt-2">Save more efficiently.</p>
            </div>
            <div className="bg-red-100 text-red-600 p-6 text-center shadow-md h-49">
              <h3 className="text-4xl font-bold">3x</h3>
              <p className="text-lg font-medium">Faster Savings Goals</p>
              <p className="text-sm text-gray-500 mt-2">Achieve goals faster.</p>
            </div>
          </div>
          {/* Image */}
          <div cl>
            <img
            src={Display} 
            alt="App illustration"
            className=" shadow-lg h-88.5"
          />
          </div>
          
        </div>
      </div>
    </div>
  );
}

export default Services;
 {/* <div className="mt-6 lg:mt-0 flex justify-center lg:flex-1">
        <img
          src={Homedisp}
          alt="Financial Planning Desk"
          className="rounded-lg shadow-lg w-full max-w-[400px] lg:max-w-[80%] h-auto"
        />
      </div> */}