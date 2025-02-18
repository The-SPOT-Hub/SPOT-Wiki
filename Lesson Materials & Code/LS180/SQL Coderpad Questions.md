Intro
Coderpad has a number of built-in tables. If you haven't used Coderpad to practice SQL before, spend a little time getting used to it.

→ What tables are we working with? How are they connected? Describe the relationships between them. How would you draw the ERD? (Or use Coderpad's ERD to explain cardinality and modality).

→ At the top right, you can view the "databases" tab, which outlines the schema we're working with. Take some time to read through and describe what we're working with.

→ View each of the tables. 
→ When you're ready, here are some additional questions. Feel free to make your own questions as you go, based on how the tables can be linked.

We want to see which employees belong to which departments. 

1. Write a SQL statement that returns a table like this:
    
    ```jsx
    department  | first_name | last_name 
    -------------+------------+-----------
     Engineering | Ian        | Peterson
     Engineering | Mike       | Peterson
     Engineering | Cailin     | Ninson
     Marketing   | John       | Mills
     Reporting   | John       | Smith
     Silly Walks | Ava        | Muffinson
    ```
    
- Possible answer
    
    ```jsx
    SELECT departments.name AS "department", employees.first_name, employees.last_name
    FROM departments
    JOIN employees
    ON employees.department_id = departments.id
    ORDER BY departments.name;
    ```
    

2. Let's format the last table so it's a bit more readable:

```jsx
Department  |                 Employees                  
-------------+--------------------------------------------
 Engineering | Ian Peterson, Mike Peterson, Cailin Ninson
 Marketing   | John Mills
 Reporting   | John Smith
 Silly Walks | Ava Muffinson
```

- Possible answer
    
    ```jsx
    SELECT departments.name AS "Department", string_agg(employees.first_name || ' ' || employees.last_name, ', ') AS "Employees"
    FROM employees
    JOIN departments
    ON employees.department_id = departments.id
    GROUP BY departments.name
    ORDER BY departments.name;
    ```
    

3. Now we want to add any departments that don't have any employees, and sort the data by department size, largest department first. Our table will look like this:

```jsx
Department  |                 Employees                  
-------------+--------------------------------------------
 Engineering | Ian Peterson, Mike Peterson, Cailin Ninson
 Marketing   | John Mills
 Silly Walks | Ava Muffinson
 Reporting   | John Smith
 Biz Dev     |
```

- Possible answer
    
    ```jsx
    SELECT departments.name AS "Department", string_agg(employees.first_name || ' ' || employees.last_name, ', ') AS "Employees"
    FROM departments
    LEFT JOIN employees
    ON employees.department_id = departments.id
    GROUP BY departments.name
    ORDER BY count(employees.id) DESC;
    ```
    
1. List the `title` of the projects that the employee named "Ava" has done, using a *scalar subquery*.
- Possible answer
    
    ```sql
    SELECT p.title 
    FROM projects p
    JOIN employees_projects ep 
    	ON p.id = ep.project_id
    WHERE ep.employee_id = (SELECT id FROM employees WHERE first_name = 'Ava')
    ```
    

_____

1. Let's add a new table to the database for employee birthdays called `employee_birthdays`. What sort of relationship should it have with the current relations? Our new table should include an `id` column as a primary key, a `birthday` column, a `cake_preference` column and an `employee_id` column. All columns should be required (not null).
- Possible answer
    
    ```jsx
    CREATE TABLE employee_birthdays (
      id serial PRIMARY KEY,
      "date" date NOT NULL,
      cake_preference text NOT NULL,
      employee_id integer NOT NULL
    );
    ```
    

2. Add a foreign key to the new table to link employee_birthdays to employees. You can do this either by editing the current `CREATE TABLE` statement or by using another statement. Note: If you edit the current `CREATE TABLE` statement, you'll have to `DROP TABLE` before running coderpad.

- Possible answer
    
    ```jsx
    ALTER TABLE employee_birthdays
    ADD FOREIGN KEY (employee_id) 
    REFERENCES employees (id);
    ```
    

3. Add three rows into employee birthdays.

- Possible answer
    
    ```jsx
    INSERT INTO employee_birthdays ("date", cake_preference, employee_id) VALUES
    ('1987-10-01', 'chocolate', 1),
    ('1598-09-12', 'cherry cheesecake', 2),
    ('1999-12-31', 'ice cream', 3),
    ('2010-03-03', 'banana pudding', 4),
    ('2004-06-12', 'fudge', 5),
    ('1991-01-27', 'vanilla', 6)
    ;
    ```
    

4. Just to check everything looks good and our tables are joined together, select the first name of each employee along with their cake preference:

```jsx
first_name |  cake_preference  
------------+-------------------
 John       | chocolate
 Ava        | cherry cheesecake
 Cailin     | ice cream
 Mike       | banana pudding
 Ian        | fudge
 John       | vanilla
```

- Possible answer
    
    ```jsx
    SELECT employees.first_name, employee_birthdays.cake_preference 
    FROM employees
    JOIN employee_birthdays
    ON employees.id = employee_birthdays.employee_id;
    ```
    

Bonus questions:

5. Can you retrieve the same data as the last one using a subquery? 

6. John Smith was fired. Delete him from the employees table, along with any other data about him.

7. Drop the foreign key constraint that links employee_birthdays to employees