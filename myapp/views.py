from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import random

def hello(request):
    return HttpResponse('<h1>Hello world!</h1>')
    
def hello2(request,username):
    now = datetime.now()
    return render(request,'hello3.html',locals())
    
def hello4(request,username):
    now = datetime.now()
    return render(request,'hello4.html',locals())
    
def testdict(request):
    now = datetime.now()
    dict1 = {'key1':123, 'key2':456}
    return render(request, 'hello4.html', dict1)
    
def dice(request):
    no=random.randint(1,6)
    return render(request, "dice.html", {"no":no})
    
def dice2(request):
   no1=random.randint(1,6)
   no2=random.randint(1,6)
   no3=random.randint(1,6) 
   return render(request,"dice2.html",locals())
   
times=0  
def dice3(request):
   global times
   times = times + 1
   local_times=times
   username="David"
   dict_no={"no":random.randint(1,6)}   
   return render(request,"dice3.html",locals())
   
a = 0  
def show(request):
    global a
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    times1 = [1,2,3,4,5,6,7,8,9]
    times2 = [1,2,3,4,5,6,7,8,9]
    return render(request,"show.html",locals())

def filter(request):
	value=4
	list1=[1,2,3]
	pw="芝麻開門"
	
	html="<h1>Hello</h1>"
	value2=False
	return render(request,"filter.html",locals())