from api.models import App
from api.serializers import AppSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class AppList(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'type')


class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer