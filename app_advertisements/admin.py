from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet
class AdvertisementAdmin(admin.ModelAdmin):
    list_display=['id','title', 'description', 'price', 'auction', 'created_at']
    list_filter=['auction','created_at']
    actions=['make_auction_as_false','make_auction_as_true']
    @admin.action(description='Убрать возможность торга')
    def  make_auction_as_false(self,request,queryset:QuerySet):
        queryset.update(auction=False)
    @admin.action(description='Добавить возможность торга')
    def  make_auction_as_true(self,request,queryset:QuerySet):
        queryset.update(auction=True)





admin.site.register(Advertisement, AdvertisementAdmin)


# Register your models here.
