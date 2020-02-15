from django.db import models

class User(models.Model):
    fName = models.CharField(max_length=264)
    lName = models.CharField(max_length=264)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
