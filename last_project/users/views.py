from users.models import CustomUser
from django.urls import reverse_lazy
from django.views import generic
from users.serializers import UserSerializer # new api rest
from rest_framework import generics, viewsets # new api rest

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# new
class UserList(generic.ListView):
	model = CustomUser
	template_name = 'list.html'

class UserUpdate(generic.UpdateView):
	model = CustomUser
	form_class = CustomUserCreationForm
	template_name = 'update.html'
	success_url = reverse_lazy('users')

class UserDelete(generic.DeleteView):
	model = CustomUser
	template_name = 'delete.html'
	success_url = reverse_lazy('users')

# api rest
class UserApi(generics.ListCreateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer
