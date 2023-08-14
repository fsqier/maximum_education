from django.contrib import admin
from .models import Advertisement
class AdvertisementAdmin(admin.ModelAdmin):
    list_display=['id','title', 'description', 'price', 'auction', 'created_at']
admin.site.register(Advertisement, AdvertisementAdmin)


# Register your models here.
