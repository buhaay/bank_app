from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def home_page(request):
    if request.method == 'GET':
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return render(request, 'home_page.html', {})
        else:
            return HttpResponse(status=403)
