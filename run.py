# run.py
# added in video 128

from app import app
from db import db

db.init_app(app)

@app.before_first_request       # gets run before any request is run
def create_tables():
    db.create_all()             # create tables iff they don't exist
