from django.shortcuts import render
from . import models
from django.contrib import admin
from dappx.forms import UserForm,UserProfileInfoForm,DocumentForm
from dappx.models import UserProfileInfo,Document
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


# admin.site.register(UserProfileInfo)
admin.site.register(Document)

def index(request):
    return render(request,'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # profile = profile_form.save(commit=False)
            # profile.user = user
            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     profile.profile_pic = request.FILES['profile_pic']
            #     profile.save()
                # registered = True
            registered = True
        else:
            # print(user_form.errors,profile_form.errors)
            print(user_form.errors)
    else:
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()
    return render(request,'registration.html',
                            {'user_form':user_form,
                            # 'profile_form':profile_form,
                            'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {}) ###############################3

def home(request):
    documents=Document.objects.all()
    return render(request,'videohome.html' , { 'documents': documents })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            ########
            HttpResponseRedirect('home')
            # HttpResponseRedirect(reverse('home'))
    else:
        form = DocumentForm()
    return render(request,'videoform.html' , {
        'DocumentForm': form
    })
# class projectlist(TemplateView):
#     template_name = 'projectlist.html'
def ProjectListView(request):
    documents=Document.objects.all()
    return render(request,'projectlist.html' , { 'documents': documents })
class BuyNow(TemplateView):
    template_name='buynow.html'
