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


class TotalTBC(object):
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
        'total_temperature': 'DimensionalTemperature',
        'total_temperature_function': 'DimensionalFunctionTemperature',
        'specific_heat_ratio': 'float'
    }

    attribute_map = {
        'type': 'type',
        'total_temperature': 'totalTemperature',
        'total_temperature_function': 'totalTemperatureFunction',
        'specific_heat_ratio': 'specificHeatRatio'
    }

    def __init__(self, type='TOTAL_TEMPERATURE', total_temperature=None, total_temperature_function=None, specific_heat_ratio=None, local_vars_configuration=None):  # noqa: E501
        """TotalTBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._total_temperature = None
        self._total_temperature_function = None
        self._specific_heat_ratio = None
        self.discriminator = None

        self.type = type
        if total_temperature is not None:
            self.total_temperature = total_temperature
        if total_temperature_function is not None:
            self.total_temperature_function = total_temperature_function
        if specific_heat_ratio is not None:
            self.specific_heat_ratio = specific_heat_ratio

    @property
    def type(self):
        """Gets the type of this TotalTBC.  # noqa: E501

        Schema name: TotalTBC  # noqa: E501

        :return: The type of this TotalTBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TotalTBC.

        Schema name: TotalTBC  # noqa: E501

        :param type: The type of this TotalTBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def total_temperature(self):
        """Gets the total_temperature of this TotalTBC.  # noqa: E501


        :return: The total_temperature of this TotalTBC.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._total_temperature

    @total_temperature.setter
    def total_temperature(self, total_temperature):
        """Sets the total_temperature of this TotalTBC.


        :param total_temperature: The total_temperature of this TotalTBC.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._total_temperature = total_temperature

    @property
    def total_temperature_function(self):
        """Gets the total_temperature_function of this TotalTBC.  # noqa: E501


        :return: The total_temperature_function of this TotalTBC.  # noqa: E501
        :rtype: DimensionalFunctionTemperature
        """
        return self._total_temperature_function

    @total_temperature_function.setter
    def total_temperature_function(self, total_temperature_function):
        """Sets the total_temperature_function of this TotalTBC.


        :param total_temperature_function: The total_temperature_function of this TotalTBC.  # noqa: E501
        :type: DimensionalFunctionTemperature
        """

        self._total_temperature_function = total_temperature_function

    @property
    def specific_heat_ratio(self):
        """Gets the specific_heat_ratio of this TotalTBC.  # noqa: E501


        :return: The specific_heat_ratio of this TotalTBC.  # noqa: E501
        :rtype: float
        """
        return self._specific_heat_ratio

    @specific_heat_ratio.setter
    def specific_heat_ratio(self, specific_heat_ratio):
        """Sets the specific_heat_ratio of this TotalTBC.


        :param specific_heat_ratio: The specific_heat_ratio of this TotalTBC.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                specific_heat_ratio is not None and specific_heat_ratio <= 0):  # noqa: E501
            raise ValueError("Invalid value for `specific_heat_ratio`, must be a value greater than `0`")  # noqa: E501

        self._specific_heat_ratio = specific_heat_ratio

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
        if not isinstance(other, TotalTBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TotalTBC):
            return True

        return self.to_dict() != other.to_dict()
