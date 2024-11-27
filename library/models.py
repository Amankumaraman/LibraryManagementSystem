from django.db import models

class User(models.Model):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='member')

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title
