from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    docname = models.CharField(max_length=256,blank=True)
    description=models.CharField(max_length=1000,blank=True)
    vidimage = models.FileField(upload_to='documents/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    # project_img = models.ImageField(upload_to="photos")
    project_video = models.FileField(upload_to='documents/',blank=True)
    # desc = models.CharField(max_length=256)
    def __str__(self):
        return self.docname


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

# class Project(models.Model):
#     name = models.CharField(max_length=256)
#     project_img = models.ImageField(upload_to="photos")
#     project_video = models.ImageField()
#     desc = models.CharField(max_length=256)
#
#     def __str__(self):
#         return self.name
