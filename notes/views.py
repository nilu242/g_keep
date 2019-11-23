from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def notes_view(request):
    return HttpResponse('notes list')

def reminders_view(request):
    return HttpResponse('reminders list')

def archive_view(request):
    return HttpResponse('archive list')

def trash_view(request):
    return HttpResponse('trash list')