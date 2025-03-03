import React from "react";

function Login() {
  return <div className=" container mt-20 min-h-screen flex items-center justify-center bg to-white align justify content-center">
  
    <div className=" w-full max-w-sm shadow-lg p-8 bg-gray-100">
      <h1 className="text-center text-2xl font-bold text-purple-600 mb-5"> Sign In</h1>
      <form>
        <input placeholder="email" type="email" required className=" w-full p-3 border rounded mb-4 focus:outline-none"/>
        <input placeholder="password" type="password" required className="w-full p-3 border rounded mb-4 focus:outline-none "/>
        <button className=" w-full py-3 bg-purple-600 text-white cursor-pointer rounded hover:bg-blue-600 transition-all duration-700" type="submit">Sign In</button>
      </form>

      <p className=" mt-4 text-sm text-center">Dont have an account ? <a href="/signup" className=" text-purple-600">Sign Up</a></p>

    </div>
  </div>;
}

export default Login;
