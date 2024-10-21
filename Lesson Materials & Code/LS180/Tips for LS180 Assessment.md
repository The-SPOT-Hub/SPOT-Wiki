# Tips for LS180 Assessment

Course: LS180
Concepts: SQL
Last Edited: June 6, 2022 3:56 PM

## Prepare To Write Lots Of SQL Statements

For most of the assessment, you receive questions for which you must write and submit SQL statements.

It's highly recommended that you test your SQL statements by querying Postgres to not submit syntaxt errors in your solution and to verify your solution.

### Three Methods for Testing your SQL Statements Efficiently

You can query the database by writing SQL Statements line by line in psql, but that gets unwieldy quick.

Here are some alternative options:

1. Write SQL statements line by line in psql, but if you make a mistake in a multiline statement, instead of aborting your command, you can press up arrow and fix your mistake.
2. It's still difficult to debug SQL statements when you only see one line at a time. You can call the `\e` meta-command in psql to open your SQL statement in a terminal text editor like nano or vim. Now, you can see the whole SQL statement as you write it in the terminal.
3. The third method is my preferred and I highly recommend it. It has two differences. One, instead of writing your SQL statements in psql you write it in an `.sql` file. Two, you write a script to execute the SQL statements idempotently. Idempotent is a fancy word for an operation that gives the same result no matter how many times you do it.

Let's say we open a `auction.sql` file. It contains the following SQL statements:
    
    ```sql
    CREATE TABLE bidders (
      id serial,
      name varchar(50),
      PRIMARY KEY(id)
    );
    
    COPY bidders
      FROM 'path/to/bidders.csv'
      WITH DELIMITER ',' CSV HEADER;
    ```
    
    We can issue SQL commands from our file to the `auction` database using this command:
    `psql auction -f auction.sql` . The `-f` flag is to specify the file to run.
    
    So far, we've moved our SQL statements to a file. But, our script isn't idempotent yet. It works the first time we run it. But if we run it again, two errors are raised:
    
    ```sql
    psql:auction_exercise_2.sql:5: ERROR:  relation "bidders" already exists
    psql:auction_exercise_2.sql:9: ERROR:  duplicate key value violates unique constraint "bidders_pkey"
    DETAIL:  Key (id)=(1) already exists.
    CONTEXT:  COPY bidders, line 2
    ```
    
    When we re-run the commands in the `auction.sql` file, we issue the same commands again to the `auction` database. The first error is because we run the `CREATE TABLE` statement again on the same database. Postgres raises an error since the relation already exists. The second error is because we copy the data from the csv file again, and it violates our unique constraint on the `id` column.
    
    As you can see, the script isn't idempotent. It doesn't give the same result each time we run it. There are different ways to make an SQL script idempotent. You can drop the tables you create if the exist using this statement: `DROP TABLE bidders IF EXISTS` . You can add that statement before the `CREATE TABLE` statement for the respective table, fixing our errors.
    
    However, my prefered method for testing my SQL statements during the assessment doesn't require adding extra SQL statements to the SQL file. Instead we create bash script, let's call it `idempotent_script.sh` . Here's what we write inside:
    
    ```bash
    DATABASE_NAME=$1
    
    dropdb $DATABASE_NAME
    
    createdb $DATABASE_NAME
    
    psql $DATABASE_NAME -f $DATABASE_NAME.sql
    ```
    
    Here's how we call it: `bash ./idempotent_script.sh auction` . The `auction` argument is the database to which I'll issue commands. On the first line of the script, I grab the first argument `$1` and give it a name by assigning it to a variable `DATABASE_NAME`. Then, I drop that database and create it again, effectively creating a blank slate from which to run commands. Then, I run the SQL statements from a file on the last line.
    
    By convention, I name the sql file the same as my database name, but you can name them differently. In that case you need to modify to script to take a second argument, a path to the file to run:
    
    ```bash
    DATABASE_NAME=$1
    SQL_FILE_PATH=$2
    
    dropdb $DATABASE_NAME
    
    createdb $DATABASE_NAME
    
    psql $DATABASE_NAME -f $SQL_FILE_PATH
    ```
    
    There you go. Now each time you run this bash script the result will be the same. You can then connect to the database with psql to inspect its state if you wish.
    
    I hope this helps!