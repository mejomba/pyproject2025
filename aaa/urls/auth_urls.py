from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from aaa.views.auth_login import LoginView
from aaa.views.auth_logout import LogoutView
from aaa.views.auth_signup import CustomTokenObtainPairView, PhoneCheckAPIView, SignupView
from aaa.views.otp_login import OtpLoginAPIView
from aaa.views.otp_register import OtpRegisterAPIView
from aaa.views.otp_send import OTPSendView
from aaa.views.otp_verify import OTPVerifyView
from aaa.views.password_login_or_signup import PasswordLoginOrSignupView
from aaa.views.resend_otp import ResendOtpAPIView
from aaa.views.user_profile import UserProfileView


app_name = 'auth'

# 'api/v1/auth/'
urlpatterns = [
    path('phone-check/', PhoneCheckAPIView.as_view(), name='phone_check'),  #buse
    path('resend-otp/', ResendOtpAPIView.as_view(), name='resend-otp'),  # use
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupView.as_view(), name='auth_signup'),
    path('otp/register/', OtpRegisterAPIView.as_view(), name='otp-register'),  # use
    path('otp/send/', OTPSendView.as_view(), name='auth_otp_send'),  # use
    path('otp/verify/', OTPVerifyView.as_view(), name='auth_otp_verify'),  # use
    path('otp/login/', OtpLoginAPIView.as_view(), name='otp-login'),  # use
    path("password-login-or-signup/", PasswordLoginOrSignupView.as_view(), name='password-login-or-signup'),  # use
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('profile/', UserProfileView.as_view(), name='auth_profile'),
]
