from django.shortcuts import render
from .serializers import (
    UserSerializers,
    NoteListSerializers,
    NoteRetrieveSerializers,
    UserCreateSerializers
    )
from django.contrib.auth.admin import User
from .models import Note
from .permission import (
    IsOwner,
    # IsLogin
    )
from rest_framework import (
    viewsets,
    status
    )
from rest_framework.decorators import (
    api_view,
    permission_classes
    )
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
    )
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    )
# Create your views here.
# User = get_user_model()


class Userview (viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateview (CreateAPIView):
    serializer_class = UserCreateSerializers
    queryset = User.objects.all()
    # permission_classes = [AllowAny, IsLogin]
    permission_classes = [AllowAny]
    authentication_classes = []


class NoteListview(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteListSerializers
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user)
        return queryset


class NoteCreateview(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteRetrieveSerializers
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteRetriveview(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteListSerializers
    permission_classes = [IsAuthenticated, IsOwner]


class NoteDeleteview(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteListSerializers
    permission_classes = [IsAuthenticated, IsOwner]


class NoteUpdateview(RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteRetrieveSerializers
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


'''
@api_view(['POST', 'GET'])
@permission_classes((AllowAny, ))
def createuser(request):
    # query = User.objects.get(email=request.data.email)
    # if query.len() > 0:
    #     return Response('error', status=status.HTTP_302_FOUND)
    # else:
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('login please', status=status.HTTP_201_CREATED)
    return Response('error input', status=status.HTTP_400_BAD_REQUEST)
'''

