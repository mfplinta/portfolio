from django.shortcuts import render
from django.db.models import F

from main.models import Education, Experience, Project, ProjectTag, SiteSettings, Skill


def _resume_url():
    resume = SiteSettings.get_current().resume
    return resume.url if resume else None


def index(request):
    return render(request, 'main/index.html', {
        'skills': Skill.objects.all().order_by(F('title').asc()),
        'education': Education.objects.all().order_by(F('end_date').desc(nulls_first=True)),
        'experiences': Experience.objects.all().order_by(F('end_date').desc(nulls_first=True), F('start_date').desc()),
        'resume_url': _resume_url(),
    })


def projects(request, tag=None):
    if tag:
        projects = Project.objects.filter(tags__tag=tag).prefetch_related('images', 'tags').order_by(F('date').desc())
    else:
        projects = Project.objects.prefetch_related('images', 'tags').all().order_by(F('date').desc())
    return render(request, 'main/projects.html', {
        'projects': projects,
        'tag': ProjectTag.objects.get(tag=tag) if tag else None,
        'resume_url': _resume_url(),
    })
