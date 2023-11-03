from django.urls import path

from .views import list_manga, create_manga, delete_manga, views_usuario, create_usuario, vista_u

urlpatterns = [
    path('', list_manga),
    path('nuevo/', create_manga, name='nuevo_manga'),
    path('delete_manga/<int:manga_id>/', delete_manga, name='delete_manga'),
    path('vista_usuario/', views_usuario, name = 'vista_usuario'),
    path('create_usuario/', create_usuario, name='create_usuario'),
    path('vista_u/', vista_u, name = 'vista_u')

]