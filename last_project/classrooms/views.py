from classrooms.models import ClassRoom
from django.urls import reverse_lazy
from django.views import generic

from .forms import ClassRoomForm

class ClassRoomList(generic.ListView):
	model = ClassRoom
	template_name = 'classrooms/index.html'

class ClassRoomCreate(generic.CreateView):
	model = ClassRoom
	form_class = ClassRoomForm
	template_name = 'classrooms/form.html'
	success_url = reverse_lazy('classrooms')

class ClassRoomUpdate(generic.UpdateView):
	model = ClassRoom
	form_class = ClassRoomForm
	template_name = 'classrooms/form.html'
	success_url = reverse_lazy('classrooms')

class ClassRoomDelete(generic.DeleteView):
	model = ClassRoom
	template_name = 'classrooms/delete.html'
	success_url = reverse_lazy('classrooms')
