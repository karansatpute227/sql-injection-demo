from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.environ.get('DB_PATH', 'bank.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS accounts')
    cur.execute('DROP TABLE IF EXISTS users')

    cur.execute('''
        CREATE TABLE accounts (
            account_no TEXT PRIMARY KEY,
            holder_name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE users (
            user_id TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')

    cur.executemany('INSERT INTO accounts VALUES (?, ?, ?)', [
        ('1001', 'Karan', 25000.00),
        ('1002', 'Rohan', 43000.50),
        ('1003', 'Priya', 9000.75),
    ])
    cur.executemany('INSERT INTO users VALUES (?, ?)', [
        ('admin', 'admin@123'),
        ('karan', 'karan123'),
        ('testuser', 'testpass'),
    ])
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    rows = []
    query = ''
    error = None
    account_no = ''
    if request.method == 'POST':
        account_no = request.form.get('account_no', '')
        # INTENTIONALLY VULNERABLE: string concatenation allows UNION injection.
        query = "SELECT account_no, holder_name, balance FROM accounts WHERE account_no = '" + account_no + "'"
        try:
            conn = get_db()
            rows = conn.execute(query).fetchall()
            conn.close()
        except Exception as e:
            error = str(e)
    return render_template('result.html', title='Vulnerable Search', rows=rows, query=query, error=error, account_no=account_no)


@app.route('/secure', methods=['GET', 'POST'])
def secure():
    rows = []
    query = 'SELECT account_no, holder_name, balance FROM accounts WHERE account_no = ?'
    error = None
    account_no = ''
    if request.method == 'POST':
        account_no = request.form.get('account_no', '')
        # SAFE: parameterized query treats input as data, not SQL code.
        try:
            conn = get_db()
            rows = conn.execute(query, (account_no,)).fetchall()
            conn.close()
        except Exception as e:
            error = str(e)
    return render_template('result.html', title='Secure Search', rows=rows, query=query, error=error, account_no=account_no)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
