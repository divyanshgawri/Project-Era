from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def python(request):
    return render(request,'python.html')
def proj1python(request):
    return render(request,'project1.html')
# Create your views here.
