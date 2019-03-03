Lesson 1D - Data types and directives:
  given:
    exercise: 1d.sql
  steps:
  - SQL:
      expected result: |+
        CREATE TABLE
        INSERT 0 1
        INSERT 0 1
         id  |  total  |  invoice_date_time  | paid 
        -----+---------+---------------------+------
         123 | 3444.50 | 2017-01-01 00:00:00 | t
         124 | 3445.50 | 2017-01-02 00:00:00 | f
        (2 rows)

...
