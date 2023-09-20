from django.urls import path
from api.views import sign_in, sign_up, index_9

urlpatterns = [
    # Ruta para la página de inicio de sesión
    path('sign_in.html', sign_in.as_view(), name='sign_in'),
    
    # Ruta para la página de registro
    path('sign_up.html', sign_up.as_view(), name='sign_up'),
    
    # Ruta para la página index_9
    path('index_9.html', index_9.as_view(), name='index_9'),
    
    # Ruta para la URL raíz (puede ser una de las páginas anteriores)
    path('', index_9.as_view(), name='index_9_root'),
]
