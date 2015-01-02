from django.shortcuts import render

# Create your views here.
def index(request):
	template = 'index.html'
	return render(request,template)

def partitioning(request):
	template = 'partitioning.html'
	return render(request,template)

def ceilings(request):
	template = 'ceilings.html'
	return render(request,template)

def other(request):
	template='other.html'
	return render(request,template)

def endorsements(request):
	template='endorsements.html'
	return render(request,template)

def mezzanine(request):
	template = "mezzanine.html"
	return render(request, template)