import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import  Template,loader
def poyy(request):
    todos_list = ["1","2","3"]
    #dtemplate = loader.get_template('maybblog/todotemp.html')
    #html = dtemplate.render({'todos_list' : todos_list})
    #return HttpResponse(html)
    return render(request,'todotemp.html',{'todos_list' : todos_list})


def index(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "time in", offset, "will be", now
    return HttpResponse(html)
