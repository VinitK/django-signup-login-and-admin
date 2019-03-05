from django.shortcuts import render
from mainApp.forms import NewUserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    data_dict = {'text':'Hello World!', 'number': 100}
    return render(request, 'mainApp/index.html', context={'data': data_dict})


def users(request):
    user_list = User.objects.order_by('first_name')
    return render(request, 'mainApp/users.html', context={'users': user_list})


def signup(request):

    # form function
    registered = False
    if request.method == "POST":
        user_form = NewUserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = NewUserForm()
        profile_form = UserProfileInfoForm()

    # form function end
    return render(request, 'mainApp/signup.html', context={'user_form': user_form,
                                                           'profile_form': profile_form,
                                                           'registered': registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print("#PROBLEM Someome tried login and failed")
            print(f"#PROBLEM Username: {username} and password: {password}")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'mainApp/login.html', context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def special(request):
    return HttpResponse("You are logged in!")