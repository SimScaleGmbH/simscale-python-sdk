# coding: utf-8

"""
    SimScale API

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from simscale_sdk.configuration import Configuration


class Duration(object):
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
        'value': 'str',
        'interval_min': 'str',
        'interval_max': 'str'
    }

    attribute_map = {
        'value': 'value',
        'interval_min': 'intervalMin',
        'interval_max': 'intervalMax'
    }

    def __init__(self, value=None, interval_min=None, interval_max=None, local_vars_configuration=None):  # noqa: E501
        """Duration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._interval_min = None
        self._interval_max = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if interval_min is not None:
            self.interval_min = interval_min
        if interval_max is not None:
            self.interval_max = interval_max

    @property
    def value(self):
        """Gets the value of this Duration.  # noqa: E501


        :return: The value of this Duration.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Duration.


        :param value: The value of this Duration.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def interval_min(self):
        """Gets the interval_min of this Duration.  # noqa: E501


        :return: The interval_min of this Duration.  # noqa: E501
        :rtype: str
        """
        return self._interval_min

    @interval_min.setter
    def interval_min(self, interval_min):
        """Sets the interval_min of this Duration.


        :param interval_min: The interval_min of this Duration.  # noqa: E501
        :type: str
        """

        self._interval_min = interval_min

    @property
    def interval_max(self):
        """Gets the interval_max of this Duration.  # noqa: E501


        :return: The interval_max of this Duration.  # noqa: E501
        :rtype: str
        """
        return self._interval_max

    @interval_max.setter
    def interval_max(self, interval_max):
        """Sets the interval_max of this Duration.


        :param interval_max: The interval_max of this Duration.  # noqa: E501
        :type: str
        """

        self._interval_max = interval_max

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
        if not isinstance(other, Duration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Duration):
            return True

        return self.to_dict() != other.to_dict()
