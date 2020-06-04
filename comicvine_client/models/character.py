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


class Character(object):
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
        'id': 'int',
        'name': 'str',
        'aliases': 'str',
        'api_detail_url': 'str',
        'description': 'str',
        'deck': 'str',
        'site_detail_url': 'object',
        'date_added': 'str',
        'date_last_updated': 'str',
        'birth': 'object',
        'character_enemies': 'object',
        'character_friends': 'object',
        'count_of_issue_appearances': 'object',
        'creators': 'object',
        'first_appeared_in_issue': 'object',
        'gender': 'object',
        'image': 'object',
        'issue_credits': 'object',
        'issues_died_in': 'object',
        'movies': 'object',
        'origin': 'object',
        'powers': 'object',
        'publisher': 'object',
        'real_name': 'object',
        'story_arc_credits': 'object',
        'team_enemies': 'object',
        'team_friends': 'object',
        'teams': 'object',
        'volume_credits': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'aliases': 'aliases',
        'api_detail_url': 'api_detail_url',
        'description': 'description',
        'deck': 'deck',
        'site_detail_url': 'site_detail_url',
        'date_added': 'date_added',
        'date_last_updated': 'date_last_updated',
        'birth': 'birth',
        'character_enemies': 'character_enemies',
        'character_friends': 'character_friends',
        'count_of_issue_appearances': 'count_of_issue_appearances',
        'creators': 'creators',
        'first_appeared_in_issue': 'first_appeared_in_issue',
        'gender': 'gender',
        'image': 'image',
        'issue_credits': 'issue_credits',
        'issues_died_in': 'issues_died_in',
        'movies': 'movies',
        'origin': 'origin',
        'powers': 'powers',
        'publisher': 'publisher',
        'real_name': 'real_name',
        'story_arc_credits': 'story_arc_credits',
        'team_enemies': 'team_enemies',
        'team_friends': 'team_friends',
        'teams': 'teams',
        'volume_credits': 'volume_credits'
    }

    def __init__(self, id=None, name=None, aliases=None, api_detail_url=None, description=None, deck=None, site_detail_url=None, date_added=None, date_last_updated=None, birth=None, character_enemies=None, character_friends=None, count_of_issue_appearances=None, creators=None, first_appeared_in_issue=None, gender=None, image=None, issue_credits=None, issues_died_in=None, movies=None, origin=None, powers=None, publisher=None, real_name=None, story_arc_credits=None, team_enemies=None, team_friends=None, teams=None, volume_credits=None, local_vars_configuration=None):  # noqa: E501
        """Character - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._aliases = None
        self._api_detail_url = None
        self._description = None
        self._deck = None
        self._site_detail_url = None
        self._date_added = None
        self._date_last_updated = None
        self._birth = None
        self._character_enemies = None
        self._character_friends = None
        self._count_of_issue_appearances = None
        self._creators = None
        self._first_appeared_in_issue = None
        self._gender = None
        self._image = None
        self._issue_credits = None
        self._issues_died_in = None
        self._movies = None
        self._origin = None
        self._powers = None
        self._publisher = None
        self._real_name = None
        self._story_arc_credits = None
        self._team_enemies = None
        self._team_friends = None
        self._teams = None
        self._volume_credits = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if aliases is not None:
            self.aliases = aliases
        if api_detail_url is not None:
            self.api_detail_url = api_detail_url
        if description is not None:
            self.description = description
        if deck is not None:
            self.deck = deck
        if site_detail_url is not None:
            self.site_detail_url = site_detail_url
        if date_added is not None:
            self.date_added = date_added
        if date_last_updated is not None:
            self.date_last_updated = date_last_updated
        if birth is not None:
            self.birth = birth
        if character_enemies is not None:
            self.character_enemies = character_enemies
        if character_friends is not None:
            self.character_friends = character_friends
        if count_of_issue_appearances is not None:
            self.count_of_issue_appearances = count_of_issue_appearances
        if creators is not None:
            self.creators = creators
        if first_appeared_in_issue is not None:
            self.first_appeared_in_issue = first_appeared_in_issue
        if gender is not None:
            self.gender = gender
        if image is not None:
            self.image = image
        if issue_credits is not None:
            self.issue_credits = issue_credits
        if issues_died_in is not None:
            self.issues_died_in = issues_died_in
        if movies is not None:
            self.movies = movies
        if origin is not None:
            self.origin = origin
        if powers is not None:
            self.powers = powers
        if publisher is not None:
            self.publisher = publisher
        if real_name is not None:
            self.real_name = real_name
        if story_arc_credits is not None:
            self.story_arc_credits = story_arc_credits
        if team_enemies is not None:
            self.team_enemies = team_enemies
        if team_friends is not None:
            self.team_friends = team_friends
        if teams is not None:
            self.teams = teams
        if volume_credits is not None:
            self.volume_credits = volume_credits

    @property
    def id(self):
        """Gets the id of this Character.  # noqa: E501

        Unique ID for the entity.  # noqa: E501

        :return: The id of this Character.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Character.

        Unique ID for the entity.  # noqa: E501

        :param id: The id of this Character.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Character.  # noqa: E501

        Name for the entity  # noqa: E501

        :return: The name of this Character.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Character.

        Name for the entity  # noqa: E501

        :param name: The name of this Character.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def aliases(self):
        """Gets the aliases of this Character.  # noqa: E501

        List of aliases the entity is known by. A \\n (newline) seperates each alias.  # noqa: E501

        :return: The aliases of this Character.  # noqa: E501
        :rtype: str
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this Character.

        List of aliases the entity is known by. A \\n (newline) seperates each alias.  # noqa: E501

        :param aliases: The aliases of this Character.  # noqa: E501
        :type: str
        """

        self._aliases = aliases

    @property
    def api_detail_url(self):
        """Gets the api_detail_url of this Character.  # noqa: E501

        URL pointing to the entity detail resource.  # noqa: E501

        :return: The api_detail_url of this Character.  # noqa: E501
        :rtype: str
        """
        return self._api_detail_url

    @api_detail_url.setter
    def api_detail_url(self, api_detail_url):
        """Sets the api_detail_url of this Character.

        URL pointing to the entity detail resource.  # noqa: E501

        :param api_detail_url: The api_detail_url of this Character.  # noqa: E501
        :type: str
        """

        self._api_detail_url = api_detail_url

    @property
    def description(self):
        """Gets the description of this Character.  # noqa: E501

        Description of the entity.  # noqa: E501

        :return: The description of this Character.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Character.

        Description of the entity.  # noqa: E501

        :param description: The description of this Character.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def deck(self):
        """Gets the deck of this Character.  # noqa: E501

        Brief summary of the Entity.  # noqa: E501

        :return: The deck of this Character.  # noqa: E501
        :rtype: str
        """
        return self._deck

    @deck.setter
    def deck(self, deck):
        """Sets the deck of this Character.

        Brief summary of the Entity.  # noqa: E501

        :param deck: The deck of this Character.  # noqa: E501
        :type: str
        """

        self._deck = deck

    @property
    def site_detail_url(self):
        """Gets the site_detail_url of this Character.  # noqa: E501

        URL pointing to the character on Giant Bomb.  # noqa: E501

        :return: The site_detail_url of this Character.  # noqa: E501
        :rtype: object
        """
        return self._site_detail_url

    @site_detail_url.setter
    def site_detail_url(self, site_detail_url):
        """Sets the site_detail_url of this Character.

        URL pointing to the character on Giant Bomb.  # noqa: E501

        :param site_detail_url: The site_detail_url of this Character.  # noqa: E501
        :type: object
        """

        self._site_detail_url = site_detail_url

    @property
    def date_added(self):
        """Gets the date_added of this Character.  # noqa: E501

        Date the entity was added to Comic Vine.  # noqa: E501

        :return: The date_added of this Character.  # noqa: E501
        :rtype: str
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """Sets the date_added of this Character.

        Date the entity was added to Comic Vine.  # noqa: E501

        :param date_added: The date_added of this Character.  # noqa: E501
        :type: str
        """

        self._date_added = date_added

    @property
    def date_last_updated(self):
        """Gets the date_last_updated of this Character.  # noqa: E501

        Date the entity was last updated on Comic Vine.  # noqa: E501

        :return: The date_last_updated of this Character.  # noqa: E501
        :rtype: str
        """
        return self._date_last_updated

    @date_last_updated.setter
    def date_last_updated(self, date_last_updated):
        """Sets the date_last_updated of this Character.

        Date the entity was last updated on Comic Vine.  # noqa: E501

        :param date_last_updated: The date_last_updated of this Character.  # noqa: E501
        :type: str
        """

        self._date_last_updated = date_last_updated

    @property
    def birth(self):
        """Gets the birth of this Character.  # noqa: E501

        A date, if one exists, that the character was born on. Not an origin date.  # noqa: E501

        :return: The birth of this Character.  # noqa: E501
        :rtype: object
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this Character.

        A date, if one exists, that the character was born on. Not an origin date.  # noqa: E501

        :param birth: The birth of this Character.  # noqa: E501
        :type: object
        """

        self._birth = birth

    @property
    def character_enemies(self):
        """Gets the character_enemies of this Character.  # noqa: E501

        List of characters that are enemies with this character.  # noqa: E501

        :return: The character_enemies of this Character.  # noqa: E501
        :rtype: object
        """
        return self._character_enemies

    @character_enemies.setter
    def character_enemies(self, character_enemies):
        """Sets the character_enemies of this Character.

        List of characters that are enemies with this character.  # noqa: E501

        :param character_enemies: The character_enemies of this Character.  # noqa: E501
        :type: object
        """

        self._character_enemies = character_enemies

    @property
    def character_friends(self):
        """Gets the character_friends of this Character.  # noqa: E501

        List of characters that are friends with this character.  # noqa: E501

        :return: The character_friends of this Character.  # noqa: E501
        :rtype: object
        """
        return self._character_friends

    @character_friends.setter
    def character_friends(self, character_friends):
        """Sets the character_friends of this Character.

        List of characters that are friends with this character.  # noqa: E501

        :param character_friends: The character_friends of this Character.  # noqa: E501
        :type: object
        """

        self._character_friends = character_friends

    @property
    def count_of_issue_appearances(self):
        """Gets the count_of_issue_appearances of this Character.  # noqa: E501

        Number of issues this character appears in.  # noqa: E501

        :return: The count_of_issue_appearances of this Character.  # noqa: E501
        :rtype: object
        """
        return self._count_of_issue_appearances

    @count_of_issue_appearances.setter
    def count_of_issue_appearances(self, count_of_issue_appearances):
        """Sets the count_of_issue_appearances of this Character.

        Number of issues this character appears in.  # noqa: E501

        :param count_of_issue_appearances: The count_of_issue_appearances of this Character.  # noqa: E501
        :type: object
        """

        self._count_of_issue_appearances = count_of_issue_appearances

    @property
    def creators(self):
        """Gets the creators of this Character.  # noqa: E501

        List of the real life people who created this character.  # noqa: E501

        :return: The creators of this Character.  # noqa: E501
        :rtype: object
        """
        return self._creators

    @creators.setter
    def creators(self, creators):
        """Sets the creators of this Character.

        List of the real life people who created this character.  # noqa: E501

        :param creators: The creators of this Character.  # noqa: E501
        :type: object
        """

        self._creators = creators

    @property
    def first_appeared_in_issue(self):
        """Gets the first_appeared_in_issue of this Character.  # noqa: E501

        Issue where the character made its first appearance.  # noqa: E501

        :return: The first_appeared_in_issue of this Character.  # noqa: E501
        :rtype: object
        """
        return self._first_appeared_in_issue

    @first_appeared_in_issue.setter
    def first_appeared_in_issue(self, first_appeared_in_issue):
        """Sets the first_appeared_in_issue of this Character.

        Issue where the character made its first appearance.  # noqa: E501

        :param first_appeared_in_issue: The first_appeared_in_issue of this Character.  # noqa: E501
        :type: object
        """

        self._first_appeared_in_issue = first_appeared_in_issue

    @property
    def gender(self):
        """Gets the gender of this Character.  # noqa: E501

        Gender of the character. Available options are: Male, Female, Other  # noqa: E501

        :return: The gender of this Character.  # noqa: E501
        :rtype: object
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Character.

        Gender of the character. Available options are: Male, Female, Other  # noqa: E501

        :param gender: The gender of this Character.  # noqa: E501
        :type: object
        """

        self._gender = gender

    @property
    def image(self):
        """Gets the image of this Character.  # noqa: E501

        Main image of the character.  # noqa: E501

        :return: The image of this Character.  # noqa: E501
        :rtype: object
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Character.

        Main image of the character.  # noqa: E501

        :param image: The image of this Character.  # noqa: E501
        :type: object
        """

        self._image = image

    @property
    def issue_credits(self):
        """Gets the issue_credits of this Character.  # noqa: E501

        List of issues this character appears in.  # noqa: E501

        :return: The issue_credits of this Character.  # noqa: E501
        :rtype: object
        """
        return self._issue_credits

    @issue_credits.setter
    def issue_credits(self, issue_credits):
        """Sets the issue_credits of this Character.

        List of issues this character appears in.  # noqa: E501

        :param issue_credits: The issue_credits of this Character.  # noqa: E501
        :type: object
        """

        self._issue_credits = issue_credits

    @property
    def issues_died_in(self):
        """Gets the issues_died_in of this Character.  # noqa: E501

        List of issues this character died in.  # noqa: E501

        :return: The issues_died_in of this Character.  # noqa: E501
        :rtype: object
        """
        return self._issues_died_in

    @issues_died_in.setter
    def issues_died_in(self, issues_died_in):
        """Sets the issues_died_in of this Character.

        List of issues this character died in.  # noqa: E501

        :param issues_died_in: The issues_died_in of this Character.  # noqa: E501
        :type: object
        """

        self._issues_died_in = issues_died_in

    @property
    def movies(self):
        """Gets the movies of this Character.  # noqa: E501

        Movies the character was in.  # noqa: E501

        :return: The movies of this Character.  # noqa: E501
        :rtype: object
        """
        return self._movies

    @movies.setter
    def movies(self, movies):
        """Sets the movies of this Character.

        Movies the character was in.  # noqa: E501

        :param movies: The movies of this Character.  # noqa: E501
        :type: object
        """

        self._movies = movies

    @property
    def origin(self):
        """Gets the origin of this Character.  # noqa: E501

        The origin of the character. Human, Alien, Robot ...etc  # noqa: E501

        :return: The origin of this Character.  # noqa: E501
        :rtype: object
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this Character.

        The origin of the character. Human, Alien, Robot ...etc  # noqa: E501

        :param origin: The origin of this Character.  # noqa: E501
        :type: object
        """

        self._origin = origin

    @property
    def powers(self):
        """Gets the powers of this Character.  # noqa: E501

        List of super powers a character has.  # noqa: E501

        :return: The powers of this Character.  # noqa: E501
        :rtype: object
        """
        return self._powers

    @powers.setter
    def powers(self, powers):
        """Sets the powers of this Character.

        List of super powers a character has.  # noqa: E501

        :param powers: The powers of this Character.  # noqa: E501
        :type: object
        """

        self._powers = powers

    @property
    def publisher(self):
        """Gets the publisher of this Character.  # noqa: E501

        The primary publisher a character is attached to.  # noqa: E501

        :return: The publisher of this Character.  # noqa: E501
        :rtype: object
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this Character.

        The primary publisher a character is attached to.  # noqa: E501

        :param publisher: The publisher of this Character.  # noqa: E501
        :type: object
        """

        self._publisher = publisher

    @property
    def real_name(self):
        """Gets the real_name of this Character.  # noqa: E501

        Real name of the character.  # noqa: E501

        :return: The real_name of this Character.  # noqa: E501
        :rtype: object
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this Character.

        Real name of the character.  # noqa: E501

        :param real_name: The real_name of this Character.  # noqa: E501
        :type: object
        """

        self._real_name = real_name

    @property
    def story_arc_credits(self):
        """Gets the story_arc_credits of this Character.  # noqa: E501

        List of story arcs this character appears in.  # noqa: E501

        :return: The story_arc_credits of this Character.  # noqa: E501
        :rtype: object
        """
        return self._story_arc_credits

    @story_arc_credits.setter
    def story_arc_credits(self, story_arc_credits):
        """Sets the story_arc_credits of this Character.

        List of story arcs this character appears in.  # noqa: E501

        :param story_arc_credits: The story_arc_credits of this Character.  # noqa: E501
        :type: object
        """

        self._story_arc_credits = story_arc_credits

    @property
    def team_enemies(self):
        """Gets the team_enemies of this Character.  # noqa: E501

        List of teams that are enemies of this character.  # noqa: E501

        :return: The team_enemies of this Character.  # noqa: E501
        :rtype: object
        """
        return self._team_enemies

    @team_enemies.setter
    def team_enemies(self, team_enemies):
        """Sets the team_enemies of this Character.

        List of teams that are enemies of this character.  # noqa: E501

        :param team_enemies: The team_enemies of this Character.  # noqa: E501
        :type: object
        """

        self._team_enemies = team_enemies

    @property
    def team_friends(self):
        """Gets the team_friends of this Character.  # noqa: E501

        List of teams that are friends with this character.  # noqa: E501

        :return: The team_friends of this Character.  # noqa: E501
        :rtype: object
        """
        return self._team_friends

    @team_friends.setter
    def team_friends(self, team_friends):
        """Sets the team_friends of this Character.

        List of teams that are friends with this character.  # noqa: E501

        :param team_friends: The team_friends of this Character.  # noqa: E501
        :type: object
        """

        self._team_friends = team_friends

    @property
    def teams(self):
        """Gets the teams of this Character.  # noqa: E501

        List of teams this character is a member of.  # noqa: E501

        :return: The teams of this Character.  # noqa: E501
        :rtype: object
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this Character.

        List of teams this character is a member of.  # noqa: E501

        :param teams: The teams of this Character.  # noqa: E501
        :type: object
        """

        self._teams = teams

    @property
    def volume_credits(self):
        """Gets the volume_credits of this Character.  # noqa: E501

        List of comic volumes this character appears in.  # noqa: E501

        :return: The volume_credits of this Character.  # noqa: E501
        :rtype: object
        """
        return self._volume_credits

    @volume_credits.setter
    def volume_credits(self, volume_credits):
        """Sets the volume_credits of this Character.

        List of comic volumes this character appears in.  # noqa: E501

        :param volume_credits: The volume_credits of this Character.  # noqa: E501
        :type: object
        """

        self._volume_credits = volume_credits

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
        if not isinstance(other, Character):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Character):
            return True

        return self.to_dict() != other.to_dict()
