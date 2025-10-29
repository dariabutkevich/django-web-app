from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ToyForm
from .models import Toy, Category, Favorite
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
# def toys_home(request):
#     toys = Toy.objects.order_by('name')
#     return render(request,'toys/toys_home.html', {'toys': toys})

def bearbricks(request):
    category = get_object_or_404(Category, name__iexact='BEARBRICKS')
    toys = Toy.objects.filter(category=category)
    return render(request, 'toys/toys_home.html', {'toys': toys, 'category': category})

def kaws(request):
    category = get_object_or_404(Category, name__iexact='KAWS')
    toys = Toy.objects.filter(category=category)
    return render(request, 'toys/toys_home.html', {'toys': toys, 'category': category})

def tud(request):
    category = get_object_or_404(Category, name__iexact='THE UGLY DUCK (TUD)')
    toys = Toy.objects.filter(category=category)
    return render(request, 'toys/toys_home.html', {'toys': toys, 'category': category})

def demengtoy(request):
    category = get_object_or_404(Category, name__iexact='DEMENG TOY')
    toys = Toy.objects.filter(category=category)
    return render(request, 'toys/toys_home.html', {'toys': toys, 'category': category})

def interioritems(request):
    category = get_object_or_404(Category, name__iexact='ПРЕДМЕТЫ ИНТЕРЬЕРА')
    toys = Toy.objects.filter(category=category)
    return render(request, 'toys/toys_home.html', {'toys': toys, 'category': category})

def create_toys(request):
    error = ''
    if request.method == 'POST':
        form = ToyForm(request.POST, request.FILES)  # Обязательно добавить request.FILES!
        if form.is_valid():
            form.save()
            return redirect('toys_home')
        else:
            error = 'Форма была неверной'

    form = ToyForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'toys/create_toys.html', data)


class ToysDetailView(LoginRequiredMixin, DetailView):
    model = Toy
    template_name = 'toys/detail_toy.html'
    context_object_name = 'toy'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        toy = self.get_object()
        user = self.request.user
        context['is_favorite'] = False
        if user.is_authenticated:
            context['is_favorite'] = toy.favorited_by.filter(user=user).exists()
        return context


class ToyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Toy
    form_class = ToyForm
    template_name = 'toys/edit_toy.html'
    success_url = reverse_lazy('toys_home')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser  # Только админ

class ToyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Toy
    template_name = 'toys/delete_toy.html'
    success_url = reverse_lazy('toys_home')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

def toys_home(request):
    toys = Toy.objects.all()
    category = request.GET.get('category')
    height = request.GET.get('height')
    material = request.GET.get('material')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    if category:
        toys = toys.filter(category__name__iexact=category)
    if height:
        toys = toys.filter(height__iexact=height)
    if material:
        toys = toys.filter(material__icontains=material)
    if date_from and date_to:
        toys = toys.filter(date__range=[date_from, date_to])

    context = {
        'toys': toys.distinct(),
        'category': category,
        'heights': Toy.objects.values_list('height', flat=True).distinct(),
        'materials': Toy.objects.values_list('material', flat=True).distinct(),
        'categories': Category.objects.all()
    }
    return render(request, 'toys/toys_home.html', context)

@login_required
def toggle_favorite(request, toy_id):
    toy = get_object_or_404(Toy, id=toy_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, toy=toy)
    if not created:
        favorite.delete()
        is_favorite = False
    else:
        is_favorite = True

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'is_favorite': is_favorite})
    else:
        return HttpResponseRedirect(reverse('toys_detail', args=[toy_id]))

@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('toy')
    toys = [f.toy for f in favorites]

    return render(request, 'toys/favorites.html', {'toys': toys})
