__author__ = 'monger'

#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request, make_response, jsonify, session
import io
import csv
import json
import pprint as pp
# import subprocess
import requests
import pandas as pd



#creating instance of the class
app=Flask(__name__)
app.secret_key = "peanuts"

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

# https://stackoverflow.com/questions/33070395/not-able-to-parse-a-csv-file-uploaded-using-flask
@app.route('/transform', methods=['GET', 'POST'])
def transform_view():
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    # print(csv_input)

    # product_name_lst = []

    # dict_ = {}
    # df = pd.DataFrame(columns=list('AB'))
    # df.columns = ['product_name']
    product_name_lst = []
    upc_lst = []
    for row in csv_input:
        print(row[0])
        clean_row = row[0].replace('\'', '')
        print(clean_row)
        url = 'https://productspider.herokuapp.com/crawl.json?spider_name=upc_db&url=https://www.upcitemdb.com/upc/' + clean_row
        print(url)
        r = requests.get(url)
        print(r.status_code)
        #     # 200
        print(r.headers['content-type'])
        #     # 'application/json; charset=utf8'
        print(r.encoding)
        #     # 'utf-8'
        j_data = r.text
        # jj_data= jsonify(j_data)
        d = json.loads(j_data)
        # print(d.keys())
        # print(d['items'][0]['similar_404_upc'])
        # similar_404_upc = d['items'][0]['similar_404_upc']
        # similar_404_desc = d['items'][0]['similar_404_desc']
        product_name_lst.append(d['items'][0]['upc'])
        # dict_['upc'].append(dict_['upc'])
        upc_lst.append(d['items'][0]['product_name'])
        # dict_['product_name'].append(dict_['product_name'])

        df = pd.DataFrame(
                        {'Product_Name': product_name_lst,
                         'UPC': upc_lst
                        })

        session["data"] = df.to_json()

        # all_products = d['items'][0]['all_products'] #<--can use this so people can pick the best name
        # url_ = d['items'][0]['url'] #
        # upc_a = d['items'][0]['UPC-A'] #
        # ean = d['items'][0]['EAN-13'] #
        # amzn = d['items'][0]['Amazon ASIN:'] #
        # cntry = d['items'][0]['Country of Registration:'] #
        # brand_href = d['items'][0]['brand_w_href'] #
        # brand = d['items'][0]['Brand:'] #
        # model = d['items'][0]['Model #:'] #
        # last_scanned = d['items'][0]['Last Scanned:'] #

# !!!!!!!
        # export all results in csv and make paginated results html
# !!!!!!!

        # dict_keys(['status', 'items', 'items_dropped', 'stats', 'spider_name'])
        # print(j_data.json())

        #     # u'{"type":"User"...'
        # print(r.json())
        # data = r.json()
        # j_data = jsonify(r.text)
        # response = r.json()
        # response = j_data

        # need to break this out into a callback function but putting here for now

        # need to parse the json data here......VVVV

    # For exporting to csv
    # stream.seek(0)
    # result = transform(stream.read())
    # response = make_response(result)
    # resp.headers["Content-Disposition"] = "attachment; filename=result.csv"
    # return response
    resp = make_response(df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
    # , render_template("result.html",tables=[df.to_html(classes='data')],titles=df.columns.values)  #, titles=df.columns.values)

# @app.route('/scrape', methods=["POST"])
# def hello_world():
#     """
#     Run spider in another process and store items in file. Simply issue command:
#
#     > scrapy crawl dmoz -o "output.json"
#
#     wait for  this command to finish, and read output.json to client.
#     """
#     spider_name = "upc_db"
#     subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "output.json"])
#     with open("output.json") as items_file:
#         return items_file.read()



# https://stackoverflow.com/questions/36384286/how-to-integrate-flask-scrapy

@app.route('/result',methods = ['GET', 'POST'])
def result():
    data = request.form.get('scrape_source')
        # dataDict = json.loads(data)
    # print(data)

    dat = session.get('data')
    dat = pd.read_json(dat, dtype=False)
    print(dat)

    return render_template("result.html",prediction=dat)

if __name__ == "__main__":
    app.run(debug=True)
