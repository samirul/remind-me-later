"""
    This module contains the views for the RemindMeLater app.
"""

from rest_framework import generics
from .serializers import ReminderSerializer, ReminderListSerializer
from .models import RemindMeLater

class ReminderCreateView(generics.CreateAPIView):
    """
        View for creating new reminders.
        This view uses the ReminderSerializer to validate and save the reminder data
        using POST requests.
    """
    serializer_class = ReminderSerializer

    def perform_create(self, serializer):
        """ saves a new reminder instance."""
        serializer.save()


class ReminderListView(generics.ListAPIView):
    """
        View for listing all reminders using GET requests.
        Retrieves and returns a list of all reminders, ordered by reminder time in descending order.
    """
    serializer_class = ReminderListSerializer

    def get_queryset(self):
        """Returns a queryset of all reminders ordered by reminder time descending."""
        return RemindMeLater.objects.all().order_by('-remind_at_time')