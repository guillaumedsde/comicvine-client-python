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
from comicvine_client.models.character_all_of import CharacterAllOf  # noqa: E501
from comicvine_client.rest import ApiException

class TestCharacterAllOf(unittest.TestCase):
    """CharacterAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CharacterAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = comicvine_client.models.character_all_of.CharacterAllOf()  # noqa: E501
        if include_optional :
            return CharacterAllOf(
                character_enemies = [
                    null
                    ], 
                character_friends = [
                    null
                    ], 
                creators = [
                    null
                    ], 
                first_appeared_in_issue = null, 
                issues_died_in = [
                    null
                    ], 
                movies = [
                    None
                    ], 
                origin = None, 
                powers = None, 
                publisher = None, 
                real_name = 'Bruce Wayne', 
                team_enemies = [
                    None
                    ], 
                team_friends = [
                    None
                    ], 
                teams = [
                    None
                    ]
            )
        else :
            return CharacterAllOf(
        )

    def testCharacterAllOf(self):
        """Test CharacterAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
