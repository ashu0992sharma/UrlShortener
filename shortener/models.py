# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator

from . import managers


class ModelBase(models.Model):
    """
    This is a abstract model class to add is_deleted,
    created_at and modified at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class UrlHashMapping(ModelBase):
    """model to store hash to url mapping"""
    url = models.URLField(validators=[URLValidator])
    hash = models.CharField(max_length=8, unique=True, db_index=True)
    objects = managers.UrlShortenerManager()

    def __str__(self):
        return "url: {} hash: {}".format(self.url, self.hash)

