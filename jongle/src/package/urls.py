# """
# URL configuration for jongle project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from importlib.metadata import packages_distributions

# from django.contrib import admin

# from django.urls import path , include, reverse
# from setuptools import find_packages
# from interface.views import Pages
# from package.controller.package_controller import upload_package
# from .views import Pages
# app_name = 'packages'
# urlpatterns = [
 
#      path('packages' , Pages.my_packages ,name='packages'),
#      path('process_actions/', Pages.process_actions, name='process_actions'),

#      path('uploadpackages' , Pages.upload_package ,name='uploadpackages'),
#      path('sendpackage' ,Pages.upload_package ,name='sendpackage'),
#      path('assistedtopurchase' ,Pages.upload_package ,name='assistedtopurchase'),
#      path('warehouse' , Pages.warehouse ,name= 'warehouse'),
#      path('in-warehouse/', Pages.warehouse, name='in_warehouse'),
#     #  path('in_warehouse/', Pages.in_warehouse, name='in_warehouse'),

#     # path('process_actions', Pages.process_actions, name='process_actions'),
#      path('repackage-popup/<int:profile_id>', Pages.show_repackage_popup, name='show_repackage_popup'),
#      path('process-repackage/<int:profile_id>', Pages.process_repackage, name='process_repackage'),
#      path('forward-popup/<int:profile_id>', Pages.show_forward_popup, name='show_forward_popup'),
#      path('process-forward/<int:profile_id>', Pages.process_forward, name='process_forward'),
#      path('consolidate-popup/<int:profile_id>', Pages.show_consolidate_popup, name='show_consolidate_popup'),
#      path('process-consolidate/<int:profile_id>', Pages.process_consolidate, name='process_consolidate'),
#         # path('upload_shipment', Pages.upload_shipment, name='upload_shipment'),
  

#     path('admin/upload_package/', upload_package, name='upload_package'),
#     path('admin/package_list/', packages_distributions, name='admin_package_list'),
#     path('admin/send_package/<int:package_id>/', find_packages, name='send_package'),



#     #     path('path/to/fetch/notifications/', Pages.fetch_notifications, name='fetch-notifications'),
#     # path('path/to/mark/notifications/as/read/', Pages.mark_notifications_as_read, name='mark-notifications-as-read'),
#     # path('reset_password/', Pages.reset_password, name='reset_password'),
#     # path('reset_password/<uidb64>/<token>/', Pages.reset_password_confirm, name='reset_password_confirm'),
     
# ]

# urls.py
from django.urls import path
from .views import Pages
from . import views

app_name = 'packages'

urlpatterns = [
    path('packages', Pages.my_packages, name='packages'),
    path('process_actions/', Pages.process_actions, name='process_actions'),
    path('uploadpackages', Pages.upload_package, name='uploadpackages'),
    path('sendpackage', Pages.upload_package, name='sendpackage'),
    path('assistedtopurchase', Pages.upload_package, name='assistedtopurchase'),
    path('warehouse', Pages.warehouse, name='warehouse'),
    path('in-warehouse/', Pages.in_warehouse, name='in_warehouse'),
     path('in-warehouse/', views.in_warehouse, name='in_warehouse'),
    path('repackage-popup/<int:profile_id>', Pages.show_repackage_popup, name='show_repackage_popup'),
    path('process-repackage/<int:profile_id>', Pages.process_repackage, name='process_repackage'),
    path('forward-popup/<int:profile_id>', Pages.show_forward_popup, name='show_forward_popup'),
    path('process-forward/<int:profile_id>', Pages.process_forward, name='process_forward'),
    path('consolidate-popup/<int:profile_id>', Pages.show_consolidate_popup, name='show_consolidate_popup'),
    path('process-consolidate/<int:profile_id>', Pages.process_consolidate, name='process_consolidate'),
    path('admin/upload_package/', Pages.upload_package, name='upload_package'),
    path('admin/package_list/', Pages.admin_package_list, name='admin_package_list'),
    path('admin/send_package/<int:package_id>/', Pages.send_package, name='send_package'),
]
