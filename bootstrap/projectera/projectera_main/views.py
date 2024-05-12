from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def python(request):
    return render(request,'python.html')
# Create your views here.
