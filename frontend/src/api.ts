export const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:5000"

export function login() {
  window.location.href = `${API_BASE}/auth/login`; 
}

export function logout() {
  window.location.href = `${API_BASE}/auth/logout`; 
}

function authFetch(path:string, opts: RequestInit = {}) {
  return fetch(`${API_BASE}${path}`, {
    ...opts,
    credentials: "include", 
    headers: {
      "Content-Type": "application/json",
      ...(opts.headers || {})
    }, 
  }); 
}

export async function fetchAuthorize() {
  const res = await fetch(`${API_BASE}/auth/authorize`, {
    credentials: "include",
  });
  return res.json();
}



export async function fetchEntries() {
  const res = await authFetch("/api/entries", {
    method: "GET",
  });
  return res.json();
}

export async function createEntry(payload: { title: string; body: string }) {
  const res = await authFetch("/api/entries", {
    method: "POST",
    body: JSON.stringify(payload),
  });
  return res.json();
}

export async function updateEntry(id: string, payload: { title: string; body: string }) {
  const res = await authFetch(`/api/entries/${id}`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
  return res.json();
}

export async function deleteEntry(id: string) {
  const res = await authFetch(`/api/entries/${id}`, {
    method: "DELETE",
  });
  return res.json();
}

export async function getUserByUsername(username: string) {
  const res = await fetch(`${API_BASE}/users/${username}`, {
    credentials: "include", // << optional but recommended for consistency
  });
  return res.json();
}