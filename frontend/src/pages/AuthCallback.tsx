import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { fetchAuthorize } from "../api";

export default function AuthCallback() {
  const nav = useNavigate();

  useEffect(() => {
    async function handleAuth() {
      const data = await fetchAuthorize();
      if (data.username) {
        nav(`/${data.username}`); // redirect inside React
      } else {
        alert("Login failed");
      }
    }
    handleAuth();
  }, [nav]);

  return <div>Logging in...</div>;
}
