import uuid
from django.db import models

class RemindMeLater(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    remind_at_time = models.DateTimeField()
    message = models.TextField(max_length=500)
    objects = models.Manager()


    def __str__(self):
        return str(self.message)
