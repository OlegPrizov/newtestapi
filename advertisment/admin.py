from django.contrib import admin

from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'views', 'position')

admin.site.register(Advertisement, AdvertisementAdmin)
