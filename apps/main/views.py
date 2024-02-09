from django.shortcuts import render

from apps.skins.models import Skin

# Create your views here.
def index(request):
    skins = Skin.objects.all()
    return render(request, 'core/index.html', {'skins': skins})