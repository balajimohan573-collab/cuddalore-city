from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    area = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
from django.db import models

class Report(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('progress', 'In Progress'),
        ('finished', 'Finished'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    area = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='reports/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
