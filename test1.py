import json

import pandas as pd
import sys

# id_list = {1: 'a',2: 'b',3: 'c'}
# for i,j in id_list.items():
#     # print(i)
#     print('i:',i,'  ' , 'j:',j)
# print(sys.getdefaultencoding())
# print()
# fpath = "./test.csv"
# ratings = pd.read_csv(fpath,encoding="gbk")
# # print(ratings)
# print(ratings.head())
# print(ratings["CPMC"])
# print(ratings.shape)

# json_file = './test2.json'
# with open(json_file, 'r',encoding= 'utf-8') as f_obj:
#     json_data = json.load(f_obj)
# print(type(json_data))
# print(json_data[0].keys())
# print(json_data[0].values())
# print(json_data[0].get('id'))
# print(json_data[0].get('name'))
# print(json_data[0].get('damage'))

json_file2 = './test3.json'
with open(json_file2, 'r', encoding='utf-8') as f_json2:
    json_data2 = json.load(f_json2)
    print(type(json_data2))
years = json_data2.keys()
temper = json_data2.values()
print(years)
year_list = [int(year_str) for year_str in years]
tem_list = [float(tem_str) for tem_str in temper]
print(tem_list)
print(year_list)

year_se = pd.Series(year_list, name='year')
tem_se = pd.Series(tem_list, name='temperature')
result = pd.concat([year_se, tem_se],axis=1)
print(result)
result.to_csv('./test4.csv',index = None)

#
# f = open("./test.csv", encoding="utf8")
# pd.read_csv(f)
# print(pd.read_csv(f))
# str = "你好"
# print(str)
