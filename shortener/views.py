# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from . import models
from . import constants
from . import utils

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
        url = request.data.get("url")
        url_validated = utils.validate_url(url)
        if url_validated:
            hash_obj = models.UrlHashMapping.objects.get_or_create_short_url(url)
            data = {
                "url": hash_obj.hash,
                "status": "Ok"
            }

            return Response(data, status=status.HTTP_200_OK)
        data = {
            "message": constants.INVALID_URL,
            "status": constants.FAILED
        }
        logger.error(data)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UrlDecode(APIView):
    """ApiView for encoding a Url"""

    def post(self, request):
        """
        :param request: hashed url to be decoded
        :return: long url if present for the hashed url else error message
        """

        hash = request.data.get("url")

        validated_hash = utils.validate_hash(hash)  # checking if hash is valid or not
        if validated_hash:
            try:
                url_object = models.UrlHashMapping.objects.get_url(hash)
            except ObjectDoesNotExist:
                data = {
                    "message": constants.URL_OBJECT_DOES_NOT_EXIST,
                    "status": constants.FAILED
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)

            data = {
                "url": url_object.url,
                "status": constants.OK
            }
            return Response(data, status=status.HTTP_200_OK)

        data = {
            "message": constants.INVALID_URL,
            "status": constants.FAILED
        }
        logger.debug(data)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class RedirectUrl(APIView):
    """Redirect API"""

    def get(self, request, hash):
        """
        :param request:
        :param hash: hash of the url
        :return: redirecting to its actual url
        """
        validated_hash = utils.validate_hash(hash)  # checking if hash is valid or not
        if validated_hash:
            try:
                url_object = models.UrlHashMapping.objects.get_url(hash)
                return HttpResponseRedirect(url_object.url)
            except ObjectDoesNotExist:
                data = {
                    "message": constants.URL_OBJECT_DOES_NOT_EXIST,
                    "status": constants.FAILED
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)
        data = {
            "message": constants.INVALID_URL,
            "status": constants.FAILED
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)




