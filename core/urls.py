from django.urls import path
from .views import home, form_vehiculo, form_mod_vehiculo,listar_mod_vehiculo,form_del_vehiculo, form_mantencion



urlpatterns = [
    path('', home, name="home"),
    path('listar-mod-vehiculo', listar_mod_vehiculo, name="listar_mod_vehiculo"),
    path('form-vehiculo', form_vehiculo, name="form_vehiculo"),
    path('form-mod-vehiculo/<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
    path('form-del-vehiculo/<id>', form_del_vehiculo, name="form_del_vehiculo"),
    path('form_mantencion', form_mantencion, name="form_mantencion"),
]   