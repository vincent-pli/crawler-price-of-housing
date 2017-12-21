#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import json
from pprint import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# with open('quotes.json') as data_file:
# 	data = json.load(data_file)
print "\u4f4f\u5b85"
file = open('quotes.json')
content = file.read()

# json_string = json.dumps(content)

# json_obj = json.loads('{"price": "8000", "name": "\u5fa1\u7b14\u57ce\u5e02\u5e7f\u573a", "address": "[\u00a0\u57ce\u897f\u00a0\u5927\u5174\u65b0\u533a\u00a0]\u00a0\u7ea2\u5e99\u5761\u5341\u5b57\u5411\u897f300\u7c73\u8def\u5317"}')
json_obj = json.loads(content)
# print(json_obj)
# print(type(json_obj))
# print(json_obj[0]["address"])
prog = re.compile(r"(\[)(.*)(\])")

py_list = []
for item in json_obj:
	tmp_list = []
	item["address"] = prog.search(item["address"]).group(2).split("\xa0")[1]
	if item["price"] == None:
		continue
	tmp_list.append(item["name"])
	tmp_list.append(item["address"])
	tmp_list.append(item["price"])
	tmp_list.append(item["category"])
	py_list.append(tmp_list)

# print py_list

hp_array = np.array(py_list)
pd_array = {"name": hp_array[:, 0], "address": hp_array[:, 1], "price": hp_array[:, 2], "category": hp_array[:, 3]}

# pd_array["price"] = pd.to_numeric(pd_array["price"])

df = pd.DataFrame(pd_array)

df["price"] = pd.to_numeric(df["price"])
# print df
# print df.index
# print df.columns
# print df.values
# print df.describe()

# print df.head(20)
# print df.loc[10:100]
# print df["price"]

# print df.sort(columns="price")
# plt.plot(first_ten["name"], first_ten["price"])
# plt.show()
# print df["address"]
# print df["address"].drop_duplicates()
area_list = df["address"].drop_duplicates()
for area_item in area_list:
	area_house_list = df.loc[df["address"] == area_item]
	area_house_list = area_house_list.loc[area_house_list["category"] == "住宅"]
	print "-------------------------------"
	print area_house_list.loc[area_house_list["price"].idxmax]

# category_list = df["category"].drop_duplicates()
# for category_item in category_list:
# 	category_houst_list = df.loc[df["category"] == category_item]
# 	print "*******************************"
# 	print category_houst_list.loc[category_houst_list["price"].idxmax]
# print df.loc[df["address"] == "高新"]

# Loop get the max price in each area

# house_area = df["name"] == "高新"
# house_array= df[house_area, :]
# print house_array

# house_key = None
# house_price = 0;
# for item in house_array:
# 	item_price = item[2].astype(float)
# 	if item_price > house_price:
# 		house_price = item_price
# 		house_key = item[0] + " | " + item[1]

# print house_key
# print house_price
# print western_price
# western_price = western_price.astype(float)
# print western_price.max()






