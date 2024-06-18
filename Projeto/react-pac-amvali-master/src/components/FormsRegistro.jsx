import React, { useState } from "react";
import view_eye from "./assets/view.png";
import hide_eye from "./assets/hide.png";

function FormsRegistro() {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };

  const handleToggleConfirmPassword = () => {
    setShowConfirmPassword(!showConfirmPassword);
  };
  return (
    <form className="form" action="POST">
      <label>
        <input className="input" type="text" placeholder="" required />
        <span>Entidade...</span>
      </label>

      <label>
        <input className="input" type="email" placeholder="" required />
        <span>E-Mail...</span>
      </label>

      <label className="password-label">
        <input
          className="input"
          type={showPassword ? "text" : "password"}
          placeholder=""
          required
          id="password"
        />
        <span>Senha...</span>
        <img
          src={showPassword ? view_eye : hide_eye}
          alt="Esconder Senha"
          id="togglePassword"
          style={{ width: "30px", cursor: "pointer" }}
          onClick={handleTogglePassword}
        />
      </label>

      <label className="password-label">
        <input
          className="input"
          type={showConfirmPassword ? "text" : "password"}
          placeholder=""
          required
          id="confirmPassword"
        />
        <span>Confirmar Senha...</span>
        <img
          src={showConfirmPassword ? view_eye : hide_eye}
          alt="Esconder Senha"
          id="toggleConfirmPassword"
          style={{ width: "30px", cursor: "pointer" }}
          onClick={handleToggleConfirmPassword}
        />
      </label>
    </form>
  );
}

export default FormsRegistro;
