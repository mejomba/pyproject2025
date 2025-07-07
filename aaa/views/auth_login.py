from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from aaa.serializers.auth_login import LoginSerializer
from aaa.utils.jwt_tokens import generate_jwt_response
from aaa.serializers.auth_signup import SignupSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response(
                generate_jwt_response(user, SignupSerializer),
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
