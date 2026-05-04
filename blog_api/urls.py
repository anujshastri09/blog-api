from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ AUTH
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),

    # ✅ YOUR APPS
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),

    # ✅ SCHEMA
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # ✅ SWAGGER UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/posts/', include('posts.urls')),

]