from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.conf import settings ##################



# Create your models here.
class Document(models.Model):
    docname = models.CharField(max_length=256,blank=True)
    description=models.TextField(max_length=1000,blank=True)
    vidimage = models.FileField(upload_to='documents/')
    uploaded_at=models.DateTimeField(default=timezone.now())
    # project_img = models.ImageField(upload_to="photos")
    project_video = models.CharField(max_length=256,blank=True)
    proj_price = models.IntegerField(default=500)
    # desc = models.CharField(max_length=256)
    def __str__(self):
        return self.docname


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

#################################33
class NewProject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=32)
    project_name = models.CharField(max_length=256,default='')
    # user = models.ManyToManyField(User,related_name='newproject')
    project_details = models.TextField(max_length=700,blank=False,default='')
    technology_preferred = models.CharField(max_length=256)
    days_available = models.DateTimeField(default=timezone.now())
    proj_status = models.CharField(max_length=256,default='')
    quotation_fixed = models.IntegerField(default=None)
    pay_due = models.IntegerField(default=100)

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse("dappx:MyProfile")
