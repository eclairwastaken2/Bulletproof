import React, { useState } from "react";

export default function EntryBox({entry, onUpdate, onDelete}:{entry:any, onUpdate: (u:{title:string, body:string})=>Promise<any>, onDelete: ()=>Promise<any>}){
  const [title, setTitle] = useState(entry.title);
  const [body, setBody] = useState(entry.body || "");
  return (
    <div style={{border:"1px solid #ddd", padding:12, borderRadius:8}}>
      <input value={title} onChange={e=>setTitle(e.target.value)} onBlur={()=>onUpdate({title, body})} />
      <textarea value={body} onChange={e=>setBody(e.target.value)} onBlur={()=>onUpdate({title, body})} style={{width:"100%", minHeight:80}} />
      <div style={{display:"flex", justifyContent:"space-between"}}>
        <small>{new Date(entry.created_at).toLocaleString()}</small>
        <button onClick={onDelete}>Delete</button>
      </div>
    </div>
  );
}