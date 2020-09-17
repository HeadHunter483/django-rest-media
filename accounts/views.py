from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import User
from .permissions import IsSelfOrReadOnly
from .serializers import UserSignUpSerializer, UserSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk})


class UserSignUpView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Uesr.objects.all()
    serializer_class = UserSignUpSerializer


class UserViewSet(NestedViewSetMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  GenericViewSet):
    permission_classes = [IsSelfOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
