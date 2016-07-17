#!/usr/bin/python
#coding:utf-8
import sys
'''
打开锁文件提取锁定的用户名
'''
lock_f = open("lock.txt",'a+')
lock_list = lock_f.readlines()
print lock_list

'''
打开用户存放文件,提取用户名以及密码,当用户名存在时才提示输入密码
'''
mes_dict = {}
mes_f = open("user.txt",'r+')
for lines in mes_f.readlines():
	key,value = lines.strip('\n').split(':')
	mes_dict[key] = value

print mes_dict

'''
开始真正的登录验证过程
'''
while True :
	userName = raw_input("请输入用户名:")
	lock_user = userName + '\n'
	print lock_user
	if  lock_user in lock_list :
		print "用户已经锁定,请联系管理员处理!退出"
		break
	if userName in mes_dict.keys():
		for  count in range (1,4) : #===>用for循环来对密码只能输入三次进行限制
			passW = raw_input("第%d次输入密码,还有%d次可以输入:" %((count),(3-count)))
			if mes_dict[userName] == passW :
				sys.exit("登录成功")
		lock_line = userName + '\n'
		if lock_line not in lock_list :
			lock_f.write(lock_line)
			sys.exit( "用户%s已经锁定成功了！" %userName)
	else :
		print "用户不存在"
		break

lock_f.close()
mes_f.close()
