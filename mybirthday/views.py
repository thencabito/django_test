import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	now = datetime.datetime.now()
	return render(request,"mybirthday/index.html",{
		"birthday": now.month == 8 and now.day == 3
		})