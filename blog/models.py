from django.db import models
import datetime

class Blog_post(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateField(default=datetime.date.today) #auto_now=False, auto_now_add=True)
    description = models.TextField(max_length = 1000, default='')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title