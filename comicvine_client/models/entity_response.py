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


class EntityResponse(object):
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
        'status_code': 'int',
        'error': 'str',
        'number_of_total_results': 'int',
        'number_of_page_results': 'int',
        'results': 'OneOfVolumeIssuePersonCharacter'
    }

    attribute_map = {
        'status_code': 'status_code',
        'error': 'error',
        'number_of_total_results': 'number_of_total_results',
        'number_of_page_results': 'number_of_page_results',
        'results': 'results'
    }

    def __init__(self, status_code=None, error=None, number_of_total_results=None, number_of_page_results=None, results=None, local_vars_configuration=None):  # noqa: E501
        """EntityResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status_code = None
        self._error = None
        self._number_of_total_results = None
        self._number_of_page_results = None
        self._results = None
        self.discriminator = None

        if status_code is not None:
            self.status_code = status_code
        if error is not None:
            self.error = error
        if number_of_total_results is not None:
            self.number_of_total_results = number_of_total_results
        if number_of_page_results is not None:
            self.number_of_page_results = number_of_page_results
        if results is not None:
            self.results = results

    @property
    def status_code(self):
        """Gets the status_code of this EntityResponse.  # noqa: E501

        An integer indicating the result of the request. Acceptable values are:   - 1:OK   - 100:Invalid API Key   - 101:Object Not Found   - 102:Error in URL Format   - 103:'jsonp' format requires a 'json_callback' argument   - 104:Filter Error   - 105:Subscriber only video is for subscribers only   # noqa: E501

        :return: The status_code of this EntityResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this EntityResponse.

        An integer indicating the result of the request. Acceptable values are:   - 1:OK   - 100:Invalid API Key   - 101:Object Not Found   - 102:Error in URL Format   - 103:'jsonp' format requires a 'json_callback' argument   - 104:Filter Error   - 105:Subscriber only video is for subscribers only   # noqa: E501

        :param status_code: The status_code of this EntityResponse.  # noqa: E501
        :type status_code: int
        """
        allowed_values = [1, 100, 101, 102, 103, 104, 105]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(status_code, allowed_values)
            )

        self._status_code = status_code

    @property
    def error(self):
        """Gets the error of this EntityResponse.  # noqa: E501

        A text string representing the status_code  # noqa: E501

        :return: The error of this EntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EntityResponse.

        A text string representing the status_code  # noqa: E501

        :param error: The error of this EntityResponse.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def number_of_total_results(self):
        """Gets the number_of_total_results of this EntityResponse.  # noqa: E501

        The number of total results matching the filter conditions specified  # noqa: E501

        :return: The number_of_total_results of this EntityResponse.  # noqa: E501
        :rtype: int
        """
        return self._number_of_total_results

    @number_of_total_results.setter
    def number_of_total_results(self, number_of_total_results):
        """Sets the number_of_total_results of this EntityResponse.

        The number of total results matching the filter conditions specified  # noqa: E501

        :param number_of_total_results: The number_of_total_results of this EntityResponse.  # noqa: E501
        :type number_of_total_results: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_total_results is not None and number_of_total_results < 0):  # noqa: E501
            raise ValueError("Invalid value for `number_of_total_results`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_of_total_results = number_of_total_results

    @property
    def number_of_page_results(self):
        """Gets the number_of_page_results of this EntityResponse.  # noqa: E501

        The number of results on this page  # noqa: E501

        :return: The number_of_page_results of this EntityResponse.  # noqa: E501
        :rtype: int
        """
        return self._number_of_page_results

    @number_of_page_results.setter
    def number_of_page_results(self, number_of_page_results):
        """Sets the number_of_page_results of this EntityResponse.

        The number of results on this page  # noqa: E501

        :param number_of_page_results: The number_of_page_results of this EntityResponse.  # noqa: E501
        :type number_of_page_results: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_page_results is not None and number_of_page_results < 0):  # noqa: E501
            raise ValueError("Invalid value for `number_of_page_results`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_of_page_results = number_of_page_results

    @property
    def results(self):
        """Gets the results of this EntityResponse.  # noqa: E501

        An Entity that match the filters specified  # noqa: E501

        :return: The results of this EntityResponse.  # noqa: E501
        :rtype: OneOfVolumeIssuePersonCharacter
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this EntityResponse.

        An Entity that match the filters specified  # noqa: E501

        :param results: The results of this EntityResponse.  # noqa: E501
        :type results: OneOfVolumeIssuePersonCharacter
        """

        self._results = results

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
        if not isinstance(other, EntityResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityResponse):
            return True

        return self.to_dict() != other.to_dict()
