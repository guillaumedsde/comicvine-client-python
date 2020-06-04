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


class PersonAllOf(object):
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
        'birth': 'object',
        'count_of_issue_appearances': 'object',
        'country': 'object',
        'created_characters': 'object',
        'death': 'object',
        'email': 'object',
        'gender': 'object',
        'hometown': 'object',
        'image': 'object',
        'issue_credits': 'object',
        'story_arc_credits': 'object',
        'volume_credits': 'object',
        'website': 'object'
    }

    attribute_map = {
        'birth': 'birth',
        'count_of_issue_appearances': 'count_of_issue_appearances',
        'country': 'country',
        'created_characters': 'created_characters',
        'death': 'death',
        'email': 'email',
        'gender': 'gender',
        'hometown': 'hometown',
        'image': 'image',
        'issue_credits': 'issue_credits',
        'story_arc_credits': 'story_arc_credits',
        'volume_credits': 'volume_credits',
        'website': 'website'
    }

    def __init__(self, birth=None, count_of_issue_appearances=None, country=None, created_characters=None, death=None, email=None, gender=None, hometown=None, image=None, issue_credits=None, story_arc_credits=None, volume_credits=None, website=None, local_vars_configuration=None):  # noqa: E501
        """PersonAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._birth = None
        self._count_of_issue_appearances = None
        self._country = None
        self._created_characters = None
        self._death = None
        self._email = None
        self._gender = None
        self._hometown = None
        self._image = None
        self._issue_credits = None
        self._story_arc_credits = None
        self._volume_credits = None
        self._website = None
        self.discriminator = None

        if birth is not None:
            self.birth = birth
        if count_of_issue_appearances is not None:
            self.count_of_issue_appearances = count_of_issue_appearances
        if country is not None:
            self.country = country
        if created_characters is not None:
            self.created_characters = created_characters
        if death is not None:
            self.death = death
        if email is not None:
            self.email = email
        if gender is not None:
            self.gender = gender
        if hometown is not None:
            self.hometown = hometown
        if image is not None:
            self.image = image
        if issue_credits is not None:
            self.issue_credits = issue_credits
        if story_arc_credits is not None:
            self.story_arc_credits = story_arc_credits
        if volume_credits is not None:
            self.volume_credits = volume_credits
        if website is not None:
            self.website = website

    @property
    def birth(self):
        """Gets the birth of this PersonAllOf.  # noqa: E501

        A date, if one exists, that the person was born on. Not an origin date.  # noqa: E501

        :return: The birth of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this PersonAllOf.

        A date, if one exists, that the person was born on. Not an origin date.  # noqa: E501

        :param birth: The birth of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._birth = birth

    @property
    def count_of_issue_appearances(self):
        """Gets the count_of_issue_appearances of this PersonAllOf.  # noqa: E501

        Number of issues this person appears in.  # noqa: E501

        :return: The count_of_issue_appearances of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._count_of_issue_appearances

    @count_of_issue_appearances.setter
    def count_of_issue_appearances(self, count_of_issue_appearances):
        """Sets the count_of_issue_appearances of this PersonAllOf.

        Number of issues this person appears in.  # noqa: E501

        :param count_of_issue_appearances: The count_of_issue_appearances of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._count_of_issue_appearances = count_of_issue_appearances

    @property
    def country(self):
        """Gets the country of this PersonAllOf.  # noqa: E501

        Country the person resides in.  # noqa: E501

        :return: The country of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PersonAllOf.

        Country the person resides in.  # noqa: E501

        :param country: The country of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._country = country

    @property
    def created_characters(self):
        """Gets the created_characters of this PersonAllOf.  # noqa: E501

        Comic characters this person created.  # noqa: E501

        :return: The created_characters of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._created_characters

    @created_characters.setter
    def created_characters(self, created_characters):
        """Sets the created_characters of this PersonAllOf.

        Comic characters this person created.  # noqa: E501

        :param created_characters: The created_characters of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._created_characters = created_characters

    @property
    def death(self):
        """Gets the death of this PersonAllOf.  # noqa: E501

        Date this person died on.  # noqa: E501

        :return: The death of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._death

    @death.setter
    def death(self, death):
        """Sets the death of this PersonAllOf.

        Date this person died on.  # noqa: E501

        :param death: The death of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._death = death

    @property
    def email(self):
        """Gets the email of this PersonAllOf.  # noqa: E501

        The email of this person.  # noqa: E501

        :return: The email of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PersonAllOf.

        The email of this person.  # noqa: E501

        :param email: The email of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._email = email

    @property
    def gender(self):
        """Gets the gender of this PersonAllOf.  # noqa: E501

        Gender of the person. Available options are: Male, Female, Other  # noqa: E501

        :return: The gender of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this PersonAllOf.

        Gender of the person. Available options are: Male, Female, Other  # noqa: E501

        :param gender: The gender of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._gender = gender

    @property
    def hometown(self):
        """Gets the hometown of this PersonAllOf.  # noqa: E501

        City or town the person resides in.  # noqa: E501

        :return: The hometown of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        """Sets the hometown of this PersonAllOf.

        City or town the person resides in.  # noqa: E501

        :param hometown: The hometown of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._hometown = hometown

    @property
    def image(self):
        """Gets the image of this PersonAllOf.  # noqa: E501

        Main image of the person.  # noqa: E501

        :return: The image of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PersonAllOf.

        Main image of the person.  # noqa: E501

        :param image: The image of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._image = image

    @property
    def issue_credits(self):
        """Gets the issue_credits of this PersonAllOf.  # noqa: E501

        List of issues this person appears in.  # noqa: E501

        :return: The issue_credits of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._issue_credits

    @issue_credits.setter
    def issue_credits(self, issue_credits):
        """Sets the issue_credits of this PersonAllOf.

        List of issues this person appears in.  # noqa: E501

        :param issue_credits: The issue_credits of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._issue_credits = issue_credits

    @property
    def story_arc_credits(self):
        """Gets the story_arc_credits of this PersonAllOf.  # noqa: E501

        List of story arcs this person appears in.  # noqa: E501

        :return: The story_arc_credits of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._story_arc_credits

    @story_arc_credits.setter
    def story_arc_credits(self, story_arc_credits):
        """Sets the story_arc_credits of this PersonAllOf.

        List of story arcs this person appears in.  # noqa: E501

        :param story_arc_credits: The story_arc_credits of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._story_arc_credits = story_arc_credits

    @property
    def volume_credits(self):
        """Gets the volume_credits of this PersonAllOf.  # noqa: E501

        List of comic volumes this person appears in.  # noqa: E501

        :return: The volume_credits of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._volume_credits

    @volume_credits.setter
    def volume_credits(self, volume_credits):
        """Sets the volume_credits of this PersonAllOf.

        List of comic volumes this person appears in.  # noqa: E501

        :param volume_credits: The volume_credits of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._volume_credits = volume_credits

    @property
    def website(self):
        """Gets the website of this PersonAllOf.  # noqa: E501

        URL to the person website.  # noqa: E501

        :return: The website of this PersonAllOf.  # noqa: E501
        :rtype: object
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this PersonAllOf.

        URL to the person website.  # noqa: E501

        :param website: The website of this PersonAllOf.  # noqa: E501
        :type: object
        """

        self._website = website

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
        if not isinstance(other, PersonAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PersonAllOf):
            return True

        return self.to_dict() != other.to_dict()
