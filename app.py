from flask import Flask, request, jsonify, render_template
import psycopg2
import time

app = Flask(__name__)

# Wait for PostgreSQL container
while True:
    try:
        conn = psycopg2.connect(
            host="db",
            database="sumdb",
            user="postgres",
            password="postgres"
        )
        break
    except Exception:
        print("Waiting for PostgreSQL...")
        time.sleep(5)

# Create table if not exists
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS calculations(
    id SERIAL PRIMARY KEY,
    num1 INTEGER,
    num2 INTEGER,
    result INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
cur.close()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/sum')
def sum_numbers():

    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))

    result = a + b

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO calculations
        (num1,num2,result)
        VALUES (%s,%s,%s)
        """,
        (a, b, result)
    )

    conn.commit()
    cur.close()

    return jsonify({
        "a": a,
        "b": b,
        "sum": result
    })


@app.route('/history')
def history():

    cur = conn.cursor()

    cur.execute("""
        SELECT id,num1,num2,result,created_at
        FROM calculations
        ORDER BY id DESC
    """)

    rows = cur.fetchall()

    cur.close()

    return render_template(
        "history.html",
        rows=rows
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )