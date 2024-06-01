from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

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
class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    username = models.CharField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_staff