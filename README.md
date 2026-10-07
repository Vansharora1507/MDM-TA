# Student Management System

A full-stack CRUD web application for managing student records using **HTML, CSS, JavaScript, Python Flask, and SQLite**.

## 📌 Project Overview

The Student Management System provides a simple and interactive web interface for managing student information. Users can add, view, search, update, and delete student records. The frontend communicates with the Flask backend using RESTful APIs and JSON, while SQLite provides persistent data storage.

## ✨ Features

- Add student records
- View all student records
- Search by name or roll number
- Update student details
- Delete student records
- Duplicate roll-number validation
- Marks, contact and email validation
- SQLite persistent storage
- RESTful GET, POST, PUT and DELETE APIs
- Dynamic updates using JavaScript Fetch API
- Responsive user interface

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Flask, Flask-CORS
- **Database:** SQLite and SQL
- **API:** RESTful API
- **Data Format:** JSON
- **Communication:** JavaScript Fetch API
- **Tools:** Visual Studio Code, Git, GitHub, Node.js

## 📁 Project Structure

```text
studentmanagementsystemmdm/
│
├── backend/
│   ├── app.py
│   └── database.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── schema.sql
├── package.json
├── requirements.txt
├── README.md
└── .gitignore
```

## 📋 Requirements

- Python 3
- Node.js and npm
- Git

## ▶️ Run on macOS/Linux

Open Terminal in the project folder:

```bash
cd studentmanagementsystemmdm
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 backend/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

The SQLite database is created automatically when the application is run for the first time.

## 🔄 CRUD Operations

| Operation | HTTP Method | Description |
|---|---|---|
| Create | POST | Add a new student |
| Read | GET | Retrieve student records |
| Update | PUT | Update student information |
| Delete | DELETE | Delete a student record |

## 🔌 API Endpoints

- `GET /api/students`
- `GET /api/students/search?q=...`
- `POST /api/students`
- `PUT /api/students/<id>`
- `DELETE /api/students/<id>`

## 📝 Example JSON

```json
{
  "name": "Rahul Sharma",
  "roll_no": "ECS101",
  "class_name": "ENCS-B",
  "marks": 87.5,
  "contact": "9876543210",
  "email": "rahul@example.com"
}
```

## 🗄️ Database

The application uses SQLite for persistent storage. The database schema is also provided separately in `schema.sql`. The Flask application automatically creates the database and `students` table when it starts.

## 🧪 Validation and Error Handling

The application handles missing fields, duplicate roll numbers, invalid email addresses, invalid 10-digit contact numbers, marks outside 0–100, invalid student IDs, and attempts to update or delete non-existing records.

## 🏗️ System Architecture

```text
Frontend (HTML / CSS / JavaScript)
              │
        Fetch API / JSON
              ▼
       Flask REST API
              │
          SQL Queries
              ▼
        SQLite Database
```

## 🎯 Project Objectives

- Develop a functional full-stack web application.
- Implement CRUD operations using RESTful APIs.
- Integrate Flask with an SQLite database.
- Use JavaScript Fetch API for frontend-backend communication.
- Implement input validation and error handling.
- Demonstrate SQL database operations.

## 👨‍💻 Author

**Vansh Arora**  
B.Tech Electronics and Computer Science

## 📄 License

This project was developed for academic and educational purposes.
# MDM-TA
# MDM-TA
