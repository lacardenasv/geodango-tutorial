from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from shops.models import Shop, Theatre


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')


@admin.register(Theatre)
class TheatreAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')


