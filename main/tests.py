from django.test import TestCase, override_settings

from main.models import SiteSettings


class SiteSettingsTests(TestCase):
    def test_get_current_returns_singleton(self):
        first = SiteSettings.get_current()
        second = SiteSettings.get_current()

        self.assertEqual(first.pk, 1)
        self.assertEqual(second.pk, 1)
        self.assertEqual(SiteSettings.objects.count(), 1)


@override_settings(
    STORAGES={
        'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
        'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
    }
)
class IndexViewTests(TestCase):
    def test_resume_link_is_rendered_when_present(self):
        settings = SiteSettings.get_current()
        settings.resume = 'files/resume.pdf'
        settings.save()

        response = self.client.get('/')

        self.assertContains(response, 'href="/media/files/resume.pdf"')
