from django.contrib import admin
from .models import Projects
from .models import User,UserProfile
# admin.site.register(Projects
# Register your models here.
admin.site.register(Projects)
admin.site.register(User)
admin.site.register(UserProfile)
