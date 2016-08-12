# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


# Third Party Stuff
from rest_framework import generics
from .serializers import SuttaRequirementSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class SuttaRequirementViewSet(generics.CreateAPIView):

    permission_class = (AllowAny, )
    serializer_class = SuttaRequirementSerializer

    def post(self, request, format=None):
        serializer = SuttaRequirementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NormalViewSet(generics.ListAPIView):

    permission_class = (AllowAny, )
    serializer_class = SuttaRequirementSerializer

    def get_queryset(self):
        qs = {"Error": "Please visit api endpoints"}
        return qs

    def get(self, request, format=None):

        queryset = self.get_queryset()
        return Response(queryset)
