#coding=utf-8 
from itty import *

@post('/')
def post(request):
	flag = request.POST.get("flag","not specified");
	if flag == 'login':
		name = request.POST.get("username","not specified");
		password = request.POST.get("password","not specified");
		print name
		print password
		if (name == 'pony' and password == 'seed333333'):
			return 'success'
		else:
			return 'fail'
	else:
		pass
	
@get('/')
def get(request):
	return "llbza server test"

run_itty(config='config')
