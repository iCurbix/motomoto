from flask import Flask
from flask_restful import Api
from src.search.resources.products import SearchItems

app = Flask(__name__)
api = Api(app)

api.add_resource(SearchItems, '/<string:search>')

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
