from crypt import methods
from flask import Flask , request, jsonify
from flask_cors import CORS, cross_origin
import util

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/hello")
def hello():
    return "HI"

@app.route("/GetLocations")
def get_locations():
    return jsonify(util.get_locations())

@app.route("/GetPredictedPrice", methods=["POST"])
def get_predicted_price():
    location = request.form["location"]
    sqft = request.form["sqft"]
    bath = request.form["bath"]
    bhk = request.form["bhk"]

    print(location, sqft, bath, bhk)
    return jsonify({
        'predicted_price' : util.get_predicted_price(location,sqft,bath,bhk)
    })


if __name__ == "__main__" : 
    app.run()