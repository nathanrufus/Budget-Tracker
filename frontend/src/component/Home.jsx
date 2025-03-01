import React from "react";
import Homedisp from "./assets/home.webp";

function Home() {
  return (
    <div className="h-screen flex flex-col lg:flex-row items-center justify-center bg-gradient-to-r from-pink-300 via-yellow-200 to-blue-300 px-4 lg:px-16">
      {/* Left Side - Text Content */}
      <div className="max-w-xl w-full space-y-6 text-center lg:text-left ">
        {/* Main Title */}
        <h1 className="text-4xl sm:text-5xl font-serif font-bold text-gray-800 leading-tight ">
          <span className="block">Take Control</span>
          <strong className="block">of Your</strong>
          <strong className="block">Finances</strong>
        </h1>
        {/* Subtitle */}
        <p className="text-base sm:text-lg text-gray-600 italic leading-relaxed">
          Track your expenses, set budgets, and achieve{" "}
          <span className="block">your financial goals—all in one place.</span>
        </p>
        {/* Button */}
        <button className="px-6 py-3 bg-purple-600 text-white text-base sm:text-lg font-bold rounded hover:bg-purple-700 transition">
          Get Started
        </button>
      </div>

      {/* Right Side - Image */}
      <div className="mt-6 lg:mt-0 flex justify-center lg:flex-1">
        <img
          src={Homedisp}
          alt="Financial Planning Desk"
          className=" rounded-4xl shadow-lg w-full max-w-[350px] sm:max-w-[600px] lg:max-w-[100%] h-auto"
        />
      </div>
    </div>
  );
}

export default Home;
