import React, { useState } from "react";

const API = "http://127.0.0.1:8000";

export default function App() {
  const [body, setBody] = useState("");
  const [textId, setTextId] = useState("");
  const [respId, setRespId] = useState("");
  const [out, setOut] = useState("Chưa có dữ liệu.");

  const pretty = (x) => JSON.stringify(x, null, 2);

  async function postInput() {
    try {
      setOut("Đang POST /input ...");
      const r = await fetch(`${API}/input`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ body }),
      });

      if (!r.ok) {
        const t = await r.text();
        setOut(`Lỗi POST: ${r.status}\n${t}`);
        return;
      }

      const data = await r.json();
      setOut(pretty(data));

      // tiện: tự điền id vào ô để test GET luôn
      if (data?.input?.id != null) setTextId(String(data.input.id));
      if (data?.output?.id != null) setRespId(String(data.output.id));
    } catch (e) {
      setOut(`Không gọi được API: ${String(e)}`);
    }
  }

  async function getInputById() {
    try {
      setOut(`Đang GET /get_input/${textId} ...`);
      const r = await fetch(`${API}/get_input/${textId}`);

      if (!r.ok) {
        const t = await r.text();
        setOut(`Lỗi GET input: ${r.status}\n${t}`);
        return;
      }

      const data = await r.json();
      setOut(pretty(data));
    } catch (e) {
      setOut(`Không gọi được API: ${String(e)}`);
    }
  }

  async function getResponseById() {
    try {
      setOut(`Đang GET /get_response/${respId} ...`);
      const r = await fetch(`${API}/get_response/${respId}`);

      if (!r.ok) {
        const t = await r.text();
        setOut(`Lỗi GET response: ${r.status}\n${t}`);
        return;
      }

      const data = await r.json();
      setOut(pretty(data));
    } catch (e) {
      setOut(`Không gọi được API: ${String(e)}`);
    }
  }

  return (
    <div style={{ fontFamily: "system-ui", maxWidth: 900, margin: "24px auto", padding: 12 }}>

      <section style={{ marginBottom: 24 }}>
        <h3>POST /input</h3>
        <textarea
          value={body}
          onChange={(e) => setBody(e.target.value)}
          rows={4}
          placeholder="Nhập body..."
          style={{ width: "100%", padding: 10 }}
        />
        <div style={{ marginTop: 8 }}>
          <button onClick={postInput}>Send POST</button>
        </div>
        <small>
        </small>
      </section>

      <section style={{ marginBottom: 24 }}>
        <h3>GET /get_input/{"{id}"}</h3>
        <input
          value={textId}
          onChange={(e) => setTextId(e.target.value)}
          placeholder="Text id"
          style={{ padding: 8, width: 200, marginRight: 8 }}
        />
        <button onClick={getInputById}>Get Input</button>
      </section>

      <section style={{ marginBottom: 24 }}>
        <h3>GET /get_response/{"{id}"}</h3>
        <input
          value={respId}
          onChange={(e) => setRespId(e.target.value)}
          placeholder="Response id"
          style={{ padding: 8, width: 200, marginRight: 8 }}
        />
        <button onClick={getResponseById}>Get Response</button>
      </section>
      <pre style={{ background: "#f6f6f6", padding: 12, borderRadius: 8, whiteSpace: "pre-wrap" }}>
        {out}
      </pre>
    </div>
  );
}
