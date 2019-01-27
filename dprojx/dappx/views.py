from django.shortcuts import render
from . import models
from django.contrib import admin
from dappx.forms import UserForm,UserProfileInfoForm,DocumentForm,NewProjectForm
from dappx.models import UserProfileInfo,Document,NewProject
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,DetailView,ListView,CreateView,UpdateView,DeleteView #################
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.shortcuts import redirect

from django.core.paginator import Paginator #for pagination


def index(request):
    return render(request,'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def Cprogram(request):
    return render(request,'Cprogram.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
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

@login_required
def ProjectListView(request):
    documents=Document.objects.all()
    return render(request,'projectlist.html' , { 'documents': documents })



def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(docname__icontains=query) | Q(description__icontains=query)

            results= Document.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'projectlist.html', context)

        else:
            return render(request, 'projectlist.html')

    else:
        return render(request, 'projectlist.html')


class ProjectDetailView(LoginRequiredMixin,DetailView):
    login_url = '/dappx/user_login/'
    redirect_field_name = 'redirect_to'
    # request.session['user'] = user.id
    context_object_name = 'project_detail'
    model = models.Document
    template_name = 'buynow.html'


#Pagination code
class ProjectListView(ListView):
    model = models.Document
    template_name = 'projectlist.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'documents'  # Default: object_list
    paginate_by = 3
    queryset = Document.objects.all()  # Default: Model.objects.all()

@login_required
def NewProject(request):
    form = NewProjectForm(request.POST or None)
    if form.is_valid():
        newpro = form.save(commit=False)
        newpro.user = request.user
        newpro.save()
        return redirect('index')
    return render(request, 'dappx/newproject_form.html', {'form':form})
#
class MyProfileProjectListView(ListView):
    context_object_name = 'MyProfile'
    model= models.NewProject
    template_name='myprofile.html'

class NewProjectUpdateView(UpdateView):
    fields=('project_name','project_details','technology_preferred','days_available')
    # form = NewProjectForm(request.POST or None)
    model = models.NewProject
    template_name = 'projupdate.html'

class NewProjectDeleteView(DeleteView):
    model = models.NewProject
    template_name = 'reqDelete.html'
    success_url = reverse_lazy("dappx:MyProfile")
