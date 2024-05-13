from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to="clients/images",default="")
    image2 = models.ImageField(upload_to="project_main/images",default="")
    project_zip = models.FileField(upload_to="project_main_file",null=True) 
    
# Create your models here.