# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse

from . import models
from . import utils


class UrlHashMappingModelTest(TestCase):
    """Unit Test for UrlHashMapping model"""

    def create_obj(self, url):
        """creating object for UrlHashMapping"""
        return models.UrlHashMapping.objects.get_or_create_short_url(url)

    def test_urlhashmapping_creation(self):
        """testing UrlHashMapping object creation"""
        url = "http://abc.com/abc"
        obj = self.create_obj(url)
        self.assertTrue(isinstance(obj, models.UrlHashMapping))


class UrlEncodeTest(TestCase):
    """Unit test for UrlEncode API"""

    def test_encode(self):
        api = reverse("url-encode")
        data = {"url": "http://abc.com/abc"}
        resp = self.client.post(api, data)
        self.assertEqual(resp.status_code, 200)


class UrlDecodeTest(TestCase):
    """Unit test for UrlEncode API"""

    def create_obj(self, url):
        """creating object for UrlHashMapping"""
        return models.UrlHashMapping.objects.get_or_create_short_url(url)

    def test_decode(self):
        """testing url decode API"""

        url = "http://abc.com/abc"
        obj = self.create_obj(url)

        api = reverse("url-decode")
        data = {"url": obj.hash}
        resp = self.client.post(api, data)
        self.assertEqual(resp.status_code, 200)


class ValidationTest(TestCase):
    """test cases for url and hash validation"""

    def test_url_validation(self):
        """testing url validation"""
        url = "http://abc.com/abc"
        validate_url = utils.validate_url(url)
        validate_url = True if validate_url else False
        self.assertEqual(validate_url, True)
        url = "http:adsf"
        validate_url = utils.validate_url(url)
        validate_url = True if validate_url else False
        self.assertEqual(validate_url, False)

    def test_hash_validation(self):
        """testing hash validation"""
        hash = "An35sfad"
        validate_hash = utils.validate_hash(hash)
        validate_hash = True if validate_hash else False
        print('validate_hash', validate_hash)
        self.assertEqual(validate_hash, True)
        hash = "An35sfad#"
        validate_hash = utils.validate_hash(hash)
        validate_hash = True if validate_hash else False
        self.assertEqual(validate_hash, False)

