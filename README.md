# Technical Lesson: Creating Data with SQL

Creating and modifying data in SQL is a critical skill for any developer or analyst working with databases. In real-world scenarios, you’ll often be responsible for not just retrieving data, but also defining table structures, adding initial records, and modifying or cleaning existing data to reflect updates in business operations.

In this lesson, we’ll walk through the key DDL (Data Definition Language) and DML (Data Manipulation Language) commands used to create tables and manage rows in a database.

## Set Up

* Fork and Clone the GitHub Repo
* Install dependencies and enter the virtual environment:
    * `pipenv install`
    * `pipenv shell`

Next, let's create our database file. Create a file at the root level of this repo called `my_db.sqlite`. This is where we'll store our tables and data.

Then, let's set up our code in `main.py`. Import libraries and connect to the database.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('my_db.sqlite')
cur = conn.cursor()
```

## Instructions

### Step 1: Plan your data structure.

Before you can store or manipulate data, you need to know what kind of information you’ll be working with.

In our case, let’s assume we’re tracking users for a web application. We'll need:

* A unique user ID
* A full name
* A unique email address
* A signup date

Think of this as designing the fields you'd find on a user sign-up form.

### Step 2: Create or adjust tables (`CREATE`, `ALTER`, `DROP`).

Use CREATE TABLE to define your data model. Add the following code to main.py:

```python
cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        signup_date DATE DEFAULT CURRENT_DATE
    );  
""")
```

After running the file, you can comment out this code or delete it. Once the table is created in the database, we do not need to create it again.

If you need to adjust this structure (for example, to add a phone_number column later), you could use:

```python
cur.execute("""
    ALTER TABLE users ADD COLUMN phone_number TEXT;
""")
```

And to remove a table entirely:

```python
cur.execute("""
    DROP TABLE users;
""")
```

> Important Note: Be *very* careful with `DROP TABLE`—it deletes the table and all its data.

> All of the above commands would only need to be run once, and so each line should be commented out after the file is run once with that command. You can test all 3, dropping the table at the end. Then you can comment back in the create table code to add the table again.

### Step 3: Add data (INSERT).

Once your table is created in the database, we can add some data using `INSERT INTO`:

```python
cur.execute("""
    INSERT INTO users (name, email)
    VALUES 
        ('Sofia Ramirez', 'sofia.ramirez@example.com'),
        ('Devon Blake', 'devon.blake@example.com');
""")
```

You can now run the file. Again, the above command needs to be run only once, if you run it more, it will duplicate your data.

We'll discuss the below command further in the next section, but for now, add the code below and run the file to see your data:

```python
cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())
```

The code above doesn't alter data in the table, and thus can be run as many times as you like. Feel free to leave it in or comment out.

### Step 4: Modify data (UPDATE).

Let’s say Devon updated their email address. You can reflect this change with an `UPDATE`:

```python
cur.execute("""
    UPDATE users
    SET email = 'devon.blake@newdomain.com'
    WHERE email = 'devon.blake@example.com';
""")
```

Always include a `WHERE` clause when using UPDATE, or you might update every row in the table. When using `WHERE` to get 1 specific individual, always use a unique identifier such as an id. 

For example, imagine you have two Jane Does in your database. One has an id of 15 and the other 30. Jane Doe with an id of 30 wants to close her account. If you specify by name, you'll accidentally delete both Jane Doe accounts, which could be disasterous. If you specify by id = 30, you'll know you will only delete the correct account.

### Step 5: Remove unnecessary data (DELETE).

Sometimes, you'll need to clean up bad or test data. Let's add some bad data and then remove.

```python
cur.execute("""
    INSERT INTO users (name, email)
    VALUES 
        ('Test User', 'test@test.com');
""")
```

After running the code above and commenting it out, feel free to run the code from step 3 to see the bad data now in the database:

```python
cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())
```

We can remove that data with `DELETE FROM`.

```python
cur.execute("""
    DELETE FROM users
    WHERE name = 'Test User';
""")
```

You can run the code from step 3 again after running the `DELETE FROM` query and commenting it out. You should see the Test User now gone:

```python
cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())
```

Again, use a WHERE clause to scope your deletion carefully. It's a good practice to first preview what you’ll delete:

```python
cur.execute("""SELECT * FROM users WHERE name = 'Test User';""")
print(cur.fetchall())
```

The test user should now be gone.

Finally, you can close out your database connection at the bottom of the file.

```python
conn.close()
```

## Considerations

* CREATE TABLE	
    * Common Pifall: Forgetting constraints
    * Fix / Best Practice: Always define PRIMARY KEY and NOT NULL where applicable
* INSERT INTO
    * Common Pitfall: Mismatched values/columns
    * Fix / Best Practice: Ensure the column count matches the number of values
* UPDATE
    * Common Pitfall: No WHERE clause
    * Fix / Best Practice: Always use a condition to limit changes to specific rows
* DELETE
    * Common Pitfall: Unscoped deletion
    * Fix / Best Practice: Test your WHERE condition with a SELECT before deleting
* General
    * Common Pitfall: Running one-time queries more than once
    * Fix / Best Practice: SQL has some built in fixes for this if your code needs it, such as, instead of `CREATE TABLE cats (cols);` you could you `CREATE TABLE IF NOT EXISTS cats (cols);`.