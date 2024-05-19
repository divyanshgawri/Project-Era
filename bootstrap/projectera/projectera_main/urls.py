from django.urls import path,include
from projectera_main import views
from django.conf import settings
from django.conf.urls.static import  static
urlpatterns = [
    
    path('',views.uploadForm,name="uploadForm"),
    path('upload_proj',views.upload_proj,name='upload_proj'),
    
]