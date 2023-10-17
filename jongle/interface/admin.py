from django.contrib import admin 
from interface.models import *

from django.contrib.admin import AdminSite

from django.contrib import admin



from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import quote
from django.contrib.admin import AdminSite



class CustomAdminSite(AdminSite):

    site_header = 'JONGLE Admin Site'
    search_fields = ['user__username']

admin_site = CustomAdminSite()


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    search_fields = ['unique_id', 'user__username', 'user__email']
    list_display = ['unique_id', 'user', 'name', 'address', 'phone', 'email', 'upload_package_link' , 'send_email_link']

    def upload_package_link(self, obj):

        url = reverse('packages:uploadpackages')
        object = CustomUser.objects.get(name= obj.user.username)
        link = f'<a href="{url}?username={obj.user.username}&destinationCountry={object.destinationCountry}" class="btn btn-link">Upload Package</a>'
        return format_html(link)

    def send_email_link(self , obj):
        
        
        object = CustomUser.objects.get(name= obj.user.username)
        email_ = object.email
        print("Email Is Here ",email_)
        email = quote(email_)
        print(email)
        url = reverse('send_message')
        link = f'<a href="{url}?username={obj.user.username}&email = {email}" class="btn btn-link">Send Message</a>'
        return format_html(link)

    upload_package_link.short_description = 'uploadpackages'

    send_email_link.short_description = 'send message'








# Register the models with the custom admin site







@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'logo_url', 'website_url']



admin_site.register(BaseUser)
admin_site.register(CustomUser, CustomUserAdmin)

admin_site.register(Store, StoreAdmin)

admin_site.register(PricePerKg)
admin_site.register(Notification)
