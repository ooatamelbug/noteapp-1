from django.db import models
from django.contrib.auth.admin import User
# Create your models here.


class Note (models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    alarm = models.DateTimeField()
    type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
