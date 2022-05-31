from flask import Flask
import scraper
import utils

app = Flask(__name__)

@app.route("/products")
def products():

    plist = utils.dictToJson(scraper.getProducts())
    return plist