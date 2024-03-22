from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Skin
from .forms import SkinForm

# Create your views here.
@login_required
def index(request):
    skins = Skin.objects.all()
    paginator = Paginator(skins, 4)
    page = request.GET.get('page')
    skins = paginator.get_page(page)
    skinAddform = SkinForm()
    return render(request, 'skins/index.html', {'skins': skins, 'skinAddform': skinAddform})

@login_required
def create(request):
    if request.method == 'POST':
        form = SkinForm(request.POST, request.FILES)
        if form.is_valid():
            skin = form.save(commit=False)
            skin.author = request.user.profile
            skin.likes = 1
            skin.save()
            request.user.profile.skin = skin
            request.user.profile.likes_skins.add(skin)
            request.user.profile.save()
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

@login_required
def like(request, id):
    skin = get_object_or_404(Skin, id=id)
    profile = request.user.profile
    if skin not in profile.likes_skins.all():
        profile.likes_skins.add(skin)
        skin.likes += 1
        skin.save()
    profile.skin = skin
    profile.save()
    return redirect('members:profile', id=profile.id)