from flask_restful import Resource


class Cat(Resource):

    def get(self):
        return {'message':'get'}
    def put(self):
        return {'message':'put'}



# class Dog(Resource)