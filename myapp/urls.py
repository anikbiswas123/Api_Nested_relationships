
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('app.urls')),
    # path('',include('filterApp.urls')),
    # path('',include('filterapp1.urls')),
    # path('',include('SearchApp.urls')),
    # path('',include('paginationApp.urls')),
    # path('',include('AppRel.urls')),
    # path('',include('nestRelApp.urls')),
    path('',include('NestApp.urls')),
    
]
