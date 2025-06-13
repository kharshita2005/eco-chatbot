import React, { useState } from "react";

const Login = ({ onLogin }: { onLogin: (email: string) => void }) => {
  const [email, setEmail] = useState("");

  const handleLogin = () => {
    if (email.trim()) {
      localStorage.setItem("ecochat_user", email);
      onLogin(email);
    }
  };

  return (
    <div className="p-4 flex flex-col items-center gap-4">
      <h2 className="text-xl font-bold">Eco ChatBot 🌿</h2>
      <input
        type="email"
        placeholder="Enter your email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="border rounded px-2 py-1 w-64"
      />
      <button onClick={handleLogin} className="bg-green-600 text-white px-4 py-1 rounded">
        Login
      </button>
    </div>
  );
};

export default Login;
