# Generated by Django 3.1.14 on 2022-04-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='body',
            field=models.TextField(max_length=600, null=True),
        ),
    ]
