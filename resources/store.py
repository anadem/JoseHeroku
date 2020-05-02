# resources\store.py

from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

#need these endpoints
#    GET
#    POST
#    DELETE

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json() # this also returns the items (see models\store.py)
                                # AND default status code 200
        else:
            return { "message": "store named '{}' not found".format(name) }, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return { "message": "store named '{}' already exists".format(name) }, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return { "message": "Error: unable to save store named '{}' ".format(name) }, 500

        return store.json(), 201 # 201 = success, created

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return { "message": "Store '{}' deleted".format(name) }


class StoreList(Resource):
    def get(self):
        return {'stores': [x.json() for x in StoreModel.query.all()]}
