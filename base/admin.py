"""
  This module register models to admin panel.
"""

from django.contrib import admin
from .models import RemindMeLater

@admin.register(RemindMeLater)
class RemindMeLaterModelAdmin(admin.ModelAdmin):
    """
      Register RemindMeLater model.
      admin (class ModelAdmin): For registering models in the admin panel.
    """
    list_display = [
      'id', 'message','remind_at_time'
    ]
