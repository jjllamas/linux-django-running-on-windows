from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index_view(request):
	message = "hello world django. You have a Linux Django Application running on Windows."
	ctx = {'message': message}
	return render_to_response('helloworld/index.html', ctx, context_instance=RequestContext(request))
