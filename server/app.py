from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)

# SQLite DB path
DB_PATH = "chatbot.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()

        # Table for storing chats
        c.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_reply TEXT,
            timestamp TEXT
        )
        """)

        # Table for mock products
        c.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            description TEXT
        )
        """)

        # Pre-populate 100 mock products
        c.execute("SELECT COUNT(*) FROM products")
        if c.fetchone()[0] == 0:
            for i in range(1, 101):
                c.execute("INSERT INTO products (name, category, description) VALUES (?, ?, ?)",
                          (f"Eco Product {i}", "general", f"This is a description for Eco Product {i}"))
            conn.commit()

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Chatbot logic
    if "eco" in user_message or "product" in user_message:
        reply = "We offer eco-friendly sustainable products like bamboo toothbrushes and reusable bags!"
    elif "gift" in user_message:
        reply = "Yes, we offer eco-friendly gift sets perfect for special occasions. 🎁"
    elif "delivery" in user_message or "carbon" in user_message:
        reply = "Absolutely! Our deliveries are 100% carbon-neutral 🌍."
    elif "recyclable" in user_message:
        reply = "Yes! Most of our packaging and products are recyclable and biodegradable."
    elif "organic" in user_message:
        reply = "Definitely! Many of our items use certified organic materials. 🌱"
    elif "discount" in user_message or "sale" in user_message:
        reply = "We run seasonal discounts. Stay tuned for our upcoming eco-sales!"
    elif "newsletter" in user_message or "subscribe" in user_message:
        reply = "Subscribe to our newsletter to get updates on green living and new products!"
    elif "return" in user_message or "policy" in user_message:
        reply = "We offer a 7-day easy return policy on all unused eco-products."
    elif "material" in user_message:
        reply = "Our products are made using bamboo, jute, recycled plastic, and other eco-friendly materials."
    elif "payment" in user_message:
        reply = "We accept all major payment methods including UPI, credit/debit cards, and net banking."
    elif "hello" in user_message or "hi" in user_message:
        reply = "Hello! 👋 How can I assist you with our green products today?"
    elif "search" in user_message or "find" in user_message:
        keyword = user_message.replace("search", "").replace("find", "").strip()
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("SELECT name FROM products WHERE name LIKE ? LIMIT 5", (f"%{keyword}%",))
            results = c.fetchall()
        if results:
            product_list = ", ".join([r[0] for r in results])
            reply = f"Here are some eco products matching your search: {product_list}"
        else:
            reply = "Sorry, no matching products found in our eco inventory."
    else:
        reply = "I'm your eco-assistant 🌿 Ask me about our sustainable products, green tips, or anything eco-friendly!"

    # Save chat to DB
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO chats (user_message, bot_reply, timestamp) VALUES (?, ?, ?)",
                  (user_message, reply, timestamp))
        conn.commit()

    return jsonify({"reply": reply, "timestamp": timestamp})

@app.route("/api/search", methods=["POST"])
def search():
    data = request.get_json()
    keyword = data.get("query", "").lower()
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT name, category, description FROM products WHERE name LIKE ? LIMIT 10", (f"%{keyword}%",))
        results = c.fetchall()
    formatted = [{"name": r[0], "category": r[1], "description": r[2]} for r in results]
    return jsonify({"results": formatted})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
