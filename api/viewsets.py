from movie import models
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer

    @action(methods=['get'], detail=False)  
    def published(self,request):
        published = self.get_queryset().filter(isPublish=True)
        serializer = self.get_serializer(published, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def newest(self,request):
        newest = self.get_queryset().order_by('pk').last()
        serializer = self.get_serializer(newest)
        return Response(serializer.data)

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
