from sqlalchemy import ForeignKey
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    # __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id) -> None:
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name, 'price':self.price, 'store_id':self.store_id}

    @classmethod
    def get_item_by_name(cls, name):
        result = cls.query.filter_by(name= name).first()    #Result typt is <class 'models.items.ItemModel'>
        item = None
        if result:
            item = cls(result.name, result.price, result.store_id)
        return item

    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self, price):
        # print(self.price, price)
        # self.price = price
        # print('Updated price: ', end=' ')
        # print(self.price, price)
        # db.session.commit()

        _ = ItemModel.query.filter_by(name=self.name)\
            .update(dict(price=price))
        db.session.commit()
    
    def delete(self):
        _ = ItemModel.query.filter_by(name=self.name)\
            .delete()
        db.session.commit()
    
if __name__ == '__main__':
    item = ItemModel.get_item_by_name('peanut')
    print(item)