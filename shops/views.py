from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

from shops.models import Theatre


class Home(generic.TemplateView):
    template_name = 'home.html'


class TheatreHome(generic.ListView):
    model = Theatre
    context_object_name = 'theatres'
    user_location = None
    template_name = 'threatres_list.html'

    def get_queryset(self):
        latitude = float(self.kwargs.get('latitude', 0))
        longitude = float(self.kwargs.get('longitude', 0))
        self.user_location = Point(longitude, latitude, srid=4326)
        queryset = Theatre.objects.annotate(distance=Distance('location', self.user_location)).order_by('distance')[0:6]
        return queryset
