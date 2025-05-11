from django.urls import path
from .views import ReminderCreateView, ReminderListView
urlpatterns = [
    path('api/new-reminder/', ReminderCreateView.as_view(), name='new-reminder'),
    path('api/reminders/', ReminderListView.as_view(), name='reminders'),
]