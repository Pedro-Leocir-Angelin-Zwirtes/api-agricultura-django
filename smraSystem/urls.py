from django.contrib import admin
from django.urls import path, include, re_path

#DRF YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#ROTAS
from rest_framework.routers import DefaultRouter
from agricultor.api import viewsets as agricultorviewsets
from fazenda.api import viewsets as fazendaviewsets
from talhao.api import viewsets as talhaoviewsets
from atividadeAgricola.api import viewsets as atividadeagricolaviewsets
from recomendacao.api import viewsets as recomendacaoviewsets

route = DefaultRouter()
route.register(r'agricultores', agricultorviewsets.AgricultorViewSets, basename="Agricultores")
route.register(r'fazendas', fazendaviewsets.FazendasViewSets, basename="Fazendas")
route.register(r'talhoes', talhaoviewsets.TalhoesViewSets, basename="Talhoes")
route.register(r'atividadesAgricola', atividadeagricolaviewsets.AtividadesAgricolasViewSets, basename="AtividadesAgricola")
route.register(r'recomendacoes', recomendacaoviewsets.RecomendacoesViewSets, basename="Recomendacoes")


#DRF YASG
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),

    #drf_yasg
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
