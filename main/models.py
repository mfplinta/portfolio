from django.db import models

class ProjectTag(models.Model):
    tag = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.tag})'

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    @property
    def description_dotted_list(self):
        return self.description.replace('- ', '• ')

    def __str__(self):
        return f'{self.title} at {self.company}, {self.start_date:%b-%Y} - {(self.end_date.strftime('%b-%Y') if self.end_date is not None else ''):}'

class Skill(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, choices=(
        ('fab fa-python', 'Python'),
        ('fab fa-js', 'JavaScript'),
        ('fab fa-react', 'React'),
        ('fab fa-docker', 'Docker'),
        ('fas fa-database', 'Database'),
        ('fab fa-microsoft', 'Microsoft'),
        ('fab fa-ubuntu', 'Ubuntu'),
        ('fab fa-github-alt', 'GitHub'),
        ('fab fa-aws', 'AWS'),
    ))
    tag = models.ForeignKey(ProjectTag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    @property
    def description_dotted_list(self):
        return self.description.replace('- ', '• ')

    def __str__(self):
        return f'{self.degree} at {self.institution}, {self.start_date:%b-%Y} - {(self.end_date.strftime('%b-%Y') if self.end_date is not None else ''):}'


class Project(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    git_url = models.URLField(null=True, blank=True)
    tags = models.ManyToManyField(ProjectTag)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

    def __str__(self):
        return self.title