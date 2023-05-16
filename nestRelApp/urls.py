from django.urls import path,include

from rest_framework.routers  import DefaultRouter

from .views import  *

router=DefaultRouter()

router.register('song',SongList,basename='song')
router.register('singer',SingerList,basename='singer')

urlpatterns = [
    # path('',include(router.urls))
    
]
