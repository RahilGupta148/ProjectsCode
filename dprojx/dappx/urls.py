from django.urls import path
from dappx import views

from django.conf import settings
from django.conf.urls.static import static
from .views import (searchposts)
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    # path('index/',views.index,name='index'),
     path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('home/',views.home,name='home'),
    path('videoform/',views.model_form_upload,name='videoform'),
    path('projectlist/',views.ProjectListView.as_view(),name='projectlist'),
    path('projectlist/<int:pk>/',views.ProjectDetailView.as_view(),name='detail'), ###############3
    path('NewProject/',views.NewProject,name='NewProject'),
    path('MyProfileProjectlist/',views.MyProfileProjectListView.as_view(),name='MyProfile'),
    path('update/<int:pk>/',views.NewProjectUpdateView.as_view(),name='updateProj'),
    path('delete/<int:pk>/',views.NewProjectDeleteView.as_view(),name='deleteProj'),
    path('Cprogram/',views.Cprogram,name='Cprogram'),
    path('', searchposts, name='searchposts'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
