from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=65)
    password2 = models.CharField(max_length=65)

    def __repr__(self):
        return f"User named '{self.username}'"

    def __str__(self):
        return self.username
    

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to = 'uploads/',blank = True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name