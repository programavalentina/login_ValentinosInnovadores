from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('all/', views.UserList.as_view(), name='users'),
    path('update/<int:pk>/', views.UserUpdate.as_view(), name='userupdate'),
    path('delete/<int:pk>/', views.UserDelete.as_view(), name='userdelete'),
    path('api/', views.UserApi.as_view()),
]
