from django.urls import path
from . import views

app_name = 'open'

urlpatterns = [
    path('', views.org_list),
    # Создание.
    path(
        'create/',
        views.OpenData_created,
        name='create'
    ),
    # Редактирование.
    path(
        'posts/<post_id>/edit/',
        views.OpenData_edit,
        name='post_edit'
    ),
    # Успешное добавление.
    path(
        'created',
        views.created,
        name='created'
    ),
]
