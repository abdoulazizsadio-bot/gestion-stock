import sqlite3, os

db = os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3')
print('db path:', db)
print('exists:', os.path.exists(db))
if not os.path.exists(db):
    raise SystemExit('db.sqlite3 not found')
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
rows = cur.fetchall()
print('tables:')
for r in rows:
    print('-', r[0])
conn.close()
