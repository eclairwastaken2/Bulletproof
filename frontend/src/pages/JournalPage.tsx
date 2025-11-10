import React, { useEffect, useState } from "react";
import { fetchEntries, createEntry, updateEntry, deleteEntry, getUserByUsername } from "../api";
import EntryBox from "../components/EntryBox";
import { useParams } from "react-router-dom";

export default function JournalPage(){
  const { username } = useParams();
  const [entries, setEntries] = useState<any[]>([]);
  const [token, setToken] = useState<string | null>(null);

  useEffect(()=>{
    const t = localStorage.getItem("bj_token");
    setToken(t);
    if (!t) return;
    fetchEntries(t).then((data:any)=>setEntries(data));
  }, [username]);

  async function add() {
    if (!token) return alert("login first");
    const res = await createEntry(token, {title:"New note", body:""});
    setEntries(prev=>[res, ...prev]);
  }

  return (
    <div style={{padding:20}}>
      <h1>{username}'s Journal</h1>
      <button onClick={add}>Add Entry</button>
      <div style={{marginTop:20, display:"grid", gap:12}}>
        {entries.map(e => <EntryBox key={e.id} entry={e} onUpdate={async (u)=>{ await updateEntry(token!, e.id, u); setEntries(es=>es.map(x=>x.id===e.id?{...x,...u}:x)) }} onDelete={async ()=>{ await deleteEntry(token!, e.id); setEntries(es=>es.filter(x=>x.id!==e.id)) }} />)}
      </div>
    </div>
  );
}