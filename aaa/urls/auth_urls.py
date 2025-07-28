from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from aaa.views.auth_login import LoginView
from aaa.views.auth_logout import LogoutView
from aaa.views.auth_signup import CustomTokenObtainPairView, PhoneCheckAPIView, SignupView
from aaa.views.otp_register import OtpRegisterAPIView
from aaa.views.otp_send import OTPSendView
from aaa.views.otp_verify import OTPVerifyView
from aaa.views.user_profile import UserProfileView


app_name = 'auth'

# 'api/v1/auth/'
urlpatterns = [
    path('phone-check/', PhoneCheckAPIView.as_view(), name='phone_check'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupView.as_view(), name='auth_signup'),
    path('otp/register/', OtpRegisterAPIView.as_view(), name='otp-register'),
    path('otp/send/', OTPSendView.as_view(), name='auth_otp_send'),
    path('otp/verify/', OTPVerifyView.as_view(), name='auth_otp_verify'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('profile/', UserProfileView.as_view(), name='auth_profile'),
]
