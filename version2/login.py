#!/usr/bin/python
#coding:utf-8

from flask import Flask ,request ,render_template


app = Flask(__name__)

@app.route("/login", methods = ["GET","POST"])
def login():
	print request.method
	if request.method == 'POST':
		userName = request.form.get("username","None")
		password = request.form.get("password","None")
		print userName ,password
		##验证登录,登录成功返回成功界面
	#	if userName in 
	else :
		print "GET method"
		return render_template("login.html")


if __name__ == "__main__":
	app.run(host="0.0.0.0",port=666,debug=True)
