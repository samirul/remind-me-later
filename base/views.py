"""
    This module contains the views for the RemindMeLater app.
"""

from rest_framework import generics
from .serializers import ReminderSerializer, ReminderListSerializer
from .models import RemindMeLater

class ReminderCreateView(generics.CreateAPIView):
    serializer_class = ReminderSerializer

    def perform_create(self, serializer):
        serializer.save()


class ReminderListView(generics.ListAPIView):
    serializer_class = ReminderListSerializer

    def get_queryset(self):
        return RemindMeLater.objects.all().order_by('-remind_at_time')