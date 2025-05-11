"""
    This module contains serializers for the RemindMeLater model.
    It includes serializers for creating and listing reminders.
"""

from datetime import datetime
from django.utils import timezone
from rest_framework import serializers
from .models import RemindMeLater


class ReminderSerializer(serializers.ModelSerializer):
    """
        This serializer is for creating and representing reminder instances.
        Handles the conversion of separate date and time fields into a single datetime and formats output for reminders.
    """
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)
    class Meta:
        """
            Meta class for ReminderSerializer.
            Specifies the model and fields to be used in the serializer.
        """
        model = RemindMeLater
        fields = ['id', 'remind_at_time', 'date', 'time', 'message']
        read_only_fields = ['remind_at_time']

    def create(self, validated_data):
        """
            Creates a new reminder instance from validated data.
            Combines the provided date and time into a single aware datetime for the reminder.
        """
        date = validated_data.pop('date')
        time = validated_data.pop('time')
        remind_at = datetime.combine(date, time)
        remind_at = timezone.make_aware(remind_at)
        validated_data['remind_at_time'] = remind_at
        return super().create(validated_data)
    
    def to_representation(self, instance):
        """
            Returns a dictionary representation of the reminder instance.
            Formats the 'remind_at_time' field as a human-readable string.
        """
        representation =  super().to_representation(instance)
        remind_me_object = instance.remind_at_time
        representation['remind_at_time'] = remind_me_object.strftime('%Y-%m-%d %I:%M %p')
        return representation
    
class ReminderListSerializer(serializers.ModelSerializer):
    """
        Serializer for listing reminder instances.
        Formats the output of reminder objects for display in reminder lists.
    """
    class Meta:
        """
            Meta class for ReminderListSerializer.
            Specifies the model and fields to be used in the serializer.
        """
        model = RemindMeLater
        fields = ['id', 'remind_at_time', 'message']

    def to_representation(self, instance):
        """
            Returns a dictionary representation of the reminder instance.
            Formats the 'remind_at_time' field as a human-readable string.
        """
        representation =  super().to_representation(instance)
        remind_me_object = instance.remind_at_time
        representation['remind_at_time'] = remind_me_object.strftime('%Y-%m-%d %I:%M %p')
        return representation
