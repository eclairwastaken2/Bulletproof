import React from "react";
import { login, API_BASE } from "../api";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function AuthPage() {

  const nav = useNavigate();

  useEffect(() => {
    async function handleAuth() {
      const res = await fetch(`${API_BASE}/auth/authorize`, {
        credentials: "include" // send Flask session cookies
      });
      const data = await res.json();
      if (data.username) {
        nav(`/${data.username}`);
      } else {
        alert("Login failed");
      }
    }
    handleAuth();
  }, [nav]);

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