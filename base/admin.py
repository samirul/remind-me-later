from django.contrib import admin
from .models import RemindMeLater

@admin.register(RemindMeLater)
class RemindMeLaterModelAdmin(admin.ModelAdmin):
    """Register User model.

    Args:
        admin (class ModelAdmin): For registering in the admin panel.
    """
    list_display = [
      'id', 'message','remind_at_time'
    ]
