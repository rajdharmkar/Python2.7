'''This example uses a separate exception handler in
do_database_work() to undo the changes made in the database, then
a global exception handler to report the error message.'''




''' $ python sqlite_error.py
INFO:db_example:Creating tables
INFO:db_example:Inserting logging (error reporting and auditing)
INFO:db_example:Inserting os (Operating system services)
INFO:db_example:Inserting sqlite3 (SQLite database access)
INFO:db_example:Inserting sys (Runtime services)
ERROR:db_example:Rolling back transaction
ERROR:db_example:Error while doing database work
Traceback (most recent call last):
  File "sqlite_error.py", line 51, in main
    do_database_work(do_create)
  File "sqlite_error.py", line 38, in do_database_work
    throws()
  File "sqlite_error.py", line 15, in throws
    raise RuntimeError('this is the error message')
RuntimeError: this is the error message'''