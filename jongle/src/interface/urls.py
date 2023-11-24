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
from interface.views import Pages
app_name = "interface"
urlpatterns = [

    path('',Pages.home ,name='home'),
    path('store',Pages.store_list, name='store'),
    path('help' , Pages.help ,name='help'),
    path('printbarcode' , Pages.generate_barcode ,name='printbarcode'),
    path('calculator', Pages.calculate_price_view, name='calculator'),
    path('dhlapi' , Pages.dhlApi , name ='dhlapi'),
    path('dhlapi/tracking' , Pages.tracking_page , name ='dhlapi'),
    path('get_tracking_data' , Pages.get_tracking_data , name ='get_tracking_data'),
    path('upload_shipment', Pages.upload_shipment, name='upload_shipment'),
    path('path/to/fetch/notifications/', Pages.fetch_notifications, name='fetch-notifications'),
    path('path/to/mark/notifications/as/read/', Pages.mark_notifications_as_read, name='mark-notifications-as-read'),

]
