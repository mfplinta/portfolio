from django.shortcuts import render

from main.models import Skill, Experience, Education


def index(request):
    return render(request, 'main/index.html', {
        'skills': Skill.objects.all(),
        'education': Education.objects.all(),
        'experiences': Experience.objects.all(),
    })

def projects(request, tag=None):
    return render(request, 'main/projects.html', {

    })