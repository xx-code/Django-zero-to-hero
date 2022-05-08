from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'todo/index.html', {})

def add_task(request):
    return render(request, 'todo/add_task.html')