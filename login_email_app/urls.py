from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('signup/', views.signup, name = 'signup'),
	path('', views.home, name = 'home'),
	path('activate/<uidb64>/<token>/', views.activate, name = "activate"),
	path('login/', auth_views.LoginView.as_view(template_name="login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name = "logout"),

]