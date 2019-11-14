from flask_restful import Resource
from src.utils.FourbikerScrapper import fourbiker
from src.utils.Xlmoto import xlmoto
import asyncio


class SearchItems(Resource):
    def get(self , search):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        responses = loop.run_until_complete(asyncio.gather(fourbiker(search) , xlmoto(search)))
        return {
            '4biker': responses[0],
            'xlmoto': responses[1]
        }
