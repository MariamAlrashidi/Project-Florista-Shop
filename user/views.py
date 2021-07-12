from django.shortcuts import render, redirect, HttpResponse
from django.urls import path
from . import views
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, UpdateProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.

def homepage(request):
	return render (request=request, template_name="home.html")



# Create your views here.

# SignUp new user:
def register(request):
    form = UserForm()

    if (request.method == "POST"):
        user = UserForm(request.POST)
        if (user.is_valid()):
            print(user)
            user.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for signing up in Florista")
            return redirect('home')
           
        else:
            form = user
            
    return render(request , 'register.html' , 
    {
        "form" : form
    }
    )


@login_required
def profile(request):
    return render(request , 'profile.html' )


#Update User profile (didn't work)
@login_required
def update_profile(request):
    print("request: ", request)
    user = User.objects.get(username = request.user)
    print("user: ", user)
    profile = Profile.objects.get(user = user)
    print("profile: ", profile)
    print("post: ", request.POST)
    if request.method == 'POST':
        form1 = UserForm(request.POST, instance=request.user)
        form2 = UpdateProfile(request.POST, instance=request.user.profile)
        form1.save()
        form2.save()
        return redirect(f'/user/{request.user.id}')
        # if form1.is_valid() and form2.is_valid():
           

    else:
        form1 = UserForm(initial={"email": user.email,"username": user.username})
        form2 = UpdateProfile(initial={"image": profile.image, "bio": profile.bio, "location": profile.location})
                                                        
    return render(request, 'show_profile.html', locals())

#
# Show User Profile
def show_profile(request , pk):
    id_ = pk
    try:
        one_user = User.objects.get(id=pk)
    except Exception:
        return HttpResponse("error")
    
    return render(request , 'show_profile.html' ,
    {   
    "profile" : one_user
    } )


  