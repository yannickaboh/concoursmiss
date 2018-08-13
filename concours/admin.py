from django.contrib import admin
from . import models
from django.conf import settings

# Register your models here.


class GprovinceAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'longitude', 'latitude',)
    list_filter    = ('nom', 'longitude', 'latitude',)

    fieldsets = (
        (None, {
            'fields': ('nom', 'longitude', 'latitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('concours/css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'concours/js/admin/location_picker.js',
            )


admin.site.register(models.Gprovince, GprovinceAdmin)
