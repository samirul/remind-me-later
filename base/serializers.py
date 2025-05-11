from datetime import datetime
from django.utils import timezone
from rest_framework import serializers
from .models import RemindMeLater


class ReminderSerializer(serializers.ModelSerializer):
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)
    class Meta:
        model = RemindMeLater
        fields = ['id', 'remind_at_time', 'date', 'time', 'message']
        read_only_fields = ['remind_at_time']

    def create(self, validated_data):
        date = validated_data.pop('date')
        time = validated_data.pop('time')
        remind_at = datetime.combine(date, time)
        remind_at = timezone.make_aware(remind_at)
        validated_data['remind_at_time'] = remind_at
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        remind_me_object = instance.remind_at_time
        representation['remind_at_time'] = remind_me_object.strftime('%Y-%m-%d %I:%M %p')
        return representation
    
class ReminderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemindMeLater
        fields = ['id', 'remind_at_time', 'message']

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        remind_me_object = instance.remind_at_time
        representation['remind_at_time'] = remind_me_object.strftime('%Y-%m-%d %I:%M %p')
        return representation
