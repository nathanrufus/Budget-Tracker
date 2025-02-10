import React, { useState } from "react";
import { FaBars, FaTimes } from "react-icons/fa";

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  // Navigation items
  const navItems = [
    { name: "Home", href: "#home" },
    { name: "About", href: "#about" },
    { name: "Our Services", href: "#services" },
    { name: "Contact Us", href: "#contact" },
  ];

  return (
    <nav className=" bg-blue-100 p-4 fixed w-full z-50">
      <div className="container mx-auto flex items-center justify-between">
        {/* Logo */}
        <h1 className="text-2xl font-serif font-extrabold text-gray-800 tracking-wider italic">
          <span className="text-black">B</span>
          <span className="text-red-500">T</span>
        </h1>


        {/* Menu for larger screens */}
        <ul className="hidden md:flex space-x-8 text-gray-800">
          {navItems.map((item) => (
            <li
              key={item.name}
              className="relative group"
            >
              <a
                href={item.href}
                className="hover:text-purple-600 transition duration-300"
              >
                {item.name}
              </a>
              <div className="absolute top-[-1.5rem] left-0 w-full h-1 bg-purple-600 scale-x-0 group-hover:scale-x-100 transform origin-left transition-transform duration-300"></div>
            </li>
          ))}
        </ul>


        {/* Buttons */}
        <div className="hidden md:flex space-x-4">
          <button className="px-4 py-2 border border-gray-800 text-gray-800 rounded hover:bg-gray-200">
            Sign In
          </button>
          <button className="px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700">
            Sign Up
          </button>
        </div>

        {/* Hamburger Menu Icon for small devices */}
        <div
          className="md:hidden text-gray-800 text-2xl cursor-pointer"
          onClick={() => setMenuOpen(!menuOpen)}
        >
          {menuOpen ? <FaTimes /> : <FaBars />}
        </div>
      </div>

      {/* Mobile Menu */}
      {menuOpen && (
        <ul className="absolute top-full left-0 w-full bg-white shadow-lg p-4 space-y-4 text-gray-800 text-center rounded">
          {navItems.map((item) => (
            <li key={item.name}>
              <a href={item.href} className="block hover:text-purple-600">
                {item.name}
              </a>
            </li>
          ))}
          <li className="mt-4">
            <button className="w-full px-4 py-2 border border-gray-800 text-gray-800 rounded hover:bg-gray-200">
              Sign In
            </button>
          </li>
          <li>
            <button className="w-full px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700">
              Sign Up
            </button>
          </li>
        </ul>
      )}

    </nav>
  );
}

export default Navbar;
