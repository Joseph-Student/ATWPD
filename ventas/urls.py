from django.urls import path, include

from ventas import views

app_name = 'ventas'
# models_name = ['articulo', 'cliente', 'detVentas']
# patterns = []
#
# for name in models_name:
#     patterns.append([
#         path('', exec('views.{0}ListView.as_view()'.format(name.capitalize())), name='{}-list'.format(name)),
#         path('create/', views.ArticuloCreateView.as_view(),
#              name='articulo-create'),
#         path('<int:pk>/detail/', views.ArticuloDetailView.as_view(),
#              name='articulo-detail'),
#         path('<int:pk>/update/', views.ArticuloUpdateView.as_view(),
#              name='articulo-update'),
#         path('<int:pk>/delete/', views.ArticuloDeleteView.as_view(),
#              name='articulo-delete')
#     ])

# urls de articulos
articulo_patterns = [
    path('', views.ArticuloListView.as_view(), name='articulo-list'),
    path('create/', views.ArticuloCreateView.as_view(),
         name='articulo-create'),
    path('<int:pk>/detail/', views.ArticuloDetailView.as_view(),
         name='articulo-detail'),
    path('<int:pk>/update/', views.ArticuloUpdateView.as_view(),
         name='articulo-update'),
    path('<int:pk>/delete/', views.ArticuloDeleteView.as_view(),
         name='articulo-delete'),
]

# urls de Cliente
cliente_patterns = [
    path('', views.ClienteListView.as_view(), name='cliente-list'),
    path('create/', views.ClienteCreateView.as_view(),
         name='cliente-create'),
    path('<int:pk>/detail/', views.ClienteDetailView.as_view(),
         name='cliente-detail'),
    path('<int:pk>/update/', views.ClienteUpdateView.as_view(),
         name='cliente-update'),
    path('<int:pk>/delete/', views.ClienteDeleteView.as_view(),
         name='cliente-delete'),
]

# urls de Detalles de Ventas
detventa_patterns = [
    path('', views.DetVentaListView.as_view(), name='detventa-list'),
    path('create/', views.DetVentaCreateView.as_view(),
         name='detventa-create'),
    path('<int:pk>/detail/', views.DetVentaDetailView.as_view(),
         name='detventa-detail'),
    path('<int:pk>/update/', views.DetVentaUpdateView.as_view(),
         name='detventa-update'),
    path('<int:pk>/delete/', views.DetVentaDeleteView.as_view(),
         name='detventa-delete'),
]

urlpatterns = [
    path('articulos/', include(articulo_patterns)),
    path('clientes/', include(cliente_patterns)),
    path('detventas/', include(detventa_patterns)),
]
