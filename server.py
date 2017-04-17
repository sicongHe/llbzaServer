#coding=utf-8 
from itty import *

@post('/')
def index(request):
	
	return "username:" + request.POST.get("username","not specified")

run_itty()