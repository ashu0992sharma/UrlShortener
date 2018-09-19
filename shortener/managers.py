from django.db import models

from . import utils


class UrlShortenerManager(models.Manager):
    """manager for UrlShortener model"""

    def get_or_create_short_url(self, url):
        """
        Creating a hash for given url
        :param url: url to be shortened 
        :return: hash for the url
        """
        hash = utils.gen_hash()
        url_short_obj, _ = self.get_or_create(url=url, defaults={'hash': hash})
        return url_short_obj
    
    def get_url(self, hash):
        """
        Getting Url from a given hash
        :param hash: hash of a url
        :return: Url from the given hash
        """
        return self.get(hash=hash)