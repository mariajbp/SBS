import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <div className="main-footer">
      <div className="container">
          <p className="col-sm">
          Sistemas Baseados em Similaridade | &copy;{new Date().getFullYear()} 
          </p>
      </div>
    </div>
  );
}

export default Footer;