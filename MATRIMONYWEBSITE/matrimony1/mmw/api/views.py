from mmw.models import personinfo
from mmw.api.serializers import userserializer
from rest_framework import viewsets

class userviews(viewsets.ModelViewSet):
    queryset=personinfo.objects.all()
    serializer_class=userserializer