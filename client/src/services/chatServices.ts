const API_URL = "http://localhost:5000/api/chat"; // Update if backend uses a different port or endpoint

export const sendMessageToBot = async (message: string): Promise<string> => {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();
    return data.reply;
  } catch (error) {
    console.error("Error contacting chatbot API:", error);
    return "Something went wrong. Please try again.";
  }
};
