from django.shortcuts import render

from main.models import Skill, Experience


def index(request):
    return render(request, 'main/index.html', {
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
    })

def projects(request):
    return render(request, 'main/projects.html', {

    })