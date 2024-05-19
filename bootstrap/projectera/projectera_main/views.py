from django.shortcuts import render,HttpResponse,redirect
from .models import Projects
from .models import User
from django.utils.http import urlencode
from django.utils.crypto import get_random_string
def index(request):
    return render(request,'index.html')
def python(request):
    pp1 = User()
    ter = User.objects.all()
    
    return render(request,'python.html',{'ter':ter})
def proj1python(request):
    return render(request,'project1.html')


def uploadForm(request):
    return render(request,'upload.html')

from django.shortcuts import render, redirect
from .models import Projects

def upload_proj(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        proj_title = request.POST.get('proj_title')
        proj_desc = request.POST.get('description')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        project_zip = request.FILES.get('project_zip')
        project_number = get_random_string(length=8)
        
        p1 = Projects(
            name=user_name,
            title=proj_title,
            description=proj_desc,
            image1=image1,
            image2=image2,
            project_zip=project_zip,
            project_number = project_number
        )
        p1.save()
        #oiii = p1.objects.all()
        query_string = urlencode({'projects_number': project_number})
        url = f"/?{query_string}"
        return redirect(url)

    return render(request, 'upload.html')



    
# Create your views here.
