from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    MESSAGE_TEXT = (
        ('B', 'Bro!'),
        ('S', 'Sis!')
    )
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=4, choices=MESSAGE_TEXT, default=None)
    id = models.BigAutoField(default=None, primary_key=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['date']
