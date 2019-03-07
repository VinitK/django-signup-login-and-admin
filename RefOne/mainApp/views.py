from mainApp.forms import NewUserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.views.generic import (View,
                                  TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.http import HttpResponseRedirect, HttpResponse

from mainApp import models


# Create your views here.

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # if context_object_name is not defined
    # then ListView automatically creates object named school_model and returns it


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'mainApp/school_detail.html'
    # if context_object_name is not defined
    # then DetailView automatically creates object named school and returns it


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('principal', 'location')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("mainApp:list")


class IndexView(TemplateView):
    template_name = 'mainApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Hello World!"
        context['number'] = 100
        return context


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
