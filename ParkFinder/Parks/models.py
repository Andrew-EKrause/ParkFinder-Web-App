from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# WILL USE THIS LATER IF/WHEN YOU CREATE USER ACCOUNTS - THIS MAY BE IN A DIFFERENT APP AS WELL!!!
class Post(models.Model):
    options = (
        #bookmarks = models.ManyToManyField(User, related_namename='bookmark', default=None, Blank=True)
    )