from django.urls import path
from django.contrib.auth import views as auth_views # Import the built-in views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='hello/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
