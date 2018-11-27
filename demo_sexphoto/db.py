#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *
from playhouse.db_url import connect
#创建链接
db = connect('mysql://username:password@localhost:3306/db')

class URL(Model):
	url=CharField(null=True,index = True)
	class Meta:
		database = db

#定义数据表模型
class ITEM_Info(Model):
	item_title = CharField(null=True,index = True)
	item_type= CharField(null=True,index = True)
	item_update=CharField(null=True,index = True)
	class Meta:
		database = db

#定义数据表模型
class YSE(Model):
	owner = ForeignKeyField(ITEM_Info, backref='yses')
	image_name = CharField(null=True,index = True)
	image_url = CharField(null=True,index = True)
	image_title = CharField(null=True,index = True)
	image_update=CharField(null=True,index = True)
	image_type= CharField(null=True,index = True)
	image_save_file=CharField(null=True,index = True)
	image_save_date=DateField(null=True)
	class Meta:
		database = db
#定义数据表模型
class TSE(Model):
	owner = ForeignKeyField(ITEM_Info, backref='tses')
	image_name = CharField(null=True,index = True)
	image_url = CharField(null=True,index = True)
	image_title = CharField(null=True,index = True)
	image_update=CharField(null=True,index = True)
	image_type= CharField(null=True,index = True)
	image_save_file=CharField(null=True,index = True)
	image_save_date=DateField(null=True)
	class Meta:
		database = db

#定义数据表模型
class OSE(Model):
	owner = ForeignKeyField(ITEM_Info, backref='oses')
	image_name = CharField(null=True,index = True)
	image_url = CharField(null=True,index = True)
	image_title = CharField(null=True,index = True)
	image_update=CharField(null=True,index = True)
	image_type= CharField(null=True,index = True)
	image_save_file=CharField(null=True,index = True)
	image_save_date=DateField(null=True)
	class Meta:
		database = db

#定义数据表模型
class QSE(Model):
	owner = ForeignKeyField(ITEM_Info, backref='qses')
	image_name = CharField(null=True,index = True)
	image_url = CharField(null=True,index = True)
	image_title = CharField(null=True,index = True)
	image_update=CharField(null=True,index = True)
	image_type= CharField(null=True,index = True)
	image_save_file=CharField(null=True,index = True)
	image_save_date=DateField(null=True)
	class Meta:
		database = db

#定义数据表模型
class MSE(Model):
	owner = ForeignKeyField(ITEM_Info, backref='mses')
	image_name = CharField(null=True,index = True)
	image_url = CharField(null=True,index = True)
	image_title = CharField(null=True,index = True)
	image_update=CharField(null=True,index = True)
	image_type= CharField(null=True,index = True)
	image_save_file=CharField(null=True,index = True)
	image_save_date=DateField(null=True)
	class Meta:
		database = db
#定义数据表模型
class SSE(Model):
	owner = ForeignKeyField(ITEM_Info, backref='sses')
	image_name = CharField(null=True,index = True)
	image_url = CharField(null=True,index = True)
	image_title = CharField(null=True,index = True)
	image_update=CharField(null=True,index = True)
	image_type= CharField(null=True,index = True)
	image_save_file=CharField(null=True,index = True)
	image_save_date=DateField(null=True)
	class Meta:
		database = db

#定义数据表模型
class MXSE(Model):
	owner = ForeignKeyField(ITEM_Info, backref='mxses')
	image_name = CharField(null=True,index = True)
	image_url = CharField(null=True,index = True)
	image_title = CharField(null=True,index = True)
	image_update=CharField(null=True,index = True)
	image_type= CharField(null=True,index = True)
	image_save_file=CharField(null=True,index = True)
	image_save_date=DateField(null=True)
	class Meta:
		database = db

#定义数据表模型
class KSE(Model):
	owner = ForeignKeyField(ITEM_Info, backref='kses')
	image_name = CharField(null=True,index = True)
	image_url = CharField(null=True,index = True)
	image_title = CharField(null=True,index = True)
	image_update=CharField(null=True,index = True)
	image_type= CharField(null=True,index = True)
	image_save_file=CharField(null=True,index = True)
	image_save_date=DateField(null=True)
	class Meta:
		database = db



db.create_tables([YSE,KSE,MXSE,MSE,QSE,OSE,TSE,SSE])
db.create_tables([URL,ITEM_Info])

def db_get_item_firstpic(item_id):
	item=ITEM_Info.get(ITEM_Info.id==item_id)
	item_type=item.item_type
	if item_type == u'亚洲色图':
		with db.atomic():
			db_data=YSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id)
			return db_data[0].image_url
	elif item_type == u'偷拍自拍':
		with db.atomic():
			db_data=TSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id)
			return db_data[0].image_url
	elif item_type == u'欧美色图':
		with db.atomic():
			db_data=OSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id)
			return db_data[0].image_url
	elif item_type == u'清纯唯美':
		with db.atomic():
			db_data=QSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id)
			return db_data[0].image_url
	elif item_type == u'美腿丝袜':
		with db.atomic():
			db_data=MSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id)
			return db_data[0].image_url
	elif item_type == u'少妇熟女':
		with db.atomic():
			db_data=SSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id)
			return db_data[0].image_url
	elif item_type == u'明星淫乱':
		with db.atomic():
			db_data=MXSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id)
			return db_data[0].image_url
	elif item_type == u'卡通动漫':
		with db.atomic():
			db_data=KSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id)
			return db_data[0].image_url

def db_get_item_list(page_num,limt,item_type):
	data_list=[]
	datas=ITEM_Info.select().where(ITEM_Info.item_type==item_type).paginate(page_num,limt)
	for data in datas:
		imgsrc=db_get_item_firstpic(data.id)
		data_list.append({'title':data.item_title,'date':data.item_update,'imgsrc':imgsrc,'id':data.id})
	return data_list


def db_get_item_pic(item_id):
	data=[]
	item=ITEM_Info.get(ITEM_Info.id==item_id)
	item_type=item.item_type
	if item_type == u'亚洲色图':
		with db.atomic():
			for pic in YSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id):
				data.append({'source': pic.image_url, 'type':'image'})
	elif item_type == u'偷拍自拍':
		with db.atomic():
			for pic in TSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id):
				data.append({'source': pic.image_url, 'type':'image'})
	elif item_type == u'欧美色图':
		with db.atomic():
			for pic in OSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id):
				data.append({'source': pic.image_url, 'type':'image'})
	elif item_type == u'清纯唯美':
		with db.atomic():
			for pic in QSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id):
				data.append({'source': pic.image_url, 'type':'image'})	
	elif item_type == u'美腿丝袜':
		with db.atomic():
			for pic in MSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id):
				data.append({'source': pic.image_url, 'type':'image'})
	elif item_type == u'少妇熟女':
		with db.atomic():
			for pic in SSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id):
				data.append({'source': pic.image_url, 'type':'image'})
	elif item_type == u'明星淫乱':
		with db.atomic():
			for pic in MXSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id):
				data.append({'source': pic.image_url, 'type':'image'})
	elif item_type == u'卡通动漫':
		with db.atomic():
			for pic in KSE.select().join(ITEM_Info).where(ITEM_Info.id == item_id):
				data.append({'source': pic.image_url, 'type':'image'})
	return data
	

