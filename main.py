from flask import Flask, json, render_template, redirect, url_for, request, jsonify
import os
from werkzeug.utils import secure_filename
import web_open as opn

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/crawl", methods=["POST"])
def crawl_progress():
    domain_dict = request.form['address']
    print("도메인 주소는 :", domain_dict)
    result_data, result_num = opn.jjim_file(domain_dict)
    return render_template("crawl_result.html", result = result_data, result_num = result_num)


if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.187.1", port=80)
