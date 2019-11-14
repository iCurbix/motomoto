from flask import Flask
from flask_restful import Api
from src.search.resources.item import SearchItems

app = Flask(__name__)
api = Api(app)


@app.route('/favicon.ico')
def favicon():
    return None , 404


api.add_resource(SearchItems , '/<string:search>')

if __name__ == '__main__':
    app.run(port=5000 , debug=True)
