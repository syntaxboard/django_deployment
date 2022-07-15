# djangomodels/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_db_routing.urls')),
    path('app_db_routing/', include('app_db_routing.urls')),
    path('app_db_serializer/', include('app_db_serializer.urls')),
    path('app_db_custom_sql/', include('app_db_custom_sql.urls')),
    # path('app_db_querysets/', include('app_db_querysets')),
]
