from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Skin
from .forms import SkinForm

# Create your views here.
@login_required
def index(request):
    skins = Skin.objects.all()
    skinAddform = SkinForm()
    return render(request, 'skins/index.html', {'skins': skins, 'skinAddform': skinAddform})

@login_required
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
    six_random_skins = Skin.objects.order_by('?')[:6]
    context = {
        'skin': skin,
        'six_random_skins': six_random_skins
    }
    
    return render(request, 'skins/detail.html', context)