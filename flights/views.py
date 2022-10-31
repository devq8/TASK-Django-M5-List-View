from flights.serializer import FlightListSerializer, BookingListSerializer, BookingDetailSerializer, BookingUpdateSerializer, BookingCancelSerializer
from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
import datetime

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.date.today())
    serializer_class = BookingListSerializer

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingCancelView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCancelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
