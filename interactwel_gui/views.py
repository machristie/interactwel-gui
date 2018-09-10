from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def hello_world(request):
    return HttpResponse("Hello from InterACTWEL!")

@login_required
def projects(request):
    return render(request, 'interactwel_gui/projects.html')
