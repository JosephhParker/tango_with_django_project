from django.shortcuts import render
from django.http import HttpResponse

		#Chapter 4

	#def index(request):
	#	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	#		# Construct a dictionary to pass to the template engine as its context.
#
#		return render(request, 'rango/index.html', context=context_dict)
			# Return a rendered response to send to the client.


#	def about(request):
#		context_dict = {'boldmessage': 'This tutorial has been put together by Joseph Parker'}
			# Construct a dictionary to pass to the template engine as its context.

#		return render(request, 'rango/about.html', context=context_dict)
			# Return a rendered response to send to the client.

	#Chapter 3

def index(request): 
	return HttpResponse("Rango says hey there partner! " + "<a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("Rango says here is the about page. " + "<a href='/rango/'>Index</a>")

