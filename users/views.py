from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
