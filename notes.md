# Falar com Vini
Após comando docker-compose build, recebi um erro do pacote db, ela esta no projeto 
não tem conteudo. 
```
(PyJobs)  serlus@serlus-ThinkPad-T450  ~/repositorios/PyJobs   master  docker-compose build 
db uses an image, skipping
Building web
Traceback (most recent call last):
  File "bin/docker-compose", line 6, in <module>
  File "compose/cli/main.py", line 72, in main
  File "compose/cli/main.py", line 128, in perform_command
  File "compose/cli/main.py", line 304, in build
  File "compose/project.py", line 403, in build
  File "compose/project.py", line 385, in build_service
  File "compose/service.py", line 1106, in build
  File "site-packages/docker/api/build.py", line 160, in build
  File "site-packages/docker/utils/build.py", line 30, in tar
  File "site-packages/docker/utils/build.py", line 49, in exclude_paths
  File "site-packages/docker/utils/build.py", line 214, in rec_walk
  File "site-packages/docker/utils/build.py", line 184, in rec_walk
PermissionError: [Errno 13] Permission denied: '/home/serlus/repositorios/PyJobs/db'
[76232] Failed to execute script docker-compose

```
```
(PyJobs)  ✘ serlus@serlus-ThinkPad-T450  ~/repositorios/PyJobs   master  docker-compose run web python manage.py migrate
Starting pyjobs_db_1 ... done
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/base/base.py", line 217, in ensure_connection
    self.connect()
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/base/base.py", line 195, in connect
    self.connection = self.get_new_connection(conn_params)
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/postgresql/base.py", line 178, in get_new_connection
    connection = Database.connect(**conn_params)
  File "/usr/local/lib/python3.6/site-packages/psycopg2/__init__.py", line 126, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
psycopg2.OperationalError: could not connect to server: Connection refused
	Is the server running on host "localhost" (127.0.0.1) and accepting
	TCP/IP connections on port 5432?
could not connect to server: Cannot assign requested address
	Is the server running on host "localhost" (::1) and accepting
	TCP/IP connections on port 5432?


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    execute_from_command_line(sys.argv)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/__init__.py", line 381, in execute_from_command_line
    utility.execute()
  File "/usr/local/lib/python3.6/site-packages/django/core/management/__init__.py", line 375, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/base.py", line 323, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/base.py", line 364, in execute
    output = self.handle(*args, **options)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/base.py", line 83, in wrapped
    res = handle_func(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/commands/migrate.py", line 87, in handle
    executor = MigrationExecutor(connection, self.migration_progress_callback)
  File "/usr/local/lib/python3.6/site-packages/django/db/migrations/executor.py", line 18, in __init__
    self.loader = MigrationLoader(self.connection)
  File "/usr/local/lib/python3.6/site-packages/django/db/migrations/loader.py", line 49, in __init__
    self.build_graph()
  File "/usr/local/lib/python3.6/site-packages/django/db/migrations/loader.py", line 212, in build_graph
    self.applied_migrations = recorder.applied_migrations()
  File "/usr/local/lib/python3.6/site-packages/django/db/migrations/recorder.py", line 73, in applied_migrations
    if self.has_table():
  File "/usr/local/lib/python3.6/site-packages/django/db/migrations/recorder.py", line 56, in has_table
    return self.Migration._meta.db_table in self.connection.introspection.table_names(self.connection.cursor())
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/base/base.py", line 256, in cursor
    return self._cursor()
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/base/base.py", line 233, in _cursor
    self.ensure_connection()
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/base/base.py", line 217, in ensure_connection
    self.connect()
  File "/usr/local/lib/python3.6/site-packages/django/db/utils.py", line 89, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/base/base.py", line 217, in ensure_connection
    self.connect()
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/base/base.py", line 195, in connect
    self.connection = self.get_new_connection(conn_params)
  File "/usr/local/lib/python3.6/site-packages/django/db/backends/postgresql/base.py", line 178, in get_new_connection
    connection = Database.connect(**conn_params)
  File "/usr/local/lib/python3.6/site-packages/psycopg2/__init__.py", line 126, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
django.db.utils.OperationalError: could not connect to server: Connection refused
	Is the server running on host "localhost" (127.0.0.1) and accepting
	TCP/IP connections on port 5432?
could not connect to server: Cannot assign requested address
	Is the server running on host "localhost" (::1) and accepting
	TCP/IP connections on port 5432?


```