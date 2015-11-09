import os
import ConfigParser

import sqlsoup

config = ConfigParser.RawConfigParser(allow_no_value=True)
inif = open(os.environ['CONFIG'], 'rb')
config.readfp(inif)

PG_USER = config.get('hype', 'PG_USER')
PG_PASS = config.get('hype', 'PG_PASSWORD')
PG_HOST = config.get('hype', 'PG_HOST')
PG_DBNAME = config.get('hype', 'PG_DBNAME')

# connection template
ct = "postgresql://{}:{}@{}/{}"

# connection string
cs = ct.format(PG_USER, PG_PASS, PG_HOST, PG_DBNAME)
db = sqlsoup.SQLSoup(cs)
db.schema = "lbs2"

db.objects.relate('users', db.users, secondary=db.object2user._table,
                  primaryjoin=db.objects.nid == db.object2user.object_id,
                  secondaryjoin=db.object2user.user_id == db.users.nid,
                  foreign_keys=[db.object2user.user_id,
                                db.object2user.object_id])
db.users.relate('objects', db.objects, secondary=db.object2user._table)
