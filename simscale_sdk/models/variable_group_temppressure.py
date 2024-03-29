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


class VariableGroupTEMPPRESSURE(object):
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
        'temperature': 'UnitTemperature',
        'pressure': 'UnitPressure'
    }

    attribute_map = {
        'temperature': 'Temperature',
        'pressure': 'Pressure'
    }

    def __init__(self, temperature=None, pressure=None, local_vars_configuration=None):  # noqa: E501
        """VariableGroupTEMPPRESSURE - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._temperature = None
        self._pressure = None
        self.discriminator = None

        if temperature is not None:
            self.temperature = temperature
        if pressure is not None:
            self.pressure = pressure

    @property
    def temperature(self):
        """Gets the temperature of this VariableGroupTEMPPRESSURE.  # noqa: E501


        :return: The temperature of this VariableGroupTEMPPRESSURE.  # noqa: E501
        :rtype: UnitTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this VariableGroupTEMPPRESSURE.


        :param temperature: The temperature of this VariableGroupTEMPPRESSURE.  # noqa: E501
        :type: UnitTemperature
        """

        self._temperature = temperature

    @property
    def pressure(self):
        """Gets the pressure of this VariableGroupTEMPPRESSURE.  # noqa: E501


        :return: The pressure of this VariableGroupTEMPPRESSURE.  # noqa: E501
        :rtype: UnitPressure
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this VariableGroupTEMPPRESSURE.


        :param pressure: The pressure of this VariableGroupTEMPPRESSURE.  # noqa: E501
        :type: UnitPressure
        """

        self._pressure = pressure

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
        if not isinstance(other, VariableGroupTEMPPRESSURE):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VariableGroupTEMPPRESSURE):
            return True

        return self.to_dict() != other.to_dict()
