#coding=utf-8 
from itty import *
import json
online = []
def getenemy(test):
	if test == "pony":
		return 'jb'
	if test == 'jb':
		return 'pony'

@post('/fightTest')
def fightTest(request):
	name = request.POST.get("playerName",'not specified')
	enemy = getenemy(name)
	back = {'enemyName': enemy}
	return Response(json.dumps(back), content_type='application/json')



@post('/')
def post(request):
	flag = request.POST.get("flag","not specified")
	if flag == 'login':
		name = request.POST.get("username","not specified")
		password = request.POST.get("password","not specified")
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
