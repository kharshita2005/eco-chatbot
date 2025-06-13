export const sendMessageToBackend = async (message: string): Promise<string> => {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }

    const data = await response.json();
    return data.reply;
  } catch (error) {
    console.error("Error sending message:", error);
    return "❌ Oops! Couldn’t connect to the server. Please ensure it's running.";
  }
};
