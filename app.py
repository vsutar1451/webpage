from flask import Flask,request, render_template
from flask import jsonify
from flask import json
from werkzeug.exceptions import HTTPException
import random
import string
import math
from flask import make_response, jsonify
import requests



app = Flask(__name__)
app.config.from_object("config.Config")


def custom_error(message, status_code): 
    return make_response(jsonify(message), status_code)

@app.route("/hello",methods=['GET'])
def main():
	try:
		lang = request.args.get('language').lower()
		lang=str(lang)
		payload={"language":lang}
		response = requests.get("https://ignitesol-app.herokuapp.com/hello?",params=payload)
		print(response.text)
		return render_template("response.html",data=response.text)
	except Exception as error:
		print("IN Exception:",error)
		return error

@app.route("/")
def index():
	return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)
