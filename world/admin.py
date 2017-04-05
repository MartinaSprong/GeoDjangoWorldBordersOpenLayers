from django.contrib.gis import admin
from .models import WorldBorder

admin.site.register(WorldBorder, admin.GeoModelAdmin)

# register world border administratoin site
# admin.site.register(WorldBorder, admin.OSMGeoAdmin)

