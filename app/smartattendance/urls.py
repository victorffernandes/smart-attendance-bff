"""
URL configuration for smartattendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import Turma, Usuario, Historico, Atestado, Presenca, Chamada


router = DefaultRouter()
router.register('usuario', Usuario.ViewSet, 'usuario')
router.register('turma', Turma.ViewSet, 'turma')
router.register('historico', Historico.ViewSet, 'historico')
router.register('atestado', Atestado.ViewSet, 'atestado')
router.register('chamada', Chamada.ViewSet, 'chamada')
router.register('presenca', Presenca.ViewSet, 'presenca')

#Schema de view para o Swagger
#Autor: Mauricio
#Data: 13/10
schema_view = get_schema_view(
   openapi.Info(
      title="Smart Attendance API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License")
   ),
   url='https://smartattendances.online/',
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    re_path('^', include(router.urls)),
]
