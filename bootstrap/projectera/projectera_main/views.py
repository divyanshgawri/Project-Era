from django.shortcuts import render,HttpResponse,redirect
from .models import Projects
from .models import User
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

def upload_proj1(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        proj_title= request.POST.get('proj_title')
        proj_desc = request.POST.get('proj_desc')
        # choose = request.POST.get('choose')
        image1 = request.FILES.get('image1')  
        image2 = request.FILES.get('image2')  
        project_zip = request.FILES.get('project_zip')
        p1 = Projects()
        p1.names = user_name
        p1.titles = proj_title
        p1.desc = proj_desc
        p1.images1 = image1
        p1.images2 = image2
        p1.zipi = project_zip
        p1.save()
        #redirect("trr")
        tdata=Projects.objects.all()
        return redirect("index")

        
    return render(request,'upload',{'tdata':tdata})


    
# Create your views here.
