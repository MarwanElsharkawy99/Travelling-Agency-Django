from django.urls import path
from . import views



urlpatterns = [
    path('signup/',views.signup,name='signup'),
    #  path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login')
     
    
]