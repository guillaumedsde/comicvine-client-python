# coding: utf-8

"""
    ComicVine API

    OpenAPI specification for the ComicVine API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from comicvine_client.configuration import Configuration


class Image(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'icon_url': 'str',
        'medium_url': 'str',
        'screen_url': 'str',
        'screen_large_url': 'str',
        'small_url': 'str',
        'super_url': 'str',
        'thumb_url': 'str',
        'tiny_url': 'str',
        'original_url': 'str',
        'image_tags': 'str'
    }

    attribute_map = {
        'icon_url': 'icon_url',
        'medium_url': 'medium_url',
        'screen_url': 'screen_url',
        'screen_large_url': 'screen_large_url',
        'small_url': 'small_url',
        'super_url': 'super_url',
        'thumb_url': 'thumb_url',
        'tiny_url': 'tiny_url',
        'original_url': 'original_url',
        'image_tags': 'image_tags'
    }

    def __init__(self, icon_url=None, medium_url=None, screen_url=None, screen_large_url=None, small_url=None, super_url=None, thumb_url=None, tiny_url=None, original_url=None, image_tags=None, local_vars_configuration=None):  # noqa: E501
        """Image - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._icon_url = None
        self._medium_url = None
        self._screen_url = None
        self._screen_large_url = None
        self._small_url = None
        self._super_url = None
        self._thumb_url = None
        self._tiny_url = None
        self._original_url = None
        self._image_tags = None
        self.discriminator = None

        if icon_url is not None:
            self.icon_url = icon_url
        if medium_url is not None:
            self.medium_url = medium_url
        if screen_url is not None:
            self.screen_url = screen_url
        if screen_large_url is not None:
            self.screen_large_url = screen_large_url
        if small_url is not None:
            self.small_url = small_url
        if super_url is not None:
            self.super_url = super_url
        if thumb_url is not None:
            self.thumb_url = thumb_url
        if tiny_url is not None:
            self.tiny_url = tiny_url
        if original_url is not None:
            self.original_url = original_url
        if image_tags is not None:
            self.image_tags = image_tags

    @property
    def icon_url(self):
        """Gets the icon_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The icon_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this Image.

        Image URL  # noqa: E501

        :param icon_url: The icon_url of this Image.  # noqa: E501
        :type icon_url: str
        """

        self._icon_url = icon_url

    @property
    def medium_url(self):
        """Gets the medium_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The medium_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._medium_url

    @medium_url.setter
    def medium_url(self, medium_url):
        """Sets the medium_url of this Image.

        Image URL  # noqa: E501

        :param medium_url: The medium_url of this Image.  # noqa: E501
        :type medium_url: str
        """

        self._medium_url = medium_url

    @property
    def screen_url(self):
        """Gets the screen_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The screen_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._screen_url

    @screen_url.setter
    def screen_url(self, screen_url):
        """Sets the screen_url of this Image.

        Image URL  # noqa: E501

        :param screen_url: The screen_url of this Image.  # noqa: E501
        :type screen_url: str
        """

        self._screen_url = screen_url

    @property
    def screen_large_url(self):
        """Gets the screen_large_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The screen_large_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._screen_large_url

    @screen_large_url.setter
    def screen_large_url(self, screen_large_url):
        """Sets the screen_large_url of this Image.

        Image URL  # noqa: E501

        :param screen_large_url: The screen_large_url of this Image.  # noqa: E501
        :type screen_large_url: str
        """

        self._screen_large_url = screen_large_url

    @property
    def small_url(self):
        """Gets the small_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The small_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._small_url

    @small_url.setter
    def small_url(self, small_url):
        """Sets the small_url of this Image.

        Image URL  # noqa: E501

        :param small_url: The small_url of this Image.  # noqa: E501
        :type small_url: str
        """

        self._small_url = small_url

    @property
    def super_url(self):
        """Gets the super_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The super_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._super_url

    @super_url.setter
    def super_url(self, super_url):
        """Sets the super_url of this Image.

        Image URL  # noqa: E501

        :param super_url: The super_url of this Image.  # noqa: E501
        :type super_url: str
        """

        self._super_url = super_url

    @property
    def thumb_url(self):
        """Gets the thumb_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The thumb_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._thumb_url

    @thumb_url.setter
    def thumb_url(self, thumb_url):
        """Sets the thumb_url of this Image.

        Image URL  # noqa: E501

        :param thumb_url: The thumb_url of this Image.  # noqa: E501
        :type thumb_url: str
        """

        self._thumb_url = thumb_url

    @property
    def tiny_url(self):
        """Gets the tiny_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The tiny_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._tiny_url

    @tiny_url.setter
    def tiny_url(self, tiny_url):
        """Sets the tiny_url of this Image.

        Image URL  # noqa: E501

        :param tiny_url: The tiny_url of this Image.  # noqa: E501
        :type tiny_url: str
        """

        self._tiny_url = tiny_url

    @property
    def original_url(self):
        """Gets the original_url of this Image.  # noqa: E501

        Image URL  # noqa: E501

        :return: The original_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._original_url

    @original_url.setter
    def original_url(self, original_url):
        """Sets the original_url of this Image.

        Image URL  # noqa: E501

        :param original_url: The original_url of this Image.  # noqa: E501
        :type original_url: str
        """

        self._original_url = original_url

    @property
    def image_tags(self):
        """Gets the image_tags of this Image.  # noqa: E501


        :return: The image_tags of this Image.  # noqa: E501
        :rtype: str
        """
        return self._image_tags

    @image_tags.setter
    def image_tags(self, image_tags):
        """Sets the image_tags of this Image.


        :param image_tags: The image_tags of this Image.  # noqa: E501
        :type image_tags: str
        """

        self._image_tags = image_tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Image):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Image):
            return True

        return self.to_dict() != other.to_dict()