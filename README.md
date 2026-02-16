# 📝 Notes Management API

A secure RESTful Notes Management API built using **Django** and **Django REST Framework**, implementing **JWT authentication** for secure access.

This project allows users to register, login, and manage personal notes with features like archiving, searching, and pagination.

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- User Login (JWT Authentication)
- Protected note endpoints (only authenticated users can access)

### 📝 Notes Management
- Create Note
- List Notes (only notes owned by logged-in user)
- Retrieve Single Note
- Update Note
- Delete Note
- Archive Notes

### 🔎 Advanced Features
- Archived notes hidden by default
- Fetch archived notes using:  
  `GET /api/notes/?archived=true`
- Search notes using:  
  `GET /api/notes/?search=keyword`
- Pagination enabled
- Title validation (non-empty, max length 255)

---

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- Simple JWT (JWT Authentication)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/notes-management-api.git
cd notes-management-api
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Virtual Environment
Windows:

venv\Scripts\activate
Mac/Linux:

source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
6️⃣ Run Development Server
python manage.py runserver
Server runs at:

http://127.0.0.1:8000/
🔐 Authentication Endpoints
🧑 Register User
POST /api/register/
Body:

{
  "username": "user1",
  "password": "password123"
}
🔑 Login
POST /api/login/
Response:

{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
Use access token in header for protected routes:

Authorization: Bearer <access_token>
📝 Notes Endpoints
Create Note
POST /api/notes/
Body:

{
  "title": "My Note",
  "content": "This is my note"
}
List Notes
GET /api/notes/
Returns paginated response.

Retrieve Single Note
GET /api/notes/<id>/
Update Note
PUT /api/notes/<id>/
Delete Note
DELETE /api/notes/<id>/
🔎 Query Parameters
📦 Get Archived Notes
GET /api/notes/?archived=true
🔍 Search Notes
GET /api/notes/?search=keyword
Search works on both title and content fields.

📄 Pagination
Notes list is paginated using Django REST Framework pagination.
Default page size: 5 notes per page.

🧠 Design Decisions
JWT authentication used for stateless security.

Notes restricted to logged-in user using request.user.

perform_create() used to securely assign note ownership.

Custom serializer validation ensures title is not empty.

Q objects used for implementing flexible search functionality.

👩‍💻 Author
Developed as part of a backend development task using Django REST Framework.


---



