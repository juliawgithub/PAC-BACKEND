# urls.py
from django.urls import path
from .views import criar_plano
from . import views
from plano import views as plano_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<str:municipio>/criar-plano/', views.criar_plano, name='criar_plano'),
    path('', plano_views.index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
