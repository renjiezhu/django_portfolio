from django.db import models

class Keyword(models.Model):

    kw = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.kw


class Experience(models.Model):
    EXP_TYPE = [
        ('project', 'project'),
        ('work', 'work'),
        ('education', 'education')
    ]
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    experience_type = models.CharField(null=True, max_length=200, choices=EXP_TYPE)
    keywords = models.ManyToManyField(Keyword, blank=True)
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return self.title


class Post(models.Model):

    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    keywords = models.ManyToManyField(Keyword)
    date_published = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

