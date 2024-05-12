from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def python(request):
    return render(request,'new.html')
# Create your views here.
