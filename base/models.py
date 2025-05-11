"""
   This module contains models for Reminder app. 
"""

import uuid
from django.db import models

class RemindMeLater(models.Model):
    """
        Stores the reminder message and the date-time
        inside a database at which the reminder should occur.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    remind_at_time = models.DateTimeField()
    message = models.TextField(max_length=500)
    objects = models.Manager()


    def __str__(self):
        """Returns a string representation of the reminder message."""
        return str(self.message)
