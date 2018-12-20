from api.models import App, User, AppGrp
from api.serializers import AppSerializer, UserSerializer, AppGrpSerializer
# from rest_framework import generics
from rest_framework import viewsets
import time

from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse


def test(request):
    print(request.POST)
    print('*'*12)
    print(request.META)
    time.sleep(3)
    return HttpResponse('ok')




# class AppList(generics.ListCreateAPIView):
#     queryset = App.objects.all()
#     serializer_class = AppSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('name', 'type')
#
#
# class AppDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = App.objects.all()
#     serializer_class = AppSerializer


class AppGrpViewSet(viewsets.ModelViewSet):
    queryset = AppGrp.objects.all()
    serializer_class = AppGrpSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'group', )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', )