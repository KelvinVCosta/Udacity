# "Database code" for the DB Forum.

import psycopg2 as pg
import bleach

DBNAME = "forum"
SELECT_QUERY = "select content, time from posts order by time desc"
INSERT_QUERY = "insert into posts values (%s)"


def get_posts():
    "Return all posts from the 'database', most recent first."
    db = pg.connect(database=DBNAME)
    c = db.cursor()
    c.execute(SELECT_QUERY)
    r = c.fetchall()
    db.close()
    return r


def add_post(content):
    "Add a post to the 'database' with the current timestamp."
    bleach.clean(content)
    db = pg.connect(database=DBNAME)
    c = db.cursor()
    c.execute(INSERT_QUERY, (content,))
    db.commit()
    db.close()


