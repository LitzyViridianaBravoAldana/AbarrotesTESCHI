from django.urls import path
from api.views import sign_in, sign_up, index_9, team, biblioteca, genero1, editorial1
#from tasks import views

urlpatterns = [
    # Ruta para la página index_9
    #path('index_9.html', index_9.as_view(), name='index_9'),
    path('index_9/', index_9.as_view(), name='index_9'),


    # Ruta para la URL raíz (puede ser una de las páginas anteriores)
    #path('', index_9.as_view(), name='index_9_root'),

    # Ruta para la página de inicio de sesión
    path('sign_in/', sign_in.as_view(), name='sign_in'),
    
    # Ruta para la página de registro
    path('sign_up/', sign_up.as_view(), name='sign_up'),
    #path('sign_up.html', views.sign_up, name='sign_up'),
    
    # Ruta para la página de Team de autores
    path('team/', team.as_view(), name='team'),

    # Ruta para la página de Team de autores
    path('biblioteca/', biblioteca.as_view(), name='biblioteca'),

    # Ruta para la página de Team de autores
    path('genero1/', genero1.as_view(), name='genero1'),

     # Ruta para la página de Team de autores
    path('editorial1/', editorial1.as_view(), name='editorial1'),
]
