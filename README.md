# Eco ChatBot 🌱

An interactive sales chatbot system built for an eco-friendly e-commerce platform. This project enhances the user shopping experience by enabling product exploration and interaction through a smart, conversational chatbot UI. The backend handles product data queries and user authentication securely.

---

## 🌟 Objective

To design and implement a user-centric chatbot system that allows customers to browse eco-friendly products, get recommendations, and simulate the shopping process through an intuitive interface.

---

## 🚀 Key Features

- Interactive chatbot interface with message timestamps
- User login and session-based authentication using Flask-Session
- Responsive UI compatible with mobile, tablet, and desktop
- Backend server using Flask and SQLite for mock inventory
- 100+ eco-friendly product entries
- REST API communication between frontend and backend
- Chat reset and session tracking functionality
- Clean and modular code with proper error handling

---

## 🛠️ Tech Stack

| Layer        | Technology                   |
|--------------|------------------------------|
| Frontend     | Vite + React (JavaScript)    |
| Backend      | Python (Flask Framework)     |
| Database     | SQLite                       |
| Auth & State | Flask-Session                |

---

## 📁 Folder Structure

eco-chatbot/
├── client/ # Frontend Vite + React application
│ ├── public/ # Static assets like index.html
│ └── src/ # Source code for React app
│ ├── assets/ # Images, icons, etc.
│ ├── components/ # Reusable UI components
│ ├── pages/ # Main pages/screens
│ └── services/ # API calls or helper services
│
├── server/ # Backend Flask application
│ ├── chatbot.db
│ ├── inventory_seed.py
│ ├── app.py # Flask main app
│ ├── models.py # SQLite DB models
| |
│ └── requirements.txt
│
├── docs/ # Project documentation (optional)
└── README.md # Project overview


---

## 🔧 Installation & Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/kharshita2005/eco-chatbot.git
cd eco-chatbot

 set up virtual environment 
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

Install python dependencies
pip install -r requirements.txt


Run the flask backend
cd server
python app.py


Start the react frontend
cd ../client
npm install
npm run dev

Visit: http://localhost:5173 to use the app