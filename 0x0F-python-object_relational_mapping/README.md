# 0x0F. Python - Object-relational mapping
`Python` `OOP` `SQL` `MySQL` `ORM` `SQLAlchemy`

|By: Guillaume|
|:--|
|Weight: 1|
|Project will start Sep 8, 2022 6:00 AM, must end by Sep 12, 2022 6:00 AM|
|Checker will be released at Sep 9, 2022 6:00 AM|
|An auto review will be launched at the deadline|


## Before you start…
**Please make sure your MySQL server is in 8.0** -> [How to install MySQL 8.0 in Ubuntu 20.04](https://github.com/codewithmide/alx-higher_level_programming/tree/master/0x0D-SQL_introduction)

## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

**Without ORM:**

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

**With an ORM:**

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.
