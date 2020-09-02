from django.http import HttpResponseRedirect

def index(request):
	return HttpResponseRedirect("http://127.0.0.1:8000/bsr/")