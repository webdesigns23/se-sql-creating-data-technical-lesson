import sqlite3
import pandas as pd

conn = sqlite3.connect('my_db.sqlite')
cur = conn.cursor()

# cur.execute("""
# 	CREATE TABLE users (
# 		id INTEGER PRIMARY KEY,
# 		name TEXT NOT NULL,
# 		email TEXT UNIQUE NOT NULL,
# 		signup_date DATE DEFAULT CURRENT_DATE
# 	);
# """)

# cur.execute("""
#     ALTER TABLE users ADD COLUMN phone_number TEXT;
# """)

# #And to remove a table entirely:
# cur.execute("""
#     DROP TABLE users;
# """)


# cur.execute("""
#     INSERT INTO users (name, email)
#     VALUES 
#         ('Sofia Ramirez', 'sofia.ramirez@example.com'),
#         ('Devon Blake', 'devon.blake@example.com');
# """)

# conn.commit()



# cur.execute("""
#     UPDATE users
#     SET email = 'devon.blake@newdomain.com'
#     WHERE email = 'devon.blake@example.com';
# """)
# conn.commit()


# cur.execute("""
#     INSERT INTO users (name, email)
#     VALUES 
#         ('Test User', 'test@test.com');
# """)

# conn.commit()


# cur.execute("""SELECT * FROM users WHERE name = 'Test User';""")
# print(cur.fetchall())


# cur.execute("""
#     DELETE FROM users
#     WHERE name = 'Test User';
# """)

# conn.commit()


cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())

conn.close()