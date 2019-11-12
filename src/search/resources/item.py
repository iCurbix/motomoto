from flask_restful import Resource
from src.utils.FourbikerScrapper import fourbiker


class SearchItems(Resource):
    def get(self , search):
        return fourbiker(search)
