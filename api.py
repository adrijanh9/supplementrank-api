from flask import Flask
import scraper
import utils
from flask import jsonify

app = Flask(__name__)

@app.route("/products")
def products():

    resp = jsonify(scraper.getProducts()) 
    resp.headers.add("Access-Control-Allow-Origin", "*")
    
    return resp