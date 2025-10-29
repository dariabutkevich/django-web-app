from django.urls import path
from . import views

urlpatterns = [
    path('', views.toys_home, name='toys_home'),
    path('create_toys/', views.create_toys, name='create_toys'),
    path('bearbricks/', views.bearbricks, name='bearbricks'),
    path('kaws/', views.kaws, name='kaws'),
    path('tud/', views.tud, name='tud'),
    path('demengtoy/', views.demengtoy, name='demengtoy'),
    path('interioritems/', views.interioritems, name='interioritems'),
    path('<int:pk>', views.ToysDetailView.as_view(), name='toys_detail'),
    path('bearbricks/<int:pk>', views.ToysDetailView.as_view(), name='toys_detail'),
    path('<int:pk>/edit/', views.ToyUpdateView.as_view(), name='toy_update'),
    path('<int:pk>/delete/', views.ToyDeleteView.as_view(), name='toy_delete'),
    path('toy/<int:toy_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorites_list, name='favorites_list'),

]
