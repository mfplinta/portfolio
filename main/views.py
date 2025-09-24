from django.shortcuts import render
from django.db.models import F

from main.models import Skill, Experience, Education, Project, ProjectTag


def index(request):
    return render(request, 'main/index.html', {
        'skills': Skill.objects.all().order_by(F('title').asc()),
        'education': Education.objects.all().order_by(F('end_date').desc(nulls_first=True)),
        'experiences': Experience.objects.all().order_by(F('end_date').desc(nulls_first=True), F('start_date').desc()),
    })

def projects(request, tag=None):
    if tag:
        projects = Project.objects.filter(tags__tag=tag).order_by(F('date').desc())
    else:
        projects = Project.objects.all().order_by(F('date').desc())
    return render(request, 'main/projects.html', {
        'projects': projects,
        'tag': ProjectTag.objects.get(tag=tag) if tag else None,
    })