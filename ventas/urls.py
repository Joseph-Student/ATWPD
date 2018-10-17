from django.urls import path

from ventas import views

app_name = 'ventas'
urlpatterns = [
    path('articulos/', views.ArticuloListView.as_view(), name='articulo-list'),
    path('articulos/create/', views.ArticuloCreateView.as_view(),
         name='articulo-create'),
]
