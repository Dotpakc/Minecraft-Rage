from django.db import models
from uuid import uuid4
from apps.members.models import Profile

# Create your models here.

class Skin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skins/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skins', null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Skin'
        verbose_name_plural = 'Skins'
        ordering = ['-created_at']