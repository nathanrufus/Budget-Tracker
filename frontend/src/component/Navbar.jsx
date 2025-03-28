import React, { useState } from "react";
import { FaBars, FaTimes } from "react-icons/fa";
import { Link } from "react-router-dom";

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  // Navigation items
  const navItems = [
    { name: "Home", path: "/" },
    { name: "Our Services", path: "/services" },
    { name: "Contact Us", path: "/contact" },
  ];

  return (
    <nav className="bg-blue-100 p-4 fixed top-0 left-0 right-0 w-full z-50">
      <div className="container mx-auto flex items-center justify-between">
        {/* Logo */}
        <h1 className="text-2xl font-serif font-extrabold text-gray-800 tracking-wider italic">
          <span className="text-black">B</span>
          <span className="text-red-500">T</span>
        </h1>

        {/* Desktop Menu */}
        <ul className="hidden md:flex space-x-8 text-gray-800">
          {navItems.map(({ name, path }) => (
            <li key={name} className="relative group">
              <Link
                to={path}
                className="hover:text-purple-600 transition duration-300"
              >
                {name}
              </Link>
              <div className="absolute top-[-1.5rem] left-0 w-full h-1 bg-purple-600 scale-x-0 group-hover:scale-x-100 transform origin-left transition-transform duration-300"></div>
            </li>
          ))}
        </ul>

        {/* Desktop Buttons */}
        <div className="hidden md:flex space-x-4">
          <Link to="/signin">
            <button className="px-4 py-2 border border-gray-800 text-gray-800 rounded hover:bg-gray-200">
              Sign In
            </button>
          </Link>
          <Link to="/signup">
            <button className="px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700">
              Sign Up
            </button>
          </Link>
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden text-gray-800 text-2xl cursor-pointer"
          onClick={() => setMenuOpen((prev) => !prev)}
          aria-label="Toggle menu"
        >
          {menuOpen ? <FaTimes /> : <FaBars />}
        </button>
      </div>

      {/* Mobile Menu */}
      {menuOpen && (
        <ul className="absolute top-full left-0 w-full bg-white shadow-lg p-4 space-y-4 text-gray-800 text-center rounded ">
          {navItems.map(({ name, path }) => (
            <li key={name}>
              <Link
                to={path}
                className="block hover:text-purple-600"
                onClick={() => setMenuOpen(false)}
              >
                {name}
              </Link>
            </li>
          ))}
          <li className="mt-4">
            <Link to="/signin">
              <button
                className="w-full px-4 py-2 border border-gray-800 text-gray-800 rounded hover:bg-gray-200"
                onClick={() => setMenuOpen(false)}
              >
                Sign In
              </button>
            </Link>
          </li>
          <li>
            <Link to="/signup">
              <button
                className="w-full px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700"
                onClick={() => setMenuOpen(false)}
              >
                Sign Up
              </button>
            </Link>
          </li>
        </ul>
      )}
    </nav>
  );
}
export default Navbar;


