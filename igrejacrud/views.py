from rest_framework import viewsets
from .models import Igreja
from .serializers import IgrejaSerializer


class IgrejaViewSet(viewsets.ModelViewSet):
    queryset = Igreja.objects.all()
    serializer_class = IgrejaSerializer
