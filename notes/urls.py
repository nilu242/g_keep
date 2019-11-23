from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_view, name="notes_list"),
    path('reminders/', views.reminders_view, name="reminders_list"),
    path('archive/', views.archive_view, name="archive_list"),
    path('trash/', views.trash_view, name="trash_list"),
]
