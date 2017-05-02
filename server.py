#coding=utf-8 
#author: sicongHe
#LLBZA ENTERTAINMENT
#llbza server
from itty import *
import json
online = []
chungeOpreation = {"turns":0,"opreation":{"eat:":"shit"}}
ponyOpreation = {"turns":0,"opreation":{}}
def getenemy(name):
	if name == 'pony':
		return 'chunge'
	if name == 'chunge':
		return 'pony'
def getTurnData(gameId,name):
	if name == "chunge":
		return ponyOpreation
	if name == "pony":
		return chungeOpreation

def setOpreation(name,opreation,turns):
	if name == 'pony':
		ponyOpreation['turns'] = int(turns)
		ponyOpreation['opreation'] = opreation
	if name == 'chunge':
		chungeOpreation['turns'] = int(turns)
		chungeOpreation['opreation'] = opreation
@post('/hardSync')
def hardSync(request):
	gameId = request.POST.get("gameId","not specified")
	name = request.POST.get("name","not specified")
	opreation = request.POST.get("opreation","not specified")
	turns = request.POST.get("turns","not specified")
	setOpreation(name,opreation,turns)
	back = getTurnData(gameId,name)
	back = json.dumps(back)
	print 'get opreation:' + opreation
	print back
	return Response(back,content_type='application/json')


@post('/infoInit')
def infoInit(request):
	name = request.POST.get("name",'not specified')
	jsonFile = open(name + '.json')
	back = json.load(jsonFile)
	print json.dumps(back)
	return Response(json.dumps(back), content_type='application/json')

@post('/fightTest')
def fightTest(request):
	name = request.POST.get("playerName",'not specified')
	enemy = getenemy(name)
	back = {'enemyName': enemy,'gameId':request.POST.get("gameId","not specified")}
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
		if (name == 'chunge' and password == 'wocaonima'):
			online.append('chunge')
			return 'chunge'

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
