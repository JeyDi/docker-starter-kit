SELECT	pg_terminate_backend (pid)
FROM	pg_stat_activity
WHERE	pg_stat_activity.datname = '<database_name>';

DROP DATABASE <database_name>;