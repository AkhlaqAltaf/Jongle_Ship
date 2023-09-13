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
from django.contrib import admin

from django.urls import path , include
from interface.views import Pages
from .views import Pages
app_name = 'packages'
urlpatterns = [
 
     path('packages' , Pages.my_packages ,name='packages'),
     path('uploadpackages' , Pages.upload_package ,name='uploadpackages'),
    
     

       path('warehouse' , Pages.warehouse ,name= 'warehouse'),

           path('in-warehouse', Pages.warehouse, name='in_warehouse'),
    path('process_actions', Pages.process_actions, name='process_actions'),
    path('repackage-popup/<int:profile_id>', Pages.show_repackage_popup, name='show_repackage_popup'),
    path('process-repackage/<int:profile_id>', Pages.process_repackage, name='process_repackage'),
    path('forward-popup/<int:profile_id>', Pages.show_forward_popup, name='show_forward_popup'),
    path('process-forward/<int:profile_id>', Pages.process_forward, name='process_forward'),
    path('consolidate-popup/<int:profile_id>', Pages.show_consolidate_popup, name='show_consolidate_popup'),
    path('process-consolidate/<int:profile_id>', Pages.process_consolidate, name='process_consolidate'),
        # path('upload_shipment', Pages.upload_shipment, name='upload_shipment'),
 
    #     path('path/to/fetch/notifications/', Pages.fetch_notifications, name='fetch-notifications'),
    # path('path/to/mark/notifications/as/read/', Pages.mark_notifications_as_read, name='mark-notifications-as-read'),
    # path('reset_password/', Pages.reset_password, name='reset_password'),
    # path('reset_password/<uidb64>/<token>/', Pages.reset_password_confirm, name='reset_password_confirm'),
     
]
