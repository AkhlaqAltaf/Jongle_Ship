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
app_name ='user'
urlpatterns = [
    
    #  path('',Pages.home ,name='home' ),
    #    path('home',Pages.home ,name='home' ),

     path('signin', Pages.signin, name='signin'),
     path('signup', Pages.signup, name='signup'),
     path('register' , Pages.saveauth , name = 'register '),
     path('signinauth',Pages.signin_auth  ,name = 'signinauth'),
    #  path('store',Pages.store_list, name='store'),
    #  path('help' , Pages.help ,name='help'),
     path('logout' , Pages.logout ,name='logout'),
    #  path('packages' , Pages.package_details ,name='packages'),
    #  path('uploadpackages' , Pages.upload_package ,name='uploadpackages'),
    #  path('printbarcode' , Pages.generate_barcode ,name='printbarcode'),
     path('send_message', Pages.send_message, name='send_message'),

    #   path('calculator', Pages.calculate_price_view, name='calculator'),
    path('reset_password/', Pages.reset_password, name='reset_password'),
    path('reset_password/<uidb64>/<token>/', Pages.reset_password_confirm, name='reset_password_confirm'),
     
]
