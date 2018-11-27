#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from db import *
from flask import Flask ,render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/get_item_list',methods=['POST'])
def get_item_list():
	if request.method=='POST':
		page_num,limt,item_type=(int(request.form['page_num']),int(request.form['limt']),str(request.form['item_type']))
		data=db_get_item_list(page_num,limt,item_type)
		return jsonify({'stat_code':200,'data':data})
@app.route('/get_items_pics',methods=['POST'])
def get_items_pics():
	if request.method=='POST':
		item_id=int(request.form['item_id'])
		data=db_get_item_pic(item_id)
		return jsonify(data)

if __name__=='__main__':
	app.run(host='localhost',port='80')
