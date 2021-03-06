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


class TimeAndPlaceSunDirection(object):
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
        'type': 'str',
        'north_angle': 'DimensionalAngle',
        'geographical_location': 'GeographicalLocation',
        'local_date_time': 'str'
    }

    attribute_map = {
        'type': 'type',
        'north_angle': 'northAngle',
        'geographical_location': 'geographicalLocation',
        'local_date_time': 'localDateTime'
    }

    def __init__(self, type='TIME_AND_PLACE', north_angle=None, geographical_location=None, local_date_time=None, local_vars_configuration=None):  # noqa: E501
        """TimeAndPlaceSunDirection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._north_angle = None
        self._geographical_location = None
        self._local_date_time = None
        self.discriminator = None

        self.type = type
        if north_angle is not None:
            self.north_angle = north_angle
        if geographical_location is not None:
            self.geographical_location = geographical_location
        if local_date_time is not None:
            self.local_date_time = local_date_time

    @property
    def type(self):
        """Gets the type of this TimeAndPlaceSunDirection.  # noqa: E501

        Schema name: TimeAndPlaceSunDirection  # noqa: E501

        :return: The type of this TimeAndPlaceSunDirection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimeAndPlaceSunDirection.

        Schema name: TimeAndPlaceSunDirection  # noqa: E501

        :param type: The type of this TimeAndPlaceSunDirection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def north_angle(self):
        """Gets the north_angle of this TimeAndPlaceSunDirection.  # noqa: E501


        :return: The north_angle of this TimeAndPlaceSunDirection.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._north_angle

    @north_angle.setter
    def north_angle(self, north_angle):
        """Sets the north_angle of this TimeAndPlaceSunDirection.


        :param north_angle: The north_angle of this TimeAndPlaceSunDirection.  # noqa: E501
        :type: DimensionalAngle
        """

        self._north_angle = north_angle

    @property
    def geographical_location(self):
        """Gets the geographical_location of this TimeAndPlaceSunDirection.  # noqa: E501


        :return: The geographical_location of this TimeAndPlaceSunDirection.  # noqa: E501
        :rtype: GeographicalLocation
        """
        return self._geographical_location

    @geographical_location.setter
    def geographical_location(self, geographical_location):
        """Sets the geographical_location of this TimeAndPlaceSunDirection.


        :param geographical_location: The geographical_location of this TimeAndPlaceSunDirection.  # noqa: E501
        :type: GeographicalLocation
        """

        self._geographical_location = geographical_location

    @property
    def local_date_time(self):
        """Gets the local_date_time of this TimeAndPlaceSunDirection.  # noqa: E501


        :return: The local_date_time of this TimeAndPlaceSunDirection.  # noqa: E501
        :rtype: str
        """
        return self._local_date_time

    @local_date_time.setter
    def local_date_time(self, local_date_time):
        """Sets the local_date_time of this TimeAndPlaceSunDirection.


        :param local_date_time: The local_date_time of this TimeAndPlaceSunDirection.  # noqa: E501
        :type: str
        """

        self._local_date_time = local_date_time

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
        if not isinstance(other, TimeAndPlaceSunDirection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeAndPlaceSunDirection):
            return True

        return self.to_dict() != other.to_dict()
