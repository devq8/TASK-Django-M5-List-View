from django.contrib import admin
from flights.models import Flight, Booking

# Register your models here.
admin.site.register([Flight, Booking])