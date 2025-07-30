from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from aaa.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class PasswordLoginOrSignupView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")

        if not phone or not password:
            return Response({"error": "Phone and password are required."}, status=400)

        try:
            user = CustomUser.objects.get(phone=phone)
            if not user.has_usable_password():
                return Response({"error": "This account uses OTP login. Cannot use password."}, status=400)

            user = authenticate(request, phone=phone, password=password)
            if not user:
                return Response({"error": "Invalid password."}, status=401)

        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_user(phone=phone, password=password)

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=200)
