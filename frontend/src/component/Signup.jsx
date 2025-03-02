import React from "react";

function Signup() {
  return (
    <div className=" mt-20 min-h-screen flex items-center justify-center bg-white">
     <div className=" w-full max-w-sm bg-gray-100 shadow-lg p-8">
      <h1 className=" text-2xl font-bold text-center mb-4 text-purple-600"> Sign Up</h1>
      <form>
        <input placeholder="email" type="email" required className=" w-full p-3 border rounded mb-4 focus:outline-none"/>
        <input placeholder="password" type="password" required className="w-full p-3 border rounded mb-4 focus:outline-none "/>
        <button className=" w-full py-3 bg-purple-600 text-white cursor-pointer rounded hover:bg-blue-600 transition-all duration-700" type="submit">Sign Up</button>
      </form>
      <p className=" mt-4 text-sm">Already have an account ? <a href="/login" className=" text-purple-600">Sign In</a></p>
     </div>
    </div>
  );
}

export default Signup;
