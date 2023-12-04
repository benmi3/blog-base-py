This simple web app is made by looking at [Django-Documents](https://docs.djangoproject.com/en/4.2/)

# Use this if you change the database from sqlite3 to postgres
# start docker
# Start postgresql server docker image:
''''
docker run --rm --name pg -p 5432:5432 \
   -e POSTGRES_PASSWORD=welcome \
   postgres:15
'''
# (optional) To have a psql terminal on pg.
# In another terminal (tab) run psql:
'''
docker exec -it -u postgres pg psql
'''
# (optional) For pg to print all sql statements.
# In psql command line started above.
'''
ALTER DATABASE postgres SET log_statement = 'all';
'''
