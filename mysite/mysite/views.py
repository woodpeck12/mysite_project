from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
import datetime
#from django.shortcuts import render

def hello(request):
	return HttpResponse('wow wow')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset,dt)
	return HttpResponse(html)

def template_exe(request):
	t = template.Template('<h1>template test {{ name }}</h1>')
	c = template.Context({'name': 'tommy'})
	return HttpResponse(t.render(c))

def test_gettemplate(request):
	t=get_template('test_temp.html')
	#html = t.render(template.Context({'current_date': 'tommy'}))
	html = t.render({'current_date': 'tommy'})
	return HttpResponse(html)
	#return render(request,'test_temp.html',{'current_date':'datedate'})