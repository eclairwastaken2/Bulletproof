import React from "react";
import { login, API_BASE } from "../api";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function AuthPage() {

  const nav = useNavigate();
  function handleLogin() {
    login();
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>Welcome</h2>

      <button onClick={handleLogin} style={{ padding: "10px 20px", fontSize: "16px" }}>
        Login / Register with AWS Cognito
      </button>
    </div>
  );
}