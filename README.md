# 🛡️ SQL Injection Account Balance Lab

> **A hands-on cybersecurity lab demonstrating SQL Injection using a vulnerable application and its secure implementation with parameterized queries.**

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![License](https://img.shields.io/badge/License-Educational-green)

---

## 📖 Overview

This project demonstrates one of the **OWASP Top 10** vulnerabilities—**SQL Injection**.

The application contains **two implementations**:

- 🔴 **Vulnerable Version** – Uses dynamic SQL queries, allowing SQL Injection.
- 🟢 **Secure Version** – Uses prepared statements (parameterized queries) to prevent SQL Injection.

The objective is to understand:

- How SQL Injection works
- How attackers exploit vulnerable applications
- How prepared statements completely eliminate this vulnerability

---

# 📂 Project Structure

```
sql-injection-account-lab/
│
├── app.py                  # Flask Application
├── Dockerfile              # Docker Image Configuration
├── docker-compose.yml      # Docker Compose Configuration
├── requirements.txt        # Python Dependencies
├── database.db             # SQLite Database (Created Automatically)
│
├── templates/
│   ├── index.html          # Home Page
│   └── result.html         # Result Page
│
└── README.md
```

---

# 🚀 Features

✅ Search Account Balance

✅ Demonstrate SQL Injection Attack

✅ Demonstrate SQL Injection Prevention

✅ Dockerized Application

✅ SQLite Database

✅ Flask Web Application

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| SQLite | Database |
| Docker | Containerization |
| HTML | Frontend |

---

# ⚙️ Prerequisites

Install:

- Docker
- Docker Compose

Verify installation

```bash
docker --version
docker compose version
```

---

# ▶️ Running the Project

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/sql-injection-account-lab.git
```

Move into the project

```bash
cd sql-injection-account-lab
```

---

## Build Docker Image

```bash
docker compose up --build
```

Docker will automatically:

- Build the image
- Install dependencies
- Create the SQLite database
- Start Flask Server

---

## Open Browser

```
http://localhost:5000
```

---

# 🧪 Testing the Application

## ✅ Normal Test

Input

```
1001
```

Expected Output

```
Account Number : 1001

Account Holder : Karan

Balance : ₹25,000
```

---

# 🔴 SQL Injection Attack

Open

```
http://localhost:5000/vulnerable
```

Enter

```sql
' UNION SELECT user_id, password, 0 FROM users --
```

Expected Output

```
admin
admin@123

karan
karan123

testuser
testpass
```

---

## Generated Vulnerable Query

```sql
SELECT account_no, holder_name, balance
FROM accounts
WHERE account_no=''
UNION
SELECT user_id,password,0
FROM users --'
```

Because user input becomes part of the SQL statement, the attacker can retrieve sensitive information.

---

# 🟢 SQL Injection Prevention

Open

```
http://localhost:5000/secure
```

Use the same payload

```sql
' UNION SELECT user_id, password, 0 FROM users --
```

Expected Output

```
No records found.
```

---

## Secure Query

```python
conn.execute(
    "SELECT account_no, holder_name, balance FROM accounts WHERE account_no=?",
    (account_no,)
)
```

Prepared statements separate **SQL code** from **user input**, preventing SQL Injection attacks.

---

# 🐳 Docker Commands

Build and Run

```bash
docker compose up --build
```

Run in Background

```bash
docker compose up -d
```

View Logs

```bash
docker compose logs -f
```

Stop Containers

```bash
docker compose down
```

Rebuild Image

```bash
docker compose up --build
```

---

# 📸 Demo

## Normal User

```
Input:
1001

↓

Account Found

Account Holder

Balance
```

---

## Attacker

```
Payload

↓

UNION Injection

↓

User IDs + Passwords Displayed
```

---

## Secure Version

```
Payload

↓

Prepared Statement

↓

No Records Found
```

---

# 🔒 Learning Outcomes

After completing this lab, you will understand:

- SQL Injection
- UNION-based SQL Injection
- Vulnerable SQL Queries
- Prepared Statements
- Parameterized Queries
- Secure Database Programming
- Dockerized Web Applications

---

# 📚 OWASP Mapping

This project demonstrates:

- OWASP Top 10
- Injection Vulnerabilities
- SQL Injection
- Secure Coding Practices

---

# 📌 Future Improvements

- MySQL Support
- PostgreSQL Support
- Login Authentication
- Blind SQL Injection Demo
- Error-based SQL Injection Demo
- Time-based SQL Injection Demo
- Docker Hub Image
- GitHub Actions CI/CD

---

# 👨‍💻 Author

**Karan Satpute**

Computer Engineering Student

Cyber Security | DevOps | Cloud Computing

GitHub: https://github.com/YOUR_USERNAME

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share it with others

---

## ⚠️ Disclaimer

This project is created **strictly for educational purposes** to demonstrate SQL Injection vulnerabilities and their prevention.

Do **NOT** deploy this application in a production environment or use these techniques against systems without explicit authorization.

Unauthorized testing or exploitation of computer systems is illegal and unethical.
