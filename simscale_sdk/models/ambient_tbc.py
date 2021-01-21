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


class AmbientTBC(object):
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
        'ambient_temperature': 'DimensionalTemperature'
    }

    attribute_map = {
        'type': 'type',
        'ambient_temperature': 'ambientTemperature'
    }

    def __init__(self, type='AMBIENT_TEMPERATURE', ambient_temperature=None, local_vars_configuration=None):  # noqa: E501
        """AmbientTBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._ambient_temperature = None
        self.discriminator = None

        self.type = type
        if ambient_temperature is not None:
            self.ambient_temperature = ambient_temperature

    @property
    def type(self):
        """Gets the type of this AmbientTBC.  # noqa: E501


        :return: The type of this AmbientTBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AmbientTBC.


        :param type: The type of this AmbientTBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def ambient_temperature(self):
        """Gets the ambient_temperature of this AmbientTBC.  # noqa: E501


        :return: The ambient_temperature of this AmbientTBC.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._ambient_temperature

    @ambient_temperature.setter
    def ambient_temperature(self, ambient_temperature):
        """Sets the ambient_temperature of this AmbientTBC.


        :param ambient_temperature: The ambient_temperature of this AmbientTBC.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._ambient_temperature = ambient_temperature

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
        if not isinstance(other, AmbientTBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AmbientTBC):
            return True

        return self.to_dict() != other.to_dict()
