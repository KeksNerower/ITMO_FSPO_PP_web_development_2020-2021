from django.shortcuts import render
from django.http import Http404
from project_first_app.models import Owner

def home(request):
    return render(request, 'home.html')

def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    
    return render(request, 'owner.html', {"owner": owner})
