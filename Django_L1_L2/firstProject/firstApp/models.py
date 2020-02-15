from django.db import models

class Topic(models.Model):
    topName = models.CharField(unique=True,max_length=264)

    def __str__(self):
        return self.topName

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name =models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
