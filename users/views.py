from django.http.response import HttpResponse
from django.contrib.auth import get_user_model
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserCreationForm

User = get_user_model() 

def users(requests):
    users = User.objects.all() 
    results = ", ".join([user.username for user in users])
    return HttpResponse(results) 

class SignUpView(CreateView):  
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'