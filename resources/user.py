# resources \ user.py

from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):
    # parser for JSON of the request, will ensure username & password are there
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type =str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type =str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return { "message": "A user with that username already exists"}, 400

        user = UserModel(**data) # ** == unpack == (data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully"}, 201 # 201 = created
