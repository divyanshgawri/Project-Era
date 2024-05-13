from django.shortcuts import render,HttpResponse
def index(request):
    return render(request,'index.html')
def python(request):
    return render(request,'python.html')
def proj1python(request):
    return render(request,'project1.html')
def upload_proj1(request):
    return render(request,'upload.html')
# Create your views here.
