# Session 18 : 23/9/2023

## How to do join (outer & inner) in pandas ?

Using merge method in pandas we can identify hyperparameter (how) to inner or outer also we can use Join method in pandas

## Stored procedure sql

A stored procedure in SQL is a collection of SQL statements that can be executed as a single unit. Stored procedures are typically used to encapsulate a series of SQL statements for reuse, security, and performance reasons. They are stored in the database and can be called by name whenever needed.

```sql
CREATE PROCEDURE AddNumbers
    @num1 INT,
    @num2 INT
AS
BEGIN
    SELECT @num1 + @num2 AS Result;
END;
```
```sql
EXEC AddNumbers @num1 = 5, @num2 = 7;
```
## Achieve Gold sql badge on hacker rank
[Profile](https://www.hackerrank.com/minaemil329)