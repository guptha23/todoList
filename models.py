from django.db import models

# Create your models here.
class Todo(models.Model):
    cur_date = models.DateTimeField()
    task = models.CharField(max_length=20)
