from django.db import models
from django.contrib.auth.models import User

class NotesPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # title of notes page
    title = models.CharField(max_length=100)
    # body of notes page
    body = models.TextField(null=True, blank=True)
    # gets timestamp of created notes page
    created = models.DateTimeField(auto_now_add=True)
