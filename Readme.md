/*
'''
需求:实现一个用户注册登录的体系。

要求:

	1.用户注册时需要输入两次密码,且两次密码都一致时才能显示注册成功

	2.用户登录时输入用户名需要验证是否锁定,锁定则返回给用户已锁定;未锁定则继续输入密码,密码输入正确则显示登录成功。
否则在此输入密码,密码连续输错三次则锁定用户

###############################################################################################################

思路:

	注册的思路:====>具体代码见zhuce.py

		输入用户名===>检验用户是否为空或者已经存在===>为空或者用户已存在,重新输入用户名====>输入密码并再次输入密码验证
		=====>两次密码输入中有一次为空或者两次输入的密码不相等==>让用户重新输入用户名密码在此注册==>直至注册成功就退出

	登录的思路：===>具体代码见login.py

		输入用户名===>验证锁文件中是否存在,若存在则打印用户已经锁定===>锁文件中不存在,查看用户名是否存在===>用户名不存
		在则打印用户名不存在====>用户名存在,则输入密码进行验证,密码三次错误,将用户名记录到锁文件中====>三次密码输入正确
		则打印登录成功的提示
'''
*/
