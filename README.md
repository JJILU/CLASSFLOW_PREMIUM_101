# 🏫 CLASSFLOW — Classroom Management System

**ClassFlow** is a web-based **Classroom Management System** built with **Flask**, designed to streamline class operations such as **attendance tracking**, **grading**, and **assignment management**.  
It provides role-based access for **Admins**, **Teachers**, and **Students**, allowing seamless management and viewing of classroom activities.

---

## 🚀 Features

### 👩‍🏫 For Admins
- Create and manage **teacher** and **student** accounts.  
- Assign teachers to specific **classes** (e.g., 10A, 10B, 10C, 11A, 11B, 11C, 12A, 12B, 12C).  
- View all attendance and grading records.  
- Manage assignments and performance reports.

### 📚 For Teachers
- Mark **attendance** for students in their assigned classes.  
- Assign **grades** and **assignments** to students.  
- View and update class records.  
- Manage multiple classes and track progress.

### 👨‍🎓 For Students
- Log in securely to view **personal attendance**, **grades**, and **assignments**.  
- Access class-specific details depending on enrollment (e.g., Class 10A, 11B, etc.).  
- Stay updated on recent assignments and performance.

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Flask (Python) |
| **Database** | SQLite / MySQL (via SQLAlchemy) |
| **Frontend** | HTML, CSS, Jinja Templates (No JavaScript) |
| **Authentication** | Flask-Login / Flask-Security |
| **Email Support** | Flask-Mail (optional for notifications) |
| **Environment Management** | python-dotenv |

---

## 📁 Project Structure

flask_app/
│
├── app/
│ ├── init.py
│ ├── extensions.py
│ ├── auth/
│ │ ├── routes.py
│ │ ├── models.py
│ │ └── templates/
│ ├── dashboard/
│ │ ├── routes.py
│ │ ├── models.py
│ │ └── templates/
│ ├── records/
│ │ ├── routes.py
│ │ ├── models.py
│ │ └── templates/
│ ├── privacy/
│ │ ├── routes.py
│ │ ├── models.py
│ │ └── templates/
│ └── templates/
│ └── base.html
│
├── .env
├── .gitignore
├── .venv/
├── requirements.txt
├── config.py
├── run.py
└── README.md


---


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
<!-- ```bash -->
- git clone https://github.com/your-username/classflow.git
cd classflow

### 2️⃣ Create a Virtual Environment
- python -m venv .venv
- source .venv/bin/activate       # For Linux/Mac
- .venv\Scripts\activate          # For Windows

### 3️⃣ Install Dependencies
- pip install -r requirements.txt

### 4️⃣ Configure Environment Variables
- FLASK_ENV=development
- SECRET_KEY=your_secret_key
- SQLALCHEMY_DATABASE_URI=sqlite:///classflow.db

### 5️⃣ Initialize Database
- flask db init
- flask db migrate -m "Initial migration"
- flask db upgrade

### 6️⃣ Run the App
- flask run

- Then visit:
👉 http://127.0.0.1:5001



# 🧑‍💻 User Roles Summary
| Role | Permissions |
|------|-------------|
| **Admin** | Create/manage users, view all records |
| **Teacher** | Mark attendance, assign grades & assignments |
| **Student** | View grades, assignments, and attendance |


# 🛡️ Security
- Passwords are hashed using SHA-256 or Werkzeug’s built-in hasher.
- Role-based access control ensures safe and organized permissions.
- Sensitive keys and credentials are stored securely in .env.



# 📄 License
- This project is open-source and available under the MIT License.


# 💡 Future Improvements
- Add automated email notifications for new assignments.
- Include data visualization charts for teachers and admins.
- Integrate REST API for mobile app support.



# 🧠 Developer Notes

- This project was created for educational and demonstration purposes — ideal for schools or institutions looking to digitize classroom operations using a clean, simple Flask architecture.


# Developed with ❤️ using Flask and Jinja2

---

- Would you like me to include a **screenshot section** and placeholder image links (e.g. `/static/assets/screenshots/dashboard.png`) so it looks more polished on GitHub?



