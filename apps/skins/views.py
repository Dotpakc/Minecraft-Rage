from django.shortcuts import render, redirect, get_object_or_404

from .models import Skin
from .forms import SkinForm

# Create your views here.
def index(request):
    skins = Skin.objects.all()
    skinAddform = SkinForm()
    return render(request, 'skins/index.html', {'skins': skins, 'skinAddform': skinAddform})


def create(request):
    if request.method == 'POST':
        form = SkinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('skins:index')
    else:
        form = SkinForm()
    return render(request, 'skins/create.html', {'form': form})


def detail(request, id):
    skin = get_object_or_404(Skin, id=id)
    return render(request, 'skins/detail.html', {'skin': skin})