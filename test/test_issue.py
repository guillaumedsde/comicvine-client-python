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
from comicvine_client.models.issue import Issue  # noqa: E501
from comicvine_client.rest import ApiException

class TestIssue(unittest.TestCase):
    """Issue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Issue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = comicvine_client.models.issue.Issue()  # noqa: E501
        if include_optional :
            return Issue(
                id = 63316, 
                name = 'Yoko Tsuno', 
                aliases = 'Joko Zuno', 
                api_detail_url = 'https://comicvine.gamespot.com/api/volume/4050-87668/', 
                description = '<p>A total of 25 albums was published between 1972 and 2010. Creator Roger Leloup has also written a novel detailing the childhood and early years of the character. Seven albums have been translated in English.</p>', 
                deck = 'With knowledge and honor you can challenge anything.', 
                site_detail_url = 'https://comicvine.gamespot.com/yoko-tsuno/4005-63316/', 
                date_added = '2016-01-26 17:52:32', 
                date_last_updated = '2016-01-26 17:53:02', 
                character_credits = None, 
                characters_died_in = None, 
                concept_credits = None, 
                cover_date = None, 
                disbanded_teams = None, 
                first_appearance_characters = None, 
                first_appearance_concepts = None, 
                first_appearance_locations = None, 
                first_appearance_objects = None, 
                first_appearance_storyarcs = None, 
                first_appearance_teams = None, 
                image = None, 
                issue_number = None, 
                location_credits = None, 
                object_credits = None, 
                person_credits = None, 
                store_date = None, 
                story_arc_credits = None, 
                team_credits = None, 
                teams_disbanded_in = None, 
                volume = None
            )
        else :
            return Issue(
                id = 63316,
        )

    def testIssue(self):
        """Test Issue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
