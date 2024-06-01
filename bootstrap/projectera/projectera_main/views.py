from django.shortcuts import render,HttpResponse,redirect
from .models import Projects,UserProfile
from .forms import LoginForm, RegistrationForm
from .models import User
from django.utils.http import urlencode
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
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
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Pass the user object to the login function
                return redirect('index')  # Redirect to home page after successful login
            else:
                form.add_error(None, 'Invalid username or password.')  # Add error message to form
    else:
        form = LoginForm()
    return render(request, 'login.html', {'login_form': form},user  )

def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            new_username = form.cleaned_data['new_username']
            new_password = form.cleaned_data['new_password']
            
            # Check if the username is already taken
            if User.objects.filter(username=new_username).exists():
                # Handle the case where the username is already taken
                error_message = "Username already exists. Please choose a different username."
                return render(request, 'login.html', {'registration_form': form, 'error_message': error_message})
            else:
                # Create a new User object and save it to the database
                user = User.objects.create_user(username=new_username, email=email, password=new_password)
                user.first_name = name


                # Create a new UserProfile object and save it to the database
                user_profile = UserProfile(
                    name=name,
                    email=email,
                    mobile=mobile,
                    username = new_username,
                    password = new_password
                )
                user_profile.save()

                # Redirect to the login page after successful registration
                return redirect('login')
    
    # If the request method is GET or the form is invalid, render the registration form
    return render(request, 'login.html', {'registration_form': form})
    
# Create your views here.
