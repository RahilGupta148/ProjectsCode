from django.urls import path
from dappx import views

from django.conf import settings
from django.conf.urls.static import static
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    # path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('home/',views.home,name='home'),
    path('videoform/',views.model_form_upload,name='videoform'),
    path('projectlist/',views.ProjectListView,name='projectlist'),
    path('buynow/',views.BuyNow.as_view(),name='buynow'),
    #url(r'^register/$',views.register,name='register'),
    #url(r'^user_login/$',views.user_login,name='user_login'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
