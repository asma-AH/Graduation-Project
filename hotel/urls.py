from django.urls import path
from . import views 
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url , include

app_name = 'hotel'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.UserFormView.as_view() , name = 'SignUp'),
    path('signin/', auth_views.LoginView.as_view(template_name='hotel/login.html'), name = 'signin'),
    path('oauth/', include('social_django.urls', namespace='social')),  
    path('logout/', views.logout , name = 'LogOut')
]