from django.contrib import admin
from service.models import Services
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_tittle','service_des')

admin.site.register(Services,ServiceAdmin)
# Register your models here.
