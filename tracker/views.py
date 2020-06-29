from django.http import HttpResponseRedirect

def index(request):
	return HttpResponseRedirect("https://covid19bulandshahr.herokuapp.com/bsr/")