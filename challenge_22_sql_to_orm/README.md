## Challenge: SQL to ORM
SQL queries and SQLAlchemy ORM queries are two ways of querying relational databases, but they differ in their syntax and approach.

SQL queries involve writing SQL statements directly in the code to retrieve data from the database. On the other hand, SQLAlchemy ORM queries are written in Python and use an object-oriented approach to interact with the database.

Rather than writing SQL statements, developers define classes and their attributes that map to database tables and columns. These classes are known as ORM models, and they provide an abstraction layer between the application code and the database.

In summary, while SQL queries require knowledge of SQL syntax and are more focused on the database structure, SQLAlchemy ORM queries provide a higher level of abstraction and can make database interactions more intuitive and Pythonic.

In this challenge you're going to work on an API that allows you to manage events and book tickets for events. The starting point is an API that's already been implemented for you, using FastAPI in combination with a SQLite database. Currently, it's not setup ideally: the API routes contain all of the code and directly interact with the SQLite database using SQL queries. Next to needing to know SQL syntax, there's also the risk of accidentally creating a security risk (SQL injection) when you write code for this API.

Refactor the code to use SQLAlchemy instead of direct SQL queries. For now, there's no need to refactor the actual API logic or extend the capabilities - this will be addressed in the upcoming challenges. However, I do recommend you split up the code into separate files at the same time, so that the `main.py` file remains small and your code remains manageable.

### Resources
* [Video](https://youtu.be/x1fCJ7sUXCM) about the differences between using SQL queries vs. ORM systems