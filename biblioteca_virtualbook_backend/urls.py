"""biblioteca_virtualbook_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from categorias import views as categorias_view
from django.urls import path, include, re_path
from accounts import views as accounts_views
from autores import views as autores_views
from django.conf.urls.static import static 
from listas import views as listas_views
from libros import views as libros_views
from rest_framework import routers
from django.contrib import admin
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'books', libros_views.LibrosView)
router.register(r'autores', autores_views.AutoresView)
router.register(r'categorys', categorias_view.CategoryView)
router.register(r'ver_todos_usuarios',accounts_views.CustomerViewTotal)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"api/",include(router.urls)),
    path(r'api-token-obtain/', obtain_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path(r'api/genereteId/', listas_views.GenerateShippingCart),
    path(r'api/CrearLista/renta',listas_views.ListaRentaCreateview),
    path(r'api/CrearLista/deseos',listas_views.ListaDeseosCreateview),
    path(r'api/accounts/register/', accounts_views.customerRegister),
    path(r'api/accounts/', accounts_views.CustomerView.as_view({ "get":"retrieve" , "put":"retrieve"})),
    re_path(r'api/deleteLista/one/renta/(?P<id_item>\d+)/', listas_views.rentados_delete_item),
    re_path(r'api/deleteLista/one/deseos/(?P<id_item>\d+)/', listas_views.deseos_delete_item), 
    re_path(r'api/deleteLista/deseos/(?P<id_cart>\d+)/', listas_views.ListaDeseosDeleteView),
    re_path(r'api/deleteLista/renta/(?P<id_cart>\d+)/', listas_views.ListaRentaDeleteView),
    re_path(r'api/books/search/(?P<palabra_clave>\w+)/',libros_views.BookssSearchView),
    re_path(r'api/rentas/checkDates/(?P<cart_id>\d+)/', listas_views.revisionFechas),
    re_path(r'api/getLista/deseos/(?P<id_cart>\d+)/', listas_views.ListaDeseosView),
    re_path(r'api/getLista/renta/(?P<id_cart>\d+)/', listas_views.ListaRentaView),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)