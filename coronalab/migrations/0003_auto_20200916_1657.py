# Generated by Django 3.1 on 2020-09-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coronalab', '0002_remove_reguser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='bangladeshupdate',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='worldupdate',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
