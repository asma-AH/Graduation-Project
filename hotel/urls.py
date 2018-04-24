from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

from django.conf.urls.static import static


app_name = 'hotel'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.UserFormView.as_view(), name='SignUp'),
    path('signin/', auth_views.LoginView.as_view(template_name='hotel/login.html'), name='signin'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('logout/', views.logout, name='LogOut'),
    path('', views.Gen, name='Gen'),
     url(r'^hotel/form/$', views.model_form_upload, name='model_form_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)