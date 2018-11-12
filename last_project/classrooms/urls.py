from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.ClassRoomList.as_view(), name='classrooms'),
	path('create/', views.ClassRoomCreate.as_view(), name='classroomcreate'),
	path('update/<int:pk>/', views.ClassRoomUpdate.as_view(), name='classroomupdate'),
    path('delete/<int:pk>/', views.ClassRoomDelete.as_view(), name='classroomdelete'),
]
