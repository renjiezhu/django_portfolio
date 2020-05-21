from django.db import models

# Create your models here.

class Experience(models.Model):
    TYPE = [
        ('project', 'project'),
        ('work', 'work'),
    ]
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    exp_type = models.CharField(null=True, choices=TYPE)
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True)