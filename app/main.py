import pandas
from flask import Flask, jsonify, request
import xmltodict
import gspread
import gspread_dataframe as gd
from celery import Celery
from .base import *




@app.route("/") 
def home_view(): 
        return "<h1>the app is working</h1>"

@app.route("/post", methods=['GET', 'POST'])
def parse_xml():
    xml_data = request.data
    content_dict = xmltodict.parse(xml_data)
    write_to_gsheets.delay("app/gd_key.json",pandas.DataFrame(split_data(content_dict)))
    return jsonify(split_data(content_dict))








