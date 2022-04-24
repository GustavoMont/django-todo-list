from django.db import models


class Task(models.Model):
    title = models.CharField("title", max_length=80)
    description = models.CharField("description" ,max_length=200)
    done = models.BooleanField("done" ,default=False)