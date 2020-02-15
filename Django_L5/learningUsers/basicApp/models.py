from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    # extending User table / add data to user which User Does not have
    user = models.OneToOneField(User)

    # additional Fiels
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username