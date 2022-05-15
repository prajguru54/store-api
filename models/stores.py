from email.utils import parsedate
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    # __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel')


    def __init__(self, name) -> None:
        self.name = name

    def json(self):
        return {'name':self.name, 'items':[item.json() for item in self.items]}

    @classmethod
    def get_store_by_name(cls, name):
        result = cls.query.filter_by(name= name).first()    #Result typt is <class 'models.items.StoreModel'>
        store = None
        if result:
            store = cls(result.name)
        return store

    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        _ = StoreModel.query.filter_by(name=self.name)\
            .delete()
        db.session.commit()
    
if __name__ == '__main__':
    item = StoreModel.get_item_by_name('fruit_store')
    print(item)