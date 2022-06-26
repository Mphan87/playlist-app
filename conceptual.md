### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

PostgresSQL is a open-source database system that supports both SQL and JSON querying. Its used as a primary database for many web applications

- What is the difference between SQL and PostgreSQL?


PostgreSQL is an advanced object-relational database management system that uses SQL in addition to its own procedural language, PL/pgSQL. PostgreSQL is easy-to-use with a full stack of RDBMS database features and capabilities for handling data


- In `psql`, how do you connect to a database?

go to the terminal and type in

-sudo service postgresql start
-psql
-\c "database name" without the quotes


- What is the difference between `HAVING` and `WHERE`?

The main difference between them is that the WHERE clause is used to specify a condition for filtering records before any groupings are made, while the HAVING clause is used to specify a condition for filtering values from a group.


- What is the difference between an `INNER` and `OUTER` join?

The biggest difference between an INNER JOIN and an OUTER JOIN is that the inner join will keep only the information from both tables that's related to each other (in the resulting table). An Outer Join, on the other hand, will also keep information that is not related to the other table in the resulting table


- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?


unmatched data of the right or left table is lost when joined 


- What is an ORM? What do they do?

An object-relational mapper provides an object-oriented layer between relational databases and object-oriented programming languages without having to write SQL queries. It standardizes interfaces reducing boilerplate and speeding development time.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

AJAX stands for asynchronous javascript and XML so if you are using javascript to load data after the browser request has finished you are doing AJAX.


- What is CSRF? What is the purpose of the CSRF token?

Definition. Cross-Site Request Forgery (CSRF) is an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated. CSRH Token is used to protect against the attacks.


- What is the purpose of `form.hidden_tag()`?

The form. hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. All you need to do to have the form protected is include this hidden field and have the SECRET_KEY variable defined in the Flask configuration