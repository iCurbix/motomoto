from flask_restful import Resource
from src.utils.FourbikerScrapper import fourbiker
from src.utils.Xlmoto import xlmoto


class SearchItems(Resource):
    def get(self , search):
        return {
            '4biker': fourbiker(search),
            'xlmoto': xlmoto(search)
        }
