from django.db import models
from datetime import datetime

class Dates(models.Model):
    topic = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    type = models.CharField(max_length=24, default=None)
    descr = models.TextField(blank=True, null=True)
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ------- {}'.format(self.topic,self.updated_at.strftime("%m/%d/%Y, %H:%M:%S"))