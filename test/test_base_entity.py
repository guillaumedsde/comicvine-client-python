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
from comicvine_client.models.base_entity import BaseEntity  # noqa: E501
from comicvine_client.rest import ApiException

class TestBaseEntity(unittest.TestCase):
    """BaseEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BaseEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = comicvine_client.models.base_entity.BaseEntity()  # noqa: E501
        if include_optional :
            return BaseEntity(
                id = 63316, 
                name = 'Yoko Tsuno', 
                aliases = 'Anthony Edward Stark
Tony Stark
Golden Avenger
Shellhead
Armored Avenger
Tetsujin
Spare Parts Man
Iron Knight
Director Stark
Cobalt Man
The Progenitor
Invincible Iron Man
Iron Maniac
Iron Avenger
Crimson Dynamo
Merchant of Death', 
                api_detail_url = 'https://comicvine.gamespot.com/api/volume/4050-87668/', 
                description = '<p>A total of 25 albums was published between 1972 and 2010. Creator Roger Leloup has also written a novel detailing the childhood and early years of the character. Seven albums have been translated in English.</p>', 
                deck = 'With knowledge and honor you can challenge anything.', 
                site_detail_url = 'https://comicvine.gamespot.com/yoko-tsuno/4005-63316/', 
                date_added = '2016-01-26 17:52:32', 
                date_last_updated = '2016-01-26 17:53:02', 
                image = comicvine_client.models.image.Image(
                    icon_url = 'https://comicvine1.cbsistatic.com/uploads/square_avatar/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    medium_url = 'https://comicvine1.cbsistatic.com/uploads/scale_medium/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    screen_url = 'https://comicvine1.cbsistatic.com/uploads/screen_medium/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    screen_large_url = 'https://comicvine1.cbsistatic.com/uploads/screen_kubrick/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    small_url = 'https://comicvine1.cbsistatic.com/uploads/scale_small/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    super_url = 'https://comicvine1.cbsistatic.com/uploads/scale_large/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    thumb_url = 'https://comicvine1.cbsistatic.com/uploads/scale_avatar/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    tiny_url = 'https://comicvine1.cbsistatic.com/uploads/square_mini/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    original_url = 'https://comicvine1.cbsistatic.com/uploads/original/5/53387/2638218-2638217-1_nl_v02.jpg', 
                    image_tags = 'All Images', )
            )
        else :
            return BaseEntity(
                id = 63316,
        )

    def testBaseEntity(self):
        """Test BaseEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
