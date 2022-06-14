from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from django.contrib import admin
from django.urls import path, include, re_path

from users.views import CustomTokenObtainPairView


schema_view = get_schema_view(
    openapi.Info(
        title="Angular Practice API",
        default_version='v1',
        description="Practice API's for NG-Ecommerce project and angular practice projects",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tareqmonwer137@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('tasks/', include('tasks.urls')),
    path('', include('users.urls')),
]
