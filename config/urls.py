from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('aaa.urls.auth_urls')),
    path('api/track/', include('device_tracker.urls')),

    path('api/v1/', include([
        # path('courses/', include('courses.urls', namespace='courses')),
        path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
        # … بقیه اپ‌ها
    ])),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
