from django.db import models

class Alticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creat_time = models.DateTimeField(auto_now=True)