from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializer import UserSerializer
from user.models import User

from .serializer import UserTokenObtainPairSerializer

class LoginView(TokenObtainPairView):

    serializer_class = UserTokenObtainPairSerializer

class RegisterView(APIView):

    serializer_class = UserSerializer

    def post(self, request):

        # Recebe os dados do usuário e passa para o serializador.
        serializer = UserSerializer(data=request.data)

        # Verifica se os dados estão válidos!
        if serializer.is_valid():
            # Salva caso os dados passados estão corretos.
            serializer.save()
            return Response({'message': 'Usuário criado com sucesso!', 'body': serializer.data}, status=status.HTTP_200_OK)
        else:
            # Retorna um erro caso os dados estejam incorretos.
            return Response({'message': 'Ocorreu um erro na criação da conta!', 'body': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
