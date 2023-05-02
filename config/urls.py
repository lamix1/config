from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import MarcaViewSet, CategoriaViewSet, CorViewSet, AcessorioViewSet, ModeloViewSet


router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)

router = DefaultRouter()
router.register(r"cor", CorViewSet)

router = DefaultRouter()
router.register(r"acessorio", AcessorioViewSet)

router = DefaultRouter()
router.register(r"modelo", ModeloViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
