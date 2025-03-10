from django.shortcuts import render

from main.models import Skill, Experience, Education, Project


def index(request):
    return render(request, 'main/index.html', {
        'skills': Skill.objects.all(),
        'education': Education.objects.all(),
        'experiences': Experience.objects.all(),
    })

def projects(request, tag=None):
    if tag:
        projects = Project.objects.filter(tags__tag=tag)
    else:
        projects = Project.objects.all()
    return render(request, 'main/projects.html', {
        'projects': projects
    })