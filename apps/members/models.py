from uuid import uuid4
from PIL import Image

from django.db import models
from django.contrib.auth.models import User
# from apps.skins.models import Skin

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    skin = models.ForeignKey('skins.Skin', on_delete=models.SET_NULL, null=True, blank=True)
    head_skin = models.ImageField(upload_to='profiles/heads', null=True, blank=True)
    likes_skins = models.ManyToManyField('skins.Skin', related_name='liked_by', blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(self.skin)
        super().save(*args, **kwargs)
        print(self.skin)
        self.head_skin = self.create_head()
        super().save(*args, **kwargs)
        print(self.skin)

    
    def create_head(self):
        # if self.head_skin:
        #     return self.head_skin.url
        if self.skin:
            img = Image.open(self.skin.image.path).convert("RGBA")
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
            resized_head.save("media/skins/" + str(self.id) + ".png")
            return "skins/" + str(self.id) + ".png"
    
    def get_head(self):
        if self.head_skin:
            return self.head_skin.url
        return "/media/skins/default_head.png"