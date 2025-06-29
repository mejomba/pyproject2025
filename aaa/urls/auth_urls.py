from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from aaa.views.auth_signup import CustomTokenObtainPairView, PhoneCheckAPIView, SignupView

urlpatterns = [
    path('api/auth/check-phone/', PhoneCheckAPIView.as_view(), name='phone_check'),
    path('api/auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/signup/', SignupView.as_view(), name='auth_signup'),
]
