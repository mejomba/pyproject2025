# aaa/views/otp_login.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from aaa.models import CustomUser
from aaa.models.otp import OTP
from rest_framework_simplejwt.tokens import RefreshToken

class OtpLoginAPIView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        code = request.data.get('code')

        if not phone or not code:
            return Response({'detail': 'phone and code are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            otp = OTP.objects.get(phone=phone, code=code, is_used=False)
        except OTP.DoesNotExist:
            return Response({'detail': 'کد وارد شده نادرست است.'}, status=status.HTTP_400_BAD_REQUEST)

        if otp.expires_at < timezone.now():
            return Response({'detail': 'کد منقضی شده است.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(phone=phone)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'کاربری با این شماره وجود ندارد.'}, status=status.HTTP_404_NOT_FOUND)

        otp.is_used = True
        otp.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'user': {
                'id': user.id,
                'phone': user.phone,
                'full_name': user.full_name,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
