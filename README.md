# 🌱 Eco Chatbot

An **interactive sales chatbot system** built for an eco-friendly e-commerce platform. This project enhances the user shopping experience by enabling product exploration and smart conversations through a chatbot interface.

---

## 🎯 Objective

To design and implement a **user-centric chatbot system** that helps customers:
- Browse eco-friendly products
- Get product recommendations
- Simulate the shopping process
- Chat through a smooth, interactive UI

---

## 🌟 Key Features

- 💬 Chatbot interface with timestamped messages
- 🔐 User login with session-based authentication (Flask-Session)
- 📱 Responsive UI for mobile, tablet, and desktop
- 🗃 100+ eco-friendly product entries (SQLite-based inventory)
- 🔁 REST API communication between frontend and backend
- 🧹 Chat reset and session tracking functionality
- 💡 Clean, modular code with error handling

---

## 🛠️ Tech Stack

| Layer        | Technology                  |
|--------------|-----------------------------|
| Frontend     | Vite + React (JavaScript)   |
| Backend      | Python (Flask Framework)    |
| Database     | SQLite                      |
| Auth & State | Flask-Session               |

---

## 📁 Folder Structure

eco-chatbot/
├── client/ # Frontend (React + Vite)
│ ├── public/ # Static files (index.html, etc.)
│ └── src/
│ ├── assets/ # Images, CSS
│ ├── components/ # Reusable UI components
│ ├── pages/ # Page-level components (Login, Chat)
│ └── services/ # API and helper functions
│
├── server/ # Backend (Flask)
│ ├── app.py # Main Flask app
│ ├── models.py # SQLite database models
│ ├── inventory_seed.py# Seed script for products
│ └── requirements.txt # Python dependencies
│
├── docs/ # Documentation (PPT, Report, Screenshots)
└── README.md # This file


---

## ⚙️ Installation & Running Locally

### 1️⃣ Clone the Repository


git clone https://github.com/kharshita2005/eco-chatbot.git
cd eco-chatbot
2️⃣ Set up Virtual Environment (Backend)

cd server
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
python app.py  # Start Flask server
3️⃣ Start React Frontend

cd ../client
npm install
npm run dev
Visit http://localhost:5173 to view the chatbot UI.

🧾 Project Assets
All documentation is available in the /docs folder:

✅ Project Report (EcoChatbot_Project_Report.docx)

✅ Presentation Slides (EcoChatbot presentation.pdf)

✅ Screenshots of working chatbot

🙌 Final Note
This chatbot is designed to demonstrate:

Real-world user interaction

Backend integration with session handling

Modular and scalable architecture

UI/UX focused frontend

Made with 💚 for sustainability and innovation.


---








