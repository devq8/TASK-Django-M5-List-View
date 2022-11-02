from flights.serializer import FlightListSerializer, BookingListSerializer, BookingDetailSerializer, BookingUpdateSerializer, BookingCancelSerializer, BookingCreateSerializer
from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
import datetime

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.date.today())
    serializer_class = BookingListSerializer
    permission_classes = [IsAdminUser]

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    permission_classes = [IsAdminUser]
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

class BookingCreateView(CreateAPIView):
    serializer_class = BookingCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)