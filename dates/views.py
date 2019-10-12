from rest_framework import viewsets
from .serializers import DatesSerializer
from .models import Dates

class DatesViwset(viewsets.ModelViewSet):
    serializer_class = DatesSerializer
    queryset = Dates.objects.all()