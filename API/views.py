from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Player
from . serializers import PlayerSerializer

from django.db.models import F

class PlayerList(APIView):

    def get(self, request):
        player = Player.objects.all()
        player = player.order_by('-score')
        serializer = PlayerSerializer(player, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        player = Player.objects.get(pk=pk)
        serializer = PlayerSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)