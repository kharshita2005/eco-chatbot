import { useState } from "react";
import { sendMessageToBackend } from "../services/api";

const ChatBot = () => {
  const [messages, setMessages] = useState<{ sender: string; text: string }[]>([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    const botReply = await sendMessageToBackend(input);
    const botMessage = { sender: "bot", text: botReply };
    setMessages((prev) => [...prev, botMessage]);
  };

  return (
    <div className="p-4 border rounded-lg shadow-md max-w-md mx-auto mt-10 bg-white">
      <h2 className="text-xl font-bold mb-4">Eco ChatBot 🌿</h2>
      <div className="h-64 overflow-y-auto border p-2 mb-4 bg-gray-50 rounded">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`mb-2 p-2 rounded ${
              msg.sender === "user" ? "bg-green-100 text-right" : "bg-blue-100 text-left"
            }`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 border rounded-l px-4 py-2"
          placeholder="Ask me something..."
        />
        <button
          onClick={handleSend}
          className="bg-green-600 text-white px-4 py-2 rounded-r"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBot;
