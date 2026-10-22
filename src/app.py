import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    # ❌ VULNERABLE: Direct string formatting allows SQL Injection
    user_id = request.args.get("id")
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # CodeQL will flag this line as a security vulnerability
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    
    return cursor.fetchall()

if __name__ == "__main__":
    app.run(permanent=False)
