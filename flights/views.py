from flights.serializer import FlightListSerializer, BookingListSerializer
from .models import Booking, Flight
from rest_framework.generics import ListAPIView
import datetime

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.date.today())
    serializer_class = BookingListSerializer