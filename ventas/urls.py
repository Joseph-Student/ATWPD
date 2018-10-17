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
    path('<int:pk>/precio', views.ArticuloAjaxView.as_view(),
         name='articulo-precio'),
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
venta_patterns = [
    path('', views.VentaListView.as_view(), name='venta-list'),
    path('create/', views.VentaCreateView.as_view(),
         name='venta-create'),
    path('<int:pk>/detail/', views.VentaDetailView.as_view(),
         name='venta-detail'),
    path('<int:pk>/update/', views.VentaUpdateView.as_view(),
         name='venta-update'),
    path('<int:pk>/delete/', views.VentaDeleteView.as_view(),
         name='venta-delete'),

]

urlpatterns = [
    path('articulos/', include(articulo_patterns)),
    path('clientes/', include(cliente_patterns)),
    path('ventas/', include(venta_patterns)),
]
