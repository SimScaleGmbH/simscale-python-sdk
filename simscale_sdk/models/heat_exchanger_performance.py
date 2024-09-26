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


class HeatExchangerPerformance(object):
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
        'ref_temperature': 'DimensionalFunctionTemperature',
        'performance': 'DimensionalFunctionTotalThermalTransmittance'
    }

    attribute_map = {
        'type': 'type',
        'ref_temperature': 'refTemperature',
        'performance': 'performance'
    }

    def __init__(self, type='HEAT_EXCHANGER_PERFORMANCE', ref_temperature=None, performance=None, local_vars_configuration=None):  # noqa: E501
        """HeatExchangerPerformance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._ref_temperature = None
        self._performance = None
        self.discriminator = None

        self.type = type
        if ref_temperature is not None:
            self.ref_temperature = ref_temperature
        if performance is not None:
            self.performance = performance

    @property
    def type(self):
        """Gets the type of this HeatExchangerPerformance.  # noqa: E501

        Schema name: HeatExchangerPerformance  # noqa: E501

        :return: The type of this HeatExchangerPerformance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HeatExchangerPerformance.

        Schema name: HeatExchangerPerformance  # noqa: E501

        :param type: The type of this HeatExchangerPerformance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def ref_temperature(self):
        """Gets the ref_temperature of this HeatExchangerPerformance.  # noqa: E501


        :return: The ref_temperature of this HeatExchangerPerformance.  # noqa: E501
        :rtype: DimensionalFunctionTemperature
        """
        return self._ref_temperature

    @ref_temperature.setter
    def ref_temperature(self, ref_temperature):
        """Sets the ref_temperature of this HeatExchangerPerformance.


        :param ref_temperature: The ref_temperature of this HeatExchangerPerformance.  # noqa: E501
        :type: DimensionalFunctionTemperature
        """

        self._ref_temperature = ref_temperature

    @property
    def performance(self):
        """Gets the performance of this HeatExchangerPerformance.  # noqa: E501


        :return: The performance of this HeatExchangerPerformance.  # noqa: E501
        :rtype: DimensionalFunctionTotalThermalTransmittance
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this HeatExchangerPerformance.


        :param performance: The performance of this HeatExchangerPerformance.  # noqa: E501
        :type: DimensionalFunctionTotalThermalTransmittance
        """

        self._performance = performance

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
        if not isinstance(other, HeatExchangerPerformance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HeatExchangerPerformance):
            return True

        return self.to_dict() != other.to_dict()