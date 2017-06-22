from django.shortcuts import render

def index(request):
		return render(request, 'personal/home.html')
# Create your views here.

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If you would like to contact me bladhg afd asdf a','adfawef@gmail.com']})