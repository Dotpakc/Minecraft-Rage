import os

from uuid import uuid4
from PIL import Image

from django.db import models

from apps.members.models import Profile

# Create your models here.

def skin_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}.{ext}"
    return os.path.join('skins/images', filename)

class Skin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=skin_image_filename)
    image_head = models.ImageField(upload_to='skins/images/head/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skins', null=True, default=None)

    tags = models.ManyToManyField(
    to='skins.Tag',
    through='skins.SkinTag',
    related_name='skins',
    blank=True,
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Skin'
        verbose_name_plural = 'Skins'
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.image_head:  # Проверяем, не существует ли уже головы для этого скина
            self.create_head()
            super().save(*args, **kwargs)
    
    def create_head(self):
        img = Image.open(self.image.path).convert("RGBA")
        x, y = img.size
        standard_size = [(8, 8, 16, 16), (40, 8, 48, 16), 128]
        head_coord = [i * (x // 64) for i in standard_size[0]]
        helm_coord = [i * (x // 64) for i in standard_size[1]]
        
        head = img.crop(head_coord)
        helm = img.crop(helm_coord)
        k = standard_size[2] // (x // 64)
        
        x, y = head.size
        head.paste(helm, (0, 0, x, y), helm)
        
        new_width = x * k
        new_height = y * k
        resized_head = head.resize((new_width, new_height), Image.NEAREST)
        
        # Получаем путь для сохранения
        head_filename = os.path.join('skins/images/head/', f"{self.id}.png")
        if not os.path.exists('media/skins/images/head/'):
            os.makedirs('media/skins/images/head/')
        resized_head.save(f"media/{head_filename}")
        
        # Присваиваем значение полю image_head
        self.image_head.name = head_filename
        
    def get_head(self):
        if not self.image_head:
            self.create_head()
            self.save()
        return self.image_head.url
    
class SkinTag(models.Model):
    skin = models.ForeignKey(Skin, on_delete=models.CASCADE)
    tag = models.ForeignKey('skins.Tag', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.skin.name} - {self.tag.name}"
    
    class Meta:
        verbose_name = 'Skin-Tag'
        verbose_name_plural = 'Skin-Tags'
        ordering = ['skin']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']