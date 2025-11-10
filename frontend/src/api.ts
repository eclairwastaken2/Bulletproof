const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:5000/api"

export async function register(data: {username:string, email?:string, password:string}) {
  const res = await fetch(`${API_BASE}/register`, {
    method:"POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify(data)
  });
  return res.json();
}

export async function login(data:{username:string,password:string}) {
  const res = await fetch(`${API_BASE}/login`, {
    method:"POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify(data)
  });
  return res.json();
}

function authFetch(path:string, token?:string, opts: RequestInit = {}) {
  const headers = opts.headers ? new Headers(opts.headers as any) : new Headers();
  headers.set("Content-Type", "application/json");
  if (token) headers.set("Authorization", `Bearer ${token}`);
  return fetch(`${API_BASE}${path}`, {...opts, headers});
}

export async function fetchEntries(token: string) {
  const res = await authFetch("/entries", token, { method: "GET" });
  return res.json();
}

export async function createEntry(token: string, payload:{title:string, body:string}) {
  const res = await authFetch("/entries", token, { method: "POST", body: JSON.stringify(payload) });
  return res.json();
}

export async function updateEntry(token: string, id:string, payload:{title:string, body:string}) {
  const res = await authFetch(`/entries/${id}`, token, { method: "PUT", body: JSON.stringify(payload) });
  return res.json();
}

export async function deleteEntry(token: string, id:string) {
  const res = await authFetch(`/entries/${id}`, token, { method: "DELETE" });
  return res.json();
}

export async function getUserByUsername(username: string) {
  const res = await fetch(`${API_BASE}/users/${username}`);
  return res.json();
}