from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to="clients/images", default="")
    image2 = models.ImageField(upload_to="project_main/images", default="")
    project_zip = models.FileField(upload_to="project_main_file", null=True)
    project_number = models.CharField(max_length=10,null=True)
    
class User(models.Model):
    names = models.CharField(max_length=30)
    titles = models.CharField(max_length=40)
    descriptions = models.CharField(max_length=500)
    images1 = models.ImageField(upload_to="User/images",default="")
    images2 = models.ImageField(upload_to="project_main_user/images",default="")
    project_zips = models.FileField(upload_to="project_main_file",null=True) 