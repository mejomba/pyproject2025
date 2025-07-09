from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from aaa.serializers.otp_verify import OTPVerifySerializer
from aaa.serializers.auth_signup import SignupSerializer
from aaa.utils.jwt_tokens import generate_jwt_response
from device_tracker.utils import track_device


class OTPVerifyView(APIView):
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            track_device(request, user, refresh)
            return Response(generate_jwt_response(user, SignupSerializer), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
