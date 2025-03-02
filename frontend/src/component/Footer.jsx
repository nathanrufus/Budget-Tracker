

import React from "react";

function Footer() {
  return (
    <footer className="bg-[#F7FAFD] py-10">
      <div className="container mx-auto text-center">
        <p className="font-Amatic_SC text-[20px] leading-[30px] text-[#838383]">
          &copy; 2025 BP. All Rights Reserved.
        </p>
        <nav className="flex justify-center space-x-5 mt-5">
          <a href="/privacy" className="text-[#6246E4]">
            Privacy Policy
          </a>
          <a href="/terms" className="text-[#6246E4]">
            Terms of Service
          </a>
        </nav>
      </div>
    </footer>
  );
};


export default Footer;
