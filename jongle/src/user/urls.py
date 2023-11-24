"""
URL configuration for jongle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path 
from interface.views import Pages
from user.views import Pages
from user.views import *
app_name ='user'
urlpatterns = [
     path('signin', Pages.signin, name='signin'),
     path('signup', Pages.signup, name='signup'),
     path('register' , Pages.saveauth , name = 'register'),
     path('signinauth',Pages.signin_auth  ,name = 'signinauth'),

    path('logout' , Pages.logout ,name='logout'),
    path('send_message', Pages.send_message, name='send_message'),
    path('reset_password/', Pages.reset_password, name='reset_password'),
    path('reset_password/<uidb64>/<token>/', Pages.reset_password_confirm, name='reset_password_confirm'),
    path('user/packages/', Pages.user_packages, name='user_packages'),
    path('user/take_action/<int:package_id>/', Pages.take_action, name='take_action'),
    path('user/set_ready/<int:package_id>/', Pages.set_ready, name='set_ready'),

]
