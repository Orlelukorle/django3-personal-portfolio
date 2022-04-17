from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    my_projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':my_projects})


def test(request):
    return render(request, 'portfolio/test.html')