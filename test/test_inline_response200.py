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
from comicvine_client.models.inline_response200 import InlineResponse200  # noqa: E501
from comicvine_client.rest import ApiException

class TestInlineResponse200(unittest.TestCase):
    """InlineResponse200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = comicvine_client.models.inline_response200.InlineResponse200()  # noqa: E501
        if include_optional :
            return InlineResponse200(
                status_code = 102, 
                error = 'Error in URL Format', 
                number_of_total_results = 0, 
                number_of_page_results = 0, 
                results = null
            )
        else :
            return InlineResponse200(
        )

    def testInlineResponse200(self):
        """Test InlineResponse200"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()