# SQL Injection Account Balance Lab

Educational local lab showing a vulnerable SQL injection route and a secure fixed route.

## Run with Docker Compose

```bash
docker compose up --build
```

Open:

```text
http://localhost:5000
```

## Normal Test

Input:

```text
1001
```

Expected vulnerable and secure result:

```text
1001 | Karan | 25000.0
```

## Prove SQL Injection Attack Succeeds

Go to vulnerable form `/vulnerable` and enter:

```sql
' UNION SELECT user_id, password, 0 FROM users --
```

Expected result: the page displays user IDs and passwords from the `users` table:

```text
admin    | admin@123  | 0
karan    | karan123   | 0
testuser | testpass   | 0
```

The vulnerable query becomes:

```sql
SELECT account_no, holder_name, balance FROM accounts WHERE account_no = '' UNION SELECT user_id, password, 0 FROM users --'
```

## Prove Prevention Works

Go to secure form `/secure` and enter the same payload:

```sql
' UNION SELECT user_id, password, 0 FROM users --
```

Expected result:

```text
No records found.
```

Reason: the secure route uses a prepared statement:

```python
conn.execute("SELECT account_no, holder_name, balance FROM accounts WHERE account_no = ?", (account_no,))
```

The payload is treated as plain input text, not as SQL code.

## Push to GitHub

```bash
git init
git add .
git commit -m "Add SQL injection account balance lab"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sql-injection-account-lab.git
git push -u origin main
```

## Ask Friend to Test

```bash
git clone https://github.com/YOUR_USERNAME/sql-injection-account-lab.git
cd sql-injection-account-lab
docker compose up --build
```

Then test both:

- Vulnerable page: attack payload shows users/passwords.
- Secure page: same payload returns no records.
