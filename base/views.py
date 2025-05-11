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

    Args:
        generics (CreateAPIView): Inherits from DRF's CreateAPIView to provide create functionality.
    """
    serializer_class = ReminderSerializer

    def perform_create(self, serializer):
        """Saves a new reminder instance.

        Args:
            serializer (ReminderSerializer): The serializer containing validated reminder data.
        """
        serializer.save()


class ReminderListView(generics.ListAPIView):
    """
        View for listing all reminders.
        Retrieves and returns a list of all reminders, ordered by reminder time in descending order.

    Args:
        generics (ListAPIView): Inherits from DRF's ListAPIView to provide list functionality.
    """
    serializer_class = ReminderListSerializer

    def get_queryset(self):
        """
            Returns a queryset of all reminders ordered by reminder time descending.

        Returns:
            QuerySet: A queryset of RemindMeLater objects ordered by 'remind_at_time' in descending order.
        """
        return RemindMeLater.objects.all().order_by('-remind_at_time')