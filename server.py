#coding=utf-8 
from itty import *

@post('/')
def post(request):
	return "username:" + request.POST.get("username","not specified")
	
@get('/')
def get(request):
	return "llbza server test"

run_itty()