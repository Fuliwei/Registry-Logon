#!/usr/bin/python
#coding:utf-8 
#filename:zhuce.py

file = open('users.txt','a+')
mes_dict = {}
mes = file.readlines()
for line in mes :
	k,v = line.strip('\n').split(':')
	mes_dict[k] = v

print mes_dict

while True :
	name = raw_input('请输入姓名：')
	if (name is '') or (name in mes_dict.keys()):
		print '用户名已经存在了或者为空,请重新输入：'
		continue
	getPassword = raw_input('请输入密码：')
	confirm_Password = raw_input('请再次输入密码：')
	if (getPassword  == '') or (confirm_Password != getPassword) or (confirm_Password == '') :
		print '密码不一致或者密码不能为空'
		continue
	else :
		file.write('%s:%s\n' %(name,getPassword))
		print "注册成功"
		break


file.close()
