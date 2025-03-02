import React from "react";
import Home from "./Home";
import Services from "./Services";
import Access from "./Access";
import Contact from "./Contact";
// import Testimonials from "./Testimonials";
import Footer from "./Footer";

function Dashboard() {
  return <div>
    <Home/>
    <Services/>
    {/* <Testimonials/> */}
    <Access/>
    <Contact/>
    <Footer/>
  </div>;
}

export default Dashboard;
