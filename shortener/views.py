# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from . import models
from . import constants
from . import serializers

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class UrlEncode(APIView):
    """ApiView for encoding a Url"""

    def post(self, request):
        """
        :param request: url to be encoded
        :return: hashed url
        """
        data = request.data
        serializer = serializers.UrlShortenerCreateSerializer(data=data)
        if serializer.is_valid():
            url_object = serializer.save()
            serializer = serializers.UrlShortenerGetHashSerializer(url_object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrlDecode(APIView):
    """ApiView for encoding a Url"""

    def post(self, request):
        """
        :param request: hashed url to be decoded
        :return: long url if present for the hashed url else error message
        """
        data = {"hash": request.data.get("url")}
        serializer = serializers.UrlShortenerValidateUrlSerializer(data=data)
        if serializer.is_valid():
            hash = data["hash"]
            try:
                url_object = models.UrlHashMapping.objects.get_url(hash)
            except ObjectDoesNotExist:
                data = {"message": constants.URL_OBJECT_DOES_NOT_EXIST}
                return Response(data, status=status.HTTP_404_NOT_FOUND)
            serializer = serializers.UrlShortenerGetUrlSerializer(url_object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectUrl(APIView):
    """Redirect API"""

    def get(self, request, hash):
        """
        :param request:
        :param hash: hash of the url
        :return: redirecting to its actual url
        """
        data = {"hash": hash}
        serializer = serializers.UrlShortenerValidateUrlSerializer(data=data)
        if serializer.is_valid():
            try:
                url_object = models.UrlHashMapping.objects.get_url(hash)
                return HttpResponseRedirect(url_object.url)
            except ObjectDoesNotExist:
                data = {
                    "message": constants.URL_OBJECT_DOES_NOT_EXIST,
                    "status": constants.FAILED
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




