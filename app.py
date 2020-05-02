# app.py


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# these imports are from my .py files in this same directory
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # or mysql, postgres sql, oracle, ...
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request       # gets run before any request is run
def create_tables():
    db.create_all()             # create tables iff they don't exist

jwt = JWT(app, authenticate, identity)

# here we're defining the endpoints which can be used, by Postman or web
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

db.init_app(app)
if __name__ == '__main__':
                                    # don't app.run unless app.py is NOT imported, i.e. is main
    app.run(port=5000, debug=True)  # debug=True shows a page with error details
