import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Helmet } from "react-helmet";
import HeaderLogin from "../components/HeaderLogin";
import FormsRegistro from "../components/FormsRegistro";
import HalfImage from "../components/HalfImage";

function Registro() {
  const [showPassword, setShowPassword] = useState(false);

  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };
  return (
    <div className="main-login">
      <Helmet bodyAttributes={{ style: "background-color : #F8C401" }} />
      <HeaderLogin />
      <div className="card-principal-login">
        <div id="card" className="card-login">
          <div className="half1">
            <div className="title-login">
              <h1>CADASTRE-SE COM A PERMISSÃO DA AMVALI</h1>
            </div>
            <FormsRegistro showPassword={showPassword} handleTogglePassword={handleTogglePassword} />
            <div className="submit">
              <div className="enter-button">
                <button>CADASTRAR-SE</button>
              </div>
              <div className="forgot-pass">
                <p id="account">
                  Já possui uma conta? <Link to="../Login">Entre agora.</Link>
                </p>
              </div>
            </div>
          </div>
          <HalfImage />
        </div>
      </div>
    </div>
  );
}

export default Registro;
