from django.shortcuts import render
from django.db.models import F

from main.models import Skill, Experience, Education, Project


def index(request):
    return render(request, 'main/index.html', {
        'skills': Skill.objects.all().order_by(F('title').asc()),
        'education': Education.objects.all().order_by(F('end_date').desc(nulls_first=True)),
        'experiences': Experience.objects.all().order_by(F('end_date').desc(nulls_first=True)),
    })

def projects(request, tag=None):
    if tag:
        projects = Project.objects.filter(tags__tag=tag)
    else:
        projects = Project.objects.all()
    return render(request, 'main/projects.html', {
        'projects': projects
    })