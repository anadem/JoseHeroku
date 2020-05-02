# models\store.py

from db import db

class StoreModel(db.Model):
    # tell SQLAlchemy the table name
    __tablename__ = 'stores'

    # tell SQLAlchemy the table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
            # when lazy='dynamic' is used, self.items is no longer a list,
            # now it is a query builder with the ability to look into the items table
            # so we can use .all to retrieve all the items in the table
        return {'name': self.name, 'items': [item.json() for item in self.items.all()] }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):  # upsert
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


