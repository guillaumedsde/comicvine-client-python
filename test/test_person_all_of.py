# coding: utf-8

"""
    ComicVine API

    OpenAPI specification for the ComicVine API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import comicvine_client
from comicvine_client.models.person_all_of import PersonAllOf  # noqa: E501
from comicvine_client.rest import ApiException

class TestPersonAllOf(unittest.TestCase):
    """PersonAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PersonAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = comicvine_client.models.person_all_of.PersonAllOf()  # noqa: E501
        if include_optional :
            return PersonAllOf(
                country = 'UK', 
                created_characters = None, 
                death = 'Fri Jul 21 00:00:00 GMT 2017', 
                email = 'bruce@example.com', 
                hometown = 'Vladivostok', 
                website = 'https://person.example.com/'
            )
        else :
            return PersonAllOf(
        )

    def testPersonAllOf(self):
        """Test PersonAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
