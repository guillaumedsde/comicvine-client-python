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


class IssueAllOf(object):
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
        'character_credits': 'object',
        'characters_died_in': 'object',
        'concept_credits': 'object',
        'cover_date': 'object',
        'disbanded_teams': 'object',
        'first_appearance_characters': 'object',
        'first_appearance_concepts': 'object',
        'first_appearance_locations': 'object',
        'first_appearance_objects': 'object',
        'first_appearance_storyarcs': 'object',
        'first_appearance_teams': 'object',
        'image': 'object',
        'issue_number': 'object',
        'location_credits': 'object',
        'object_credits': 'object',
        'person_credits': 'object',
        'store_date': 'object',
        'story_arc_credits': 'object',
        'team_credits': 'object',
        'teams_disbanded_in': 'object',
        'volume': 'object'
    }

    attribute_map = {
        'character_credits': 'character_credits',
        'characters_died_in': 'characters_died_in',
        'concept_credits': 'concept_credits',
        'cover_date': 'cover_date',
        'disbanded_teams': 'disbanded_teams',
        'first_appearance_characters': 'first_appearance_characters',
        'first_appearance_concepts': 'first_appearance_concepts',
        'first_appearance_locations': 'first_appearance_locations',
        'first_appearance_objects': 'first_appearance_objects',
        'first_appearance_storyarcs': 'first_appearance_storyarcs',
        'first_appearance_teams': 'first_appearance_teams',
        'image': 'image',
        'issue_number': 'issue_number',
        'location_credits': 'location_credits',
        'object_credits': 'object_credits',
        'person_credits': 'person_credits',
        'store_date': 'store_date',
        'story_arc_credits': 'story_arc_credits',
        'team_credits': 'team_credits',
        'teams_disbanded_in': 'teams_disbanded_in',
        'volume': 'volume'
    }

    def __init__(self, character_credits=None, characters_died_in=None, concept_credits=None, cover_date=None, disbanded_teams=None, first_appearance_characters=None, first_appearance_concepts=None, first_appearance_locations=None, first_appearance_objects=None, first_appearance_storyarcs=None, first_appearance_teams=None, image=None, issue_number=None, location_credits=None, object_credits=None, person_credits=None, store_date=None, story_arc_credits=None, team_credits=None, teams_disbanded_in=None, volume=None, local_vars_configuration=None):  # noqa: E501
        """IssueAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._character_credits = None
        self._characters_died_in = None
        self._concept_credits = None
        self._cover_date = None
        self._disbanded_teams = None
        self._first_appearance_characters = None
        self._first_appearance_concepts = None
        self._first_appearance_locations = None
        self._first_appearance_objects = None
        self._first_appearance_storyarcs = None
        self._first_appearance_teams = None
        self._image = None
        self._issue_number = None
        self._location_credits = None
        self._object_credits = None
        self._person_credits = None
        self._store_date = None
        self._story_arc_credits = None
        self._team_credits = None
        self._teams_disbanded_in = None
        self._volume = None
        self.discriminator = None

        if character_credits is not None:
            self.character_credits = character_credits
        if characters_died_in is not None:
            self.characters_died_in = characters_died_in
        if concept_credits is not None:
            self.concept_credits = concept_credits
        if cover_date is not None:
            self.cover_date = cover_date
        if disbanded_teams is not None:
            self.disbanded_teams = disbanded_teams
        if first_appearance_characters is not None:
            self.first_appearance_characters = first_appearance_characters
        if first_appearance_concepts is not None:
            self.first_appearance_concepts = first_appearance_concepts
        if first_appearance_locations is not None:
            self.first_appearance_locations = first_appearance_locations
        if first_appearance_objects is not None:
            self.first_appearance_objects = first_appearance_objects
        if first_appearance_storyarcs is not None:
            self.first_appearance_storyarcs = first_appearance_storyarcs
        if first_appearance_teams is not None:
            self.first_appearance_teams = first_appearance_teams
        if image is not None:
            self.image = image
        if issue_number is not None:
            self.issue_number = issue_number
        if location_credits is not None:
            self.location_credits = location_credits
        if object_credits is not None:
            self.object_credits = object_credits
        if person_credits is not None:
            self.person_credits = person_credits
        if store_date is not None:
            self.store_date = store_date
        if story_arc_credits is not None:
            self.story_arc_credits = story_arc_credits
        if team_credits is not None:
            self.team_credits = team_credits
        if teams_disbanded_in is not None:
            self.teams_disbanded_in = teams_disbanded_in
        if volume is not None:
            self.volume = volume

    @property
    def character_credits(self):
        """Gets the character_credits of this IssueAllOf.  # noqa: E501

        A list of characters that appear in this issue.  # noqa: E501

        :return: The character_credits of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._character_credits

    @character_credits.setter
    def character_credits(self, character_credits):
        """Sets the character_credits of this IssueAllOf.

        A list of characters that appear in this issue.  # noqa: E501

        :param character_credits: The character_credits of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._character_credits = character_credits

    @property
    def characters_died_in(self):
        """Gets the characters_died_in of this IssueAllOf.  # noqa: E501

        A list of characters that died in this issue.  # noqa: E501

        :return: The characters_died_in of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._characters_died_in

    @characters_died_in.setter
    def characters_died_in(self, characters_died_in):
        """Sets the characters_died_in of this IssueAllOf.

        A list of characters that died in this issue.  # noqa: E501

        :param characters_died_in: The characters_died_in of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._characters_died_in = characters_died_in

    @property
    def concept_credits(self):
        """Gets the concept_credits of this IssueAllOf.  # noqa: E501

        A list of concepts that appear in this issue.  # noqa: E501

        :return: The concept_credits of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._concept_credits

    @concept_credits.setter
    def concept_credits(self, concept_credits):
        """Sets the concept_credits of this IssueAllOf.

        A list of concepts that appear in this issue.  # noqa: E501

        :param concept_credits: The concept_credits of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._concept_credits = concept_credits

    @property
    def cover_date(self):
        """Gets the cover_date of this IssueAllOf.  # noqa: E501

        The publish date printed on the cover of an issue.  # noqa: E501

        :return: The cover_date of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._cover_date

    @cover_date.setter
    def cover_date(self, cover_date):
        """Sets the cover_date of this IssueAllOf.

        The publish date printed on the cover of an issue.  # noqa: E501

        :param cover_date: The cover_date of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._cover_date = cover_date

    @property
    def disbanded_teams(self):
        """Gets the disbanded_teams of this IssueAllOf.  # noqa: E501

        A list of teams that disbanded in this issue.  # noqa: E501

        :return: The disbanded_teams of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._disbanded_teams

    @disbanded_teams.setter
    def disbanded_teams(self, disbanded_teams):
        """Sets the disbanded_teams of this IssueAllOf.

        A list of teams that disbanded in this issue.  # noqa: E501

        :param disbanded_teams: The disbanded_teams of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._disbanded_teams = disbanded_teams

    @property
    def first_appearance_characters(self):
        """Gets the first_appearance_characters of this IssueAllOf.  # noqa: E501

        A list of characters in which this issue is the first appearance of the character.  # noqa: E501

        :return: The first_appearance_characters of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._first_appearance_characters

    @first_appearance_characters.setter
    def first_appearance_characters(self, first_appearance_characters):
        """Sets the first_appearance_characters of this IssueAllOf.

        A list of characters in which this issue is the first appearance of the character.  # noqa: E501

        :param first_appearance_characters: The first_appearance_characters of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._first_appearance_characters = first_appearance_characters

    @property
    def first_appearance_concepts(self):
        """Gets the first_appearance_concepts of this IssueAllOf.  # noqa: E501

        A list of concepts in which this issue is the first appearance of the concept.  # noqa: E501

        :return: The first_appearance_concepts of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._first_appearance_concepts

    @first_appearance_concepts.setter
    def first_appearance_concepts(self, first_appearance_concepts):
        """Sets the first_appearance_concepts of this IssueAllOf.

        A list of concepts in which this issue is the first appearance of the concept.  # noqa: E501

        :param first_appearance_concepts: The first_appearance_concepts of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._first_appearance_concepts = first_appearance_concepts

    @property
    def first_appearance_locations(self):
        """Gets the first_appearance_locations of this IssueAllOf.  # noqa: E501

        A list of locations in which this issue is the first appearance of the location.  # noqa: E501

        :return: The first_appearance_locations of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._first_appearance_locations

    @first_appearance_locations.setter
    def first_appearance_locations(self, first_appearance_locations):
        """Sets the first_appearance_locations of this IssueAllOf.

        A list of locations in which this issue is the first appearance of the location.  # noqa: E501

        :param first_appearance_locations: The first_appearance_locations of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._first_appearance_locations = first_appearance_locations

    @property
    def first_appearance_objects(self):
        """Gets the first_appearance_objects of this IssueAllOf.  # noqa: E501

        A list of objects in which this issue is the first appearance of the object.  # noqa: E501

        :return: The first_appearance_objects of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._first_appearance_objects

    @first_appearance_objects.setter
    def first_appearance_objects(self, first_appearance_objects):
        """Sets the first_appearance_objects of this IssueAllOf.

        A list of objects in which this issue is the first appearance of the object.  # noqa: E501

        :param first_appearance_objects: The first_appearance_objects of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._first_appearance_objects = first_appearance_objects

    @property
    def first_appearance_storyarcs(self):
        """Gets the first_appearance_storyarcs of this IssueAllOf.  # noqa: E501

        A list of storyarcs in which this issue is the first appearance of the story arc.  # noqa: E501

        :return: The first_appearance_storyarcs of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._first_appearance_storyarcs

    @first_appearance_storyarcs.setter
    def first_appearance_storyarcs(self, first_appearance_storyarcs):
        """Sets the first_appearance_storyarcs of this IssueAllOf.

        A list of storyarcs in which this issue is the first appearance of the story arc.  # noqa: E501

        :param first_appearance_storyarcs: The first_appearance_storyarcs of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._first_appearance_storyarcs = first_appearance_storyarcs

    @property
    def first_appearance_teams(self):
        """Gets the first_appearance_teams of this IssueAllOf.  # noqa: E501

        A list of teams in which this issue is the first appearance of the team.  # noqa: E501

        :return: The first_appearance_teams of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._first_appearance_teams

    @first_appearance_teams.setter
    def first_appearance_teams(self, first_appearance_teams):
        """Sets the first_appearance_teams of this IssueAllOf.

        A list of teams in which this issue is the first appearance of the team.  # noqa: E501

        :param first_appearance_teams: The first_appearance_teams of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._first_appearance_teams = first_appearance_teams

    @property
    def image(self):
        """Gets the image of this IssueAllOf.  # noqa: E501

        Main image of the issue.  # noqa: E501

        :return: The image of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IssueAllOf.

        Main image of the issue.  # noqa: E501

        :param image: The image of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._image = image

    @property
    def issue_number(self):
        """Gets the issue_number of this IssueAllOf.  # noqa: E501

        The number assigned to the issue within the volume set.  # noqa: E501

        :return: The issue_number of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """Sets the issue_number of this IssueAllOf.

        The number assigned to the issue within the volume set.  # noqa: E501

        :param issue_number: The issue_number of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._issue_number = issue_number

    @property
    def location_credits(self):
        """Gets the location_credits of this IssueAllOf.  # noqa: E501

        List of locations that appeared in this issue.  # noqa: E501

        :return: The location_credits of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._location_credits

    @location_credits.setter
    def location_credits(self, location_credits):
        """Sets the location_credits of this IssueAllOf.

        List of locations that appeared in this issue.  # noqa: E501

        :param location_credits: The location_credits of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._location_credits = location_credits

    @property
    def object_credits(self):
        """Gets the object_credits of this IssueAllOf.  # noqa: E501

        List of objects that appeared in this issue.  # noqa: E501

        :return: The object_credits of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._object_credits

    @object_credits.setter
    def object_credits(self, object_credits):
        """Sets the object_credits of this IssueAllOf.

        List of objects that appeared in this issue.  # noqa: E501

        :param object_credits: The object_credits of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._object_credits = object_credits

    @property
    def person_credits(self):
        """Gets the person_credits of this IssueAllOf.  # noqa: E501

        List of people that worked on this issue.  # noqa: E501

        :return: The person_credits of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._person_credits

    @person_credits.setter
    def person_credits(self, person_credits):
        """Sets the person_credits of this IssueAllOf.

        List of people that worked on this issue.  # noqa: E501

        :param person_credits: The person_credits of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._person_credits = person_credits

    @property
    def store_date(self):
        """Gets the store_date of this IssueAllOf.  # noqa: E501

        The date the issue was first sold in stores.  # noqa: E501

        :return: The store_date of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._store_date

    @store_date.setter
    def store_date(self, store_date):
        """Sets the store_date of this IssueAllOf.

        The date the issue was first sold in stores.  # noqa: E501

        :param store_date: The store_date of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._store_date = store_date

    @property
    def story_arc_credits(self):
        """Gets the story_arc_credits of this IssueAllOf.  # noqa: E501

        List of story arcs this issue appears in.  # noqa: E501

        :return: The story_arc_credits of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._story_arc_credits

    @story_arc_credits.setter
    def story_arc_credits(self, story_arc_credits):
        """Sets the story_arc_credits of this IssueAllOf.

        List of story arcs this issue appears in.  # noqa: E501

        :param story_arc_credits: The story_arc_credits of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._story_arc_credits = story_arc_credits

    @property
    def team_credits(self):
        """Gets the team_credits of this IssueAllOf.  # noqa: E501

        List of teams that appear in this issue.  # noqa: E501

        :return: The team_credits of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._team_credits

    @team_credits.setter
    def team_credits(self, team_credits):
        """Sets the team_credits of this IssueAllOf.

        List of teams that appear in this issue.  # noqa: E501

        :param team_credits: The team_credits of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._team_credits = team_credits

    @property
    def teams_disbanded_in(self):
        """Gets the teams_disbanded_in of this IssueAllOf.  # noqa: E501

        List of teams that disbanded in this issue.  # noqa: E501

        :return: The teams_disbanded_in of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._teams_disbanded_in

    @teams_disbanded_in.setter
    def teams_disbanded_in(self, teams_disbanded_in):
        """Sets the teams_disbanded_in of this IssueAllOf.

        List of teams that disbanded in this issue.  # noqa: E501

        :param teams_disbanded_in: The teams_disbanded_in of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._teams_disbanded_in = teams_disbanded_in

    @property
    def volume(self):
        """Gets the volume of this IssueAllOf.  # noqa: E501

        The volume this issue is a part of.  # noqa: E501

        :return: The volume of this IssueAllOf.  # noqa: E501
        :rtype: object
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this IssueAllOf.

        The volume this issue is a part of.  # noqa: E501

        :param volume: The volume of this IssueAllOf.  # noqa: E501
        :type: object
        """

        self._volume = volume

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
        if not isinstance(other, IssueAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IssueAllOf):
            return True

        return self.to_dict() != other.to_dict()
