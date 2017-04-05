from django.shortcuts import render, redirect
from world.models import WorldBorder
from world.forms import WorldBorderForm
from world.vectorformats.Formats import Django, GeoJSON
from django.core.serializers import serialize

def index(request):
    # enter = "start exploring"
    # context = { 'enter': enter }
    return render(request, 'world/index.html')

def explore(request):
    form = WorldBorderForm()
    context = { 'form': form }
    return render(request, 'world/explore.html', context)

def geojson(request):
    # not using serializer! For creating GeoJSON from postGIS database
    # ly = WorldBorder.objects.all() # for selection of all countries 
    ly = WorldBorder.objects.filter(name = "Russia") # for selection of just one country
    djf = Django.Django(geodjango='mpoly', properties=['name'])
    geoj = GeoJSON.GeoJSON()
    my_geojson = geoj.encode(djf.decode(ly))   
    return render(request, "world/map.html", {'my_geojson': my_geojson})

    # using serializer! For creating GeoJSON from postGIS database
    # my_geojson = serialize('geojson', 
    #              WorldBorder.objects.all(),
    #              geometry_field='mpoly',
    #              fields=('name', 'mpoly'))
    # return render(request, "world/map.html", {'my_geojson': my_geojson})

