from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tigers/', views.tigers_index, name='tigers_index'),
  path('tigers/<int:tiger_id>/', views.tigers_detail, name='tigers_detail'),
  path('tigers/create/', views.TigerCreate.as_view(), name='tigers_create'),
  path('tigers/<int:pk>/update/', views.TigerUpdate.as_view(), name='tigers_update'),
  path('tigers/<int:pk>/delete/', views.TigerDelete.as_view(), name='tigers_delete'),
  path('tigers/<int:tiger_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]