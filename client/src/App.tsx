import React, { useState, useEffect, useRef } from "react";
import { sendMessageToBackend } from "./services/api";
import Login from "./Login";

const App = () => {
  const [email, setEmail] = useState(localStorage.getItem("ecochat_user") || "");
  const [messages, setMessages] = useState<{ text: string; type: "user" | "bot"; time: string }[]>([]);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const time = new Date().toLocaleString();
    const userMsg = { text: input, type: "user" as const, time };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");

    const reply = await sendMessageToBackend(input);
    const botMsg = { text: reply, type: "bot" as const, time: new Date().toLocaleString() };
    setMessages((prev) => [...prev, botMsg]);

    const history = JSON.parse(localStorage.getItem("ecochat_history") || "[]");
    localStorage.setItem(
      "ecochat_history",
      JSON.stringify([...history, { user: email, session: [...messages, userMsg, botMsg] }])
    );
  };

  const handleLogout = () => {
    localStorage.removeItem("ecochat_user");
    localStorage.removeItem("ecochat_history");
    window.location.reload();
  };

  const handleReset = () => {
    setMessages([]);
    localStorage.removeItem("ecochat_history");
  };

  if (!email) return <Login onLogin={setEmail} />;

  return (
    <div className="min-h-screen bg-cover bg-center bg-fixed px-4 py-8 font-sans" style={{ backgroundImage: "url('/eco-bg.jpg')" }}>
      <div className="w-full max-w-xl mx-auto bg-white bg-opacity-90 backdrop-blur-sm rounded-2xl shadow-xl p-6 relative flex flex-col h-[90vh]">
        {/* Logout Button */}
        <button
          onClick={handleLogout}
          className="absolute top-4 right-4 bg-red-500 hover:bg-red-600 text-white px-4 py-2 text-sm rounded-lg"
        >
          Logout
        </button>

        {/* Header */}
        <h1 className="text-3xl font-bold text-center text-green-700 mb-4">Eco ChatBot 🌿</h1>

        {/* Chat Messages */}
        <div className="flex-1 overflow-y-auto space-y-3 p-3 border rounded bg-gray-100">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`max-w-[75%] px-5 py-3 rounded-xl text-sm whitespace-pre-wrap shadow-sm ${
                msg.type === "user"
                  ? "ml-auto bg-green-500 text-white text-right"
                  : "mr-auto bg-gray-200 text-gray-800 text-left"
              }`}
            >
              <p>{msg.text}</p>
              <p className="text-[10px] mt-1 opacity-60">{msg.time}</p>
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="mt-4 flex gap-2">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            placeholder="Ask me something..."
            className="flex-1 border rounded-xl px-4 py-3 text-base focus:outline-none focus:ring-2 focus:ring-green-400"
          />
          <button
            onClick={handleSend}
            className="bg-green-600 hover:bg-green-700 text-white px-5 py-3 rounded-xl text-base"
          >
            Send
          </button>
          <button
            onClick={handleReset}
            className="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-3 rounded-xl text-base"
          >
            Reset
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
