# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from . import managers

from mongoengine.document import Document
from mongoengine import StringField


class ModelBase(Document):
    """
    This is a abstract model class to add is_deleted,
    created_at and modified at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    meta = {
        "abstract": True
    }

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class UrlHashMapping(ModelBase):
    """model to store hash to url mapping"""
    url = StringField()
    hash = StringField()

    meta = {

    }

    def __str__(self):
        return "url: {} hash: {}".format(self.url, self.hash)




