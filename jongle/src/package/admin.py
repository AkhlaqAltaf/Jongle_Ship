from django.contrib import admin

from interface.admin import admin_site
from .models import WarehousePackage , Profile , ReadyToShip , InProgressPackage


admin_site.register(WarehousePackage)

admin_site.register(ReadyToShip)
admin_site.register(InProgressPackage)


admin_site.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     search_fields = ['user__username', 'user__email']
#     list_display = ['user', 'package_image', 'package_dimensions', 'package_weight']

