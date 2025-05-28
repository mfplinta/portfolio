import sys

from django.conf import settings, urls
from django.urls import path
from django.conf.urls.static import static
from django.views.debug import technical_500_response
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("projects/", views.projects, name="projects"),
    path("projects/with-tag/<str:tag>/", views.projects, name="projects-withtag"),
]

urls.handler500 = lambda req: technical_500_response(req, *sys.exc_info())

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)