from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('signup/', views.register, name='signup'),
    path('user-dashboard/<int:pk>/', views.user_dashboard, name='user-dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
]