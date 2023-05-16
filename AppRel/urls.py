from django.urls import  path,include

from rest_framework.routers import DefaultRouter
from .views import   *


router=DefaultRouter()

router.register('Singerlist',SingerViewSet,basename='Singerlist')
router.register('songlist',SongViewSet,basename='songlist')

urlpatterns = [
    
    # path('',include(router.urls))
    
]
