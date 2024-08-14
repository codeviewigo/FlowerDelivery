from django.db import models

class Manager(models.Model):
    chat_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, default='UserName')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.chat_id
