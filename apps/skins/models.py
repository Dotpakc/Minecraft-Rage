from uuid import uuid4
from PIL import Image

from django.db import models

from apps.members.models import Profile

# Create your models here.

class Skin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skins/images')
    image_head = models.ImageField(upload_to='skins/images/head/', null=True, blank=True)
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
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.image_head = self.create_head()
        super().save(*args, **kwargs)
    
    def create_head(self):
        img = Image.open(self.image.path).convert("RGBA")
        x, y = img.size
        standard_size = [(8, 8, 16, 16), (40, 8, 48, 16), 128]
        head_coord = []
        helm_coord = []
        for i in standard_size[0]:
            head_coord.append(i * (x // 64))
        for i in standard_size[1]:
            helm_coord.append(i * (x // 64))
        head = img.crop(head_coord)
        helm = img.crop(helm_coord)
        k = standard_size[2] // (x // 64)
        x, y = head.size
        head.paste(helm, (0, 0, x, y), helm)
        new_width = x * k
        new_height = y * k
        resized_head = Image.new('RGBA', (new_width, new_height))
        for i in range(x):
            for j in range(y):
                pixel = head.getpixel((i, j))
                resized_head.paste(pixel, (i * k, j * k, (i + 1) * k, (j + 1) * k))
        resized_head.save("media/skins/head/" + str(self.id) + ".png")
        return "skins/head" + str(self.id) + ".png"