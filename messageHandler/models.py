from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
     subject = models.CharField(max_length=300, default='0000000')
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)
     is_read = models.BooleanField(default=False)

     def __str__(self):
           return self.message



class Meta:
   ordering = ('timestamp',)



