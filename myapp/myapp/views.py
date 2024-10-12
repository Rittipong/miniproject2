from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def form(request):
	return render(request, 'form.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def news(request):
	return render(request, 'news.html')

def reviews(request):
	return render(request, 'reviews.html')

def mk(request):
	return render(request, 'mk.html')

def minecraft(request):
	return render(request, 'minecraft.html')
	
def doom(request):
	return render(request,'doom.html')

def cy(request):
	return render(request,'cy.html')

def si(request):
	return render(request,'si.html')

def recy(request):
	return render(request,'recy.html')

def redoom(request):
	return render(request,'redoom.html')

def remine(request):
	return render(request,'remine.html')

def remk(request):
	return render(request,'remk.html')

def resi(request):
	return render(request,'resi.html')

def comment(request):
	return render(request,'comment.html')