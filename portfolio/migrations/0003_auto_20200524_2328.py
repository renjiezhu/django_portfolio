# Generated by Django 3.0.3 on 2020-05-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200522_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='experience_type',
            field=models.CharField(choices=[('project', 'project'), ('work', 'work'), ('education', 'education')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='portfolio.Keyword'),
        ),
    ]
