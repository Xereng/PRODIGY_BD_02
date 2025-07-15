# 🧠 Prodigy Task 2 - User Management REST API (Database Version)

This Django project is a REST-style backend API built for the **Prodigy Backend Internship - Task 2**. It allows performing full CRUD operations on a `User` resource with persistent storage using Django ORM and proper input validation.

---

## 🚀 Features

* Create, Read, Update, Delete users
* UUID-based user IDs
* Email and input validation
* Persistent storage via SQLite (or PostgreSQL)
* Admin panel to manage users
* Uses `.env` for configuration (secret key, DB engine, etc.)
* Clean architecture with app structure

---

## 📁 Project Structure

```
BD_task2/
├── BD_task2/              # Project-level config
├── user_details/          # App for user management
├── .env                   # Secret keys and DB config (not committed)
├── db.sqlite3             # SQLite database (ignored by Git)
├── manage.py              # Django's CLI utility
└── requirements.txt       # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Xereng/PRODIGY_BD_02.git
cd PRODIGY_BD_02
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
# or
source .venv/bin/activate     # On Linux/macOS
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file in root directory

```
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the server

```bash
python manage.py runserver
```

### 7. (Optional) Create admin user

```bash
python manage.py createsuperuser
```

---

## 📢 API Endpoints

| Method | Endpoint           | Description    |
| ------ | ------------------ | -------------- |
| POST   | `/`                | Create user    |
| GET    | `/api/users/`      | List all users |
| GET    | `/api/users/<id>/` | Retrieve user  |
| PUT    | `/api/users/<id>/` | Update user    |
| DELETE | `/api/users/<id>/` | Delete user    |

> All data should be sent in JSON format.

---

## 📄 Example Request Body (POST/PUT)

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 25
}
```

---

## 👤 Admin Panel Access

* URL: `http://localhost:8000/admin/`
* Use your superuser credentials created via `createsuperuser`

---

## 🚜 Deployment Notes

* Keep `.env` and `db.sqlite3` excluded from Git via `.gitignore`
* Can be deployed to platforms like Heroku or Railway
* For production, switch to PostgreSQL and configure `.env`

---

## 📅 Tech Stack

* Python 3.11+
* Django 5+
* SQLite / PostgreSQL
* Environment config via `python-dotenv`

---

## 📚 License

This project is part of a backend internship task at Prodigy InfoTech and is intended for learning and demonstration purposes only.
