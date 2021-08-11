from django.urls import path

from .views import index, new_photo, photo_page


urlpatterns = [
    path('', index, name='index'),
    path('new/', new_photo, name='new_photo'),
    path('photo/<int:photo_id>/', photo_page, name='photo_page'),
]
