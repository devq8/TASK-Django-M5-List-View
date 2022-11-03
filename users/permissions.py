from rest_framework.permissions import BasePermission
from datetime import datetime, timezone, timedelta

class IsOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        
        return request.user.is_staff or obj.user == request.user

class IsAllowedBooking(BasePermission):
    message = "You can't change or cancel your booking unless it's more than 3 days of departure."

    def has_object_permission(self, request, view, obj):
        delta = timedelta(days=3)
        today = datetime.today().date()
        flight_date = obj.date
        
        return (today+delta) < flight_date