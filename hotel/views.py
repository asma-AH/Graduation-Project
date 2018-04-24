from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, UserLoginForm
from .forms import DocumentForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
import logging
from hotel.models import User

from django.conf import settings
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)
def Gen(request):
    
     return logger.debug('Something went wrong!')


def index(request):
    return render(request, 'hotel/index.html')


def logout(request):
    django_logout(request)
    return redirect('hotel:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'hotel/signup.html'

    """display blank form """

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

        """process form data  """

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized ) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('hotel:index')

        else:
            return render(request, self.template_name, {'form': form, 'error': "this form is invalid "})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'hotel/UploadSample.html', {
        'form': form
    })