from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import re
from database import get_connection, init_db

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)
init_db()

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
CONTACT_RE = re.compile(r"^[0-9]{10}$")

def student_dict(row):
    return dict(row)

def validate_student(data):
    required = ["name", "roll_no", "class_name", "marks", "contact", "email"]
    for field in required:
        if field not in data or str(data[field]).strip() == "":
            return f"{field} is required"
    name = str(data["name"]).strip()
    contact = str(data["contact"]).strip()
    email = str(data["email"]).strip()
    try:
        marks = float(data["marks"])
    except (TypeError, ValueError):
        return "Marks must be a valid number"
    if len(name) < 2:
        return "Name must contain at least 2 characters"
    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100"
    if not CONTACT_RE.fullmatch(contact):
        return "Contact must contain exactly 10 digits"
    if not EMAIL_RE.fullmatch(email):
        return "Enter a valid email address"
    return None

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.get("/api/students")
def get_students():
    conn = get_connection()
    rows = conn.execute("SELECT id, name, roll_no, class_name, marks, contact, email, created_at FROM students ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([student_dict(row) for row in rows])

@app.get("/api/students/search")
def search_students():
    query = request.args.get("q", "").strip()
    conn = get_connection()
    rows = conn.execute("SELECT id, name, roll_no, class_name, marks, contact, email, created_at FROM students WHERE name LIKE ? OR roll_no LIKE ? ORDER BY id DESC", (f"%{query}%", f"%{query}%")).fetchall()
    conn.close()
    return jsonify([student_dict(row) for row in rows])

@app.post("/api/students")
def add_student():
    data = request.get_json(silent=True) or {}
    error = validate_student(data)
    if error:
        return jsonify({"error": error}), 400
    conn = get_connection()
    try:
        cursor = conn.execute("INSERT INTO students (name, roll_no, class_name, marks, contact, email) VALUES (?, ?, ?, ?, ?, ?)", (str(data["name"]).strip(), str(data["roll_no"]).strip(), str(data["class_name"]).strip(), float(data["marks"]), str(data["contact"]).strip(), str(data["email"]).strip()))
        conn.commit()
        row = conn.execute("SELECT id, name, roll_no, class_name, marks, contact, email, created_at FROM students WHERE id = ?", (cursor.lastrowid,)).fetchone()
        return jsonify(student_dict(row)), 201
    except Exception as exc:
        conn.rollback()
        print("ERROR ADDING STUDENT:", repr(exc))
        if "UNIQUE constraint failed" in str(exc):
            return jsonify({"error": "Roll number already exists"}), 409
        return jsonify({"error": "Unable to add student"}), 500
    finally:
        conn.close()

@app.put("/api/students/<int:student_id>")
def update_student(student_id):
    data = request.get_json(silent=True) or {}
    error = validate_student(data)
    if error:
        return jsonify({"error": error}), 400
    conn = get_connection()
    try:
        if not conn.execute("SELECT id FROM students WHERE id = ?", (student_id,)).fetchone():
            return jsonify({"error": "Student not found"}), 404
        conn.execute("UPDATE students SET name = ?, roll_no = ?, class_name = ?, marks = ?, contact = ?, email = ? WHERE id = ?", (str(data["name"]).strip(), str(data["roll_no"]).strip(), str(data["class_name"]).strip(), float(data["marks"]), str(data["contact"]).strip(), str(data["email"]).strip(), student_id))
        conn.commit()
        row = conn.execute("SELECT id, name, roll_no, class_name, marks, contact, email, created_at FROM students WHERE id = ?", (student_id,)).fetchone()
        return jsonify(student_dict(row))
    except Exception as exc:
        conn.rollback()
        if "UNIQUE constraint failed" in str(exc):
            return jsonify({"error": "Roll number already exists"}), 409
        return jsonify({"error": "Unable to update student"}), 500
    finally:
        conn.close()

@app.delete("/api/students/<int:student_id>")
def delete_student(student_id):
    conn = get_connection()
    try:
        cursor = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404
        return jsonify({"message": "Student deleted successfully"})
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
