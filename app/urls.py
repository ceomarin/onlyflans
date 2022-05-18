from django.urls import path
from .views import home,registro,contacto,agregar_producto,listar_productos,\
    modificar_producto,eliminar_producto

urlpatterns = [
    path('',home,name='home'),
    path('registro/',registro,name='registro'),
    path('contacto/',contacto,name='contacto'),
    path('listar-productos/', listar_productos,name='listar_productos'),
    path('agregar-producto/', agregar_producto,name='agregar_producto'),
    path('modificar-producto/<id>/', modificar_producto,name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto,name='eliminar_producto'),
]