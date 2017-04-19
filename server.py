#coding=utf-8 
from itty import *
online = []
@post('/')
def post(request):
	flag = request.POST.get("flag","not specified");
	if flag == 'login':
		name = request.POST.get("username","not specified");
		password = request.POST.get("password","not specified");
		print name
		print password
		if (name == 'pony' and password == 'seed333333'):
			online.append('pony')
			return 'pony'
		if (name == 'jb' and password == 'wocaonima'):
			online.append('jb')
			return 'jb'

		else:
			return 'fail'
	else:
		pass
	
@get('/')
def get(request):
	a = ''
	for i in online:
		a = a + i
	return a

run_itty(config='config')
