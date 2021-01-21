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


class TemperatureResultControlItem(object):
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
        'name': 'str',
        'temperature_type': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'temperature_type': 'temperatureType'
    }

    def __init__(self, type='TEMPERATURE', name=None, temperature_type=None, local_vars_configuration=None):  # noqa: E501
        """TemperatureResultControlItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._temperature_type = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if temperature_type is not None:
            self.temperature_type = temperature_type

    @property
    def type(self):
        """Gets the type of this TemperatureResultControlItem.  # noqa: E501


        :return: The type of this TemperatureResultControlItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemperatureResultControlItem.


        :param type: The type of this TemperatureResultControlItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this TemperatureResultControlItem.  # noqa: E501


        :return: The name of this TemperatureResultControlItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemperatureResultControlItem.


        :param name: The name of this TemperatureResultControlItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def temperature_type(self):
        """Gets the temperature_type of this TemperatureResultControlItem.  # noqa: E501


        :return: The temperature_type of this TemperatureResultControlItem.  # noqa: E501
        :rtype: str
        """
        return self._temperature_type

    @temperature_type.setter
    def temperature_type(self, temperature_type):
        """Sets the temperature_type of this TemperatureResultControlItem.


        :param temperature_type: The temperature_type of this TemperatureResultControlItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIELD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and temperature_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `temperature_type` ({0}), must be one of {1}"  # noqa: E501
                .format(temperature_type, allowed_values)
            )

        self._temperature_type = temperature_type

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
        if not isinstance(other, TemperatureResultControlItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemperatureResultControlItem):
            return True

        return self.to_dict() != other.to_dict()
