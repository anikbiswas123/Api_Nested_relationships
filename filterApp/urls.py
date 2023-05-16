from django.urls import path,include

from .views import StudentModelViewset,StudentList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Student', StudentModelViewset, basename='Student')
urlpatterns = [
    # path('',include(router.urls)),
    #   path('auth/',include('rest_framework.urls',namespace='rest_framework')),

    # path('studentlist/',StudentList.as_view(),name='studentlist')
]