from uuid import uuid4


from django.db import models
from django.contrib.auth.models import User
# from apps.skins.models import Skin

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    skin = models.ForeignKey('skins.Skin', on_delete=models.SET_NULL, null=True, blank=True)
    likes_skins = models.ManyToManyField('skins.Skin', related_name='liked_by', blank=True)
    
    def __str__(self):
        return self.user.username
    
    
        
    def get_head(self):
        if self.skin:
            return self.skin.get_head()
        return "/media/skins/default_head.png"