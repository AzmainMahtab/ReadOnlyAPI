from django.db import models

# Create your models here.
class Todo(models.Model):
    tittle = models.CharField(max_length=200)
    body = models.TextField(max_length=600, null=True)

    def __str__(self):
        return self.tittle