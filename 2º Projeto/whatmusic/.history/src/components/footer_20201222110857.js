import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <div className="main-footer">
      <div className="container">
          <p className="col-sm">
            &copy;{new Date().getFullYear()} | SBS
          </p>
      </div>
    </div>
  );
}

export default Footer;