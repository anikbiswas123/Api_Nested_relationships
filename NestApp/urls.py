

from django.urls import path,include


from rest_framework.routers import DefaultRouter

from .views import *

router=DefaultRouter()

router.register('track',TrackList,basename='track')
router.register('album',AlbumList,basename='album')



urlpatterns = [
    
    path('',include(router.urls))
    
]
