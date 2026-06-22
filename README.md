# 🛡️ SQL Injection Demo Lab

> An educational cybersecurity lab demonstrating **SQL Injection (UNION Attack)** and its **prevention using parameterized queries (Prepared Statements)**.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

This project is designed for students and cybersecurity beginners to understand:

- ✅ How SQL Injection works
- ✅ How attackers exploit vulnerable SQL queries
- ✅ How sensitive data can be exposed
- ✅ How Prepared Statements prevent SQL Injection
- ✅ How to run secure applications inside Docker

> **Educational Purpose Only**
>
> This project should only be used in a local lab environment.

---

# 📂 Project Structure

```
sql-injection-demo/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── database.db
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── README.md
```

---

# 🚀 Features

- Vulnerable SQL query
- Secure SQL query
- SQLite Database
- Account Balance Lookup
- UNION SQL Injection Demo
- Prepared Statement Example
- Docker Support
- Docker Compose Support

---

# 🛠 Technologies

- Python
- Flask
- SQLite
- HTML
- Docker
- Docker Compose

---

# ⚙️ Prerequisites

Install:

- Docker Desktop
- Docker Compose
- Git

Verify installation

```bash
docker --version
docker compose version
git --version
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/karansatpute227/sql-injection-demo.git

cd sql-injection-demo
```

---

# 🐳 Run using Docker

Build the Docker image

```bash
docker compose up --build
```

When the build completes, open

```
http://localhost:5000
```

---

# 🧪 Normal Test

Enter

```
1001
```

Expected Output

```
Account Number : 1001
Holder Name    : Karan
Balance         : 25000.0
```

---

# 💥 SQL Injection Demonstration

Open the **Vulnerable Version**

Input

```sql
' UNION SELECT user_id,password,0 FROM users --
```

Expected Output

```
admin      admin123
karan      karan123
testuser   testpass
```

The vulnerable application executes a dynamically constructed SQL query, allowing attacker-controlled input to change the query logic. :contentReference[oaicite:1]{index=1}

---

# 🔒 SQL Injection Prevention

Open the **Secure Version**

Enter the same payload

```sql
' UNION SELECT user_id,password,0 FROM users --
```

Expected Output

```
No records found
```

The secure route uses parameterized queries (prepared statements), which ensure user input is treated as data rather than executable SQL. This is the recommended mitigation approach. :contentReference[oaicite:2]{index=2}

---

# 🔍 Vulnerable Query

```python
query = "SELECT account_no, holder_name, balance FROM accounts WHERE account_no='" + account_no + "'"
```

---

# ✅ Secure Query

```python
conn.execute(
    "SELECT account_no, holder_name, balance FROM accounts WHERE account_no=?",
    (account_no,)
)
```

---

# 🐳 Docker Commands

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Run in Background

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

View Logs

```bash
docker compose logs
```

Rebuild

```bash
docker compose up --build
```

---

# 📤 Push to GitHub

```bash
git init

git add .

git commit -m "Initial SQL Injection Demo"

git branch -M main

git remote add origin https://github.com/karansatpute227/sql-injection-demo.git

git push -u origin main
```

---

# 🧑‍💻 Testing by Another User

Clone the repository

```bash
git clone https://github.com/karansatpute227/sql-injection-demo.git

cd sql-injection-demo

docker compose up --build
```

Then verify:

✅ Normal account lookup

✅ SQL Injection succeeds on Vulnerable page

✅ SQL Injection fails on Secure page

---

# 📚 Learning Outcomes

After completing this project you will understand:

- SQL Injection
- UNION Based SQL Injection
- Dynamic SQL Queries
- Prepared Statements
- Secure Coding Practices
- Docker Containerization
- Flask Web Development
- SQLite Database Integration

---

# ⚠ Disclaimer

This project is intended **only for educational purposes** in a controlled environment.

Do **not** deploy vulnerable code to production systems or use these techniques against systems you do not own or have explicit authorization to test.

---

# 👨‍💻 Author

**Karan Satpute**

- GitHub: https://github.com/karansatpute227

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
