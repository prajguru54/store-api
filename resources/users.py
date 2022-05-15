from flask_restful import Resource, reqparse
from models.users import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type= str, 
        required=True, 
        help="this field can't be blank"
    )
    parser.add_argument('password', 
        type= str, 
        required=True, 
        help="this field can't be blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return f"User already exists", 400

        user = UserModel(**data)
        user.save_to_db()

        return f"User is created successfully", 201

if __name__ == '__main__':
    user = UserModel.find_by_userid(1)
    print(user)

    user = UserModel.find_by_username('Jou')
    print(user)


