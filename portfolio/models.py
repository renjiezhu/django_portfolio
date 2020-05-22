from django.db import models

# Create your models here.

class Experience(models.Model):
    EXP_TYPE = [
        ('project', 'project'),
        ('work', 'work'),
    ]
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    experience_type = models.CharField(null=True, choices=EXP_TYPE)
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True, blank=True)
    github_url = models.URLField(null=True)