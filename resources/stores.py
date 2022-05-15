from flask_restful import Resource
from models.stores import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.get_store_by_name(name)
        if not store:
            return {"Message :":"Store not found"}, 404
        return store.json()


    def post(self, name):
        if StoreModel.get_store_by_name(name):
            return {"Message :":"Store already exist"}, 400
        store = StoreModel(name)
        try:
            store.insert()
        except:
            return {"Message :":"Coud not create store"}, 500

        return {"Message :":"Store created successfully"}, 201

    def delete(self, name):
        store = StoreModel.get_store_by_name(name)
        if store:
            store.delete()
        
        return {"Message :":"Store deleted"}

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()] }
