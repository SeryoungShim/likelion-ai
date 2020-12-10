from django.db import models

# Create your models here.
class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()
    title = models.TextField()
    describe = models.TextField()
    date = models.CharField(max_length=40)