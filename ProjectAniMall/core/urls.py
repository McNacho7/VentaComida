from urllib.parse import urlparse
from django.urls import path
from .views import index, gatos, accesorios, formulariocontacto, login, mostrarperros, perros, listarproductos, carro,formagregar,formModificar


urlpatterns = [
   path('', index,name="index") ,
   path('gatos/', gatos,name="gatos"),
   path('accesorios/', accesorios,name="accesorios"), 
   path('formulariocontacto/', formulariocontacto,name="formulariocontacto"), #se modifico nombre va sin el "-"
   path('login/', login,name="login"),
   path('mostrarperros/', mostrarperros,name="mostrarperros"),
   path('perros/', perros,name="perros"),
   path('listarproductos/', listarproductos,name="listarproductos"),
   path('carro/', carro,name="carro"),
   path('formagregar',formagregar, name="formagregar" ),
   path('formModificar',formModificar, name="formModificar" ),
   

   
]