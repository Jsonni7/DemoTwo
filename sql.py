import random
import string
import cherrypy
import os, os.path
import sqlite3
import time

DB_STRING = "my.db"
c = sqlite3.connect(DB_STRING)

data = time.time()
r = c.execute("INSERT INTO user_string VALUES (?, ?)", ['1', '555'])
r = c.execute("SELECT value FROM user_string")
print(r.fetchone())
