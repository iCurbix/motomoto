from flask_restful import Resource
from src.utils.Shops import Shops


class SearchItems(Resource):
    def get(self, search):
        result = {}
        shops = [shop for shop in dir(Shops) if shop[0] != '_']
        for shop in shops:
            result[shop] = getattr(Shops, shop)(search)
        return result, 201
