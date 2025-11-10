import React, { useState } from "react";
import { login, register } from "../api";
import { useNavigate } from "react-router-dom";

export default function AuthPage(){
  const [isRegister, setIsRegister] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const nav = useNavigate();

  async function submit(e:React.FormEvent){
    e.preventDefault();
    const fn = isRegister ? register : login;
    const res = await fn({username, password});
    if (res.token) {
      localStorage.setItem("bj_token", res.token);
      localStorage.setItem("bj_username", res.username);
      nav(`/${res.username}`);
    } else {
      alert(res.error || JSON.stringify(res));
    }
  }

  return (
    <div style={{padding:20}}>
      <h2>{isRegister ? "Register" : "Login"}</h2>
      <form onSubmit={submit}>
        <input placeholder="username" value={username} onChange={e=>setUsername(e.target.value)} />
        <input type="password" placeholder="password" value={password} onChange={e=>setPassword(e.target.value)} />
        <button type="submit">{isRegister ? "Register" : "Login"}</button>
      </form>
      <button onClick={()=>setIsRegister(v=>!v)}>{isRegister ? "Have an account? Log in" : "No account? Register"}</button>
    </div>
  );
}