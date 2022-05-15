import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.items import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
        type= float, 
        required=True, 
        help="this field can't be blank"
    )
    parser.add_argument('store_id', 
        type= int, 
        required=True, 
        help="this field can't be blank"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.get_item_by_name(name)
        return item.json() if item else {'Message': 'Item not found'}, 404
    
    @jwt_required()
    def post(self, name):
        if ItemModel.get_item_by_name(name):
            return {"Message:": f"Item '{name}' already exist"}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        item.insert()
        # ItemModel.create_item(name, data['price'])
        return {'Message':"Item created"}, 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.get_item_by_name(name)
        if not item:
            return {'Message': f"Item '{name}' doesn't exist "}, 400

        item.delete()
        return {'Message': f"Item '{name}' deleted"}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.get_item_by_name(name)

        if not item:
            item = ItemModel(name, data['price'], data['store_id'])
            item.insert()
            print('Item not found, trying to create')
        else:
            print(f"Item found, trying to update price to {data['price']}")
            item.update(data['price'])
            
            
        return ItemModel.get_item_by_name(name).json()



class ItemList(Resource):
    def get(self):
        # return {'items':[{'name':item.name, 'price':item.price} for item in ItemModel.query.all()] }
        # return {'items':list(map(lambda x:x.json() , ItemModel.query.all()))}
        #Even better way
        return {'items':[item.json() for item in ItemModel.query.all()] }

if __name__ == '__main__':
    # print(ItemModel.get_item_by_name('banana'))
    print(ItemModel.query.all())
