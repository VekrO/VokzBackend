from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserTokenObtainPairSerializer

class LoginView(TokenObtainPairView):

    serializer_class = UserTokenObtainPairSerializer


