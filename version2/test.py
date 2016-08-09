#!/usr/bin/python 
#coding:utf-8


from pickle import dump,load

user_list  = [{"name":"kkk","password":"123456"},{"name":"bbb","password":"123456"}]
with open("test.txt","wb") as f :
	dump(user_list,f)

with open("test.txt") as r_f:
	print load(r_f)



