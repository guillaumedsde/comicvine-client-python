# coding: utf-8

"""
    ComicVine API

    OpenAPI specification for the ComicVine API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import comicvine_client
from comicvine_client.api.volume_api import VolumeApi  # noqa: E501
from comicvine_client.rest import ApiException


class TestVolumeApi(unittest.TestCase):
    """VolumeApi unit test stubs"""

    def setUp(self):
        self.api = comicvine_client.api.volume_api.VolumeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_volume(self):
        """Test case for get_volume

        Get a particular volume  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
