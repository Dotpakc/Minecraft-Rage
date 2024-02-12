from django.shortcuts import render

from .models import Skin

# Create your views here.
def index(request):
    skins = Skin.objects.all()
    return render(request, 'skins/index.html', {'skins': skins})