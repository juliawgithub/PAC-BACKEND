from django.urls import path
from .views import login_view, login_success

urlpatterns = [
    path('', login_view, name='login'),  # Remova 'admin/' para evitar duplicação
    path('login/success/', login_success, name='login_success'),
]
