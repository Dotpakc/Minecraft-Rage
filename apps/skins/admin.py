from django.contrib import admin

from .models import Skin, Tag
# Register your models here.



class TagInline(admin.TabularInline):
    model = Skin.tags.through
    extra = 1

class SkinInline(admin.TabularInline):
    model = Tag.skins.through   
    extra = 1



@admin.register(Skin)
class SkinAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    list_display = ['name', 'author', 'likes', 'status']
  
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [SkinInline]
    list_display = ['name']
   
    