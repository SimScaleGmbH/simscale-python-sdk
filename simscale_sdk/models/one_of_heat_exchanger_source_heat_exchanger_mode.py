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


class OneOfHeatExchangerSourceHeatExchangerMode(object):
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
        'heat_transfer_coefficient': 'DimensionalFunctionThermalTransmittance',
        'surface_area_density': 'DimensionalAbsorptivity',
        'heat_distribution': 'str',
        'performance': 'DimensionalFunctionTotalThermalTransmittance'
    }

    attribute_map = {
        'type': 'type',
        'ref_temperature': 'refTemperature',
        'heat_transfer_coefficient': 'heatTransferCoefficient',
        'surface_area_density': 'surfaceAreaDensity',
        'heat_distribution': 'heatDistribution',
        'performance': 'performance'
    }

    discriminator_value_class_map = {
        'HEAT_TRANSFER_COEFFICIENTS': 'HeatTransferCoefficients',
        'HEAT_EXCHANGER_PERFORMANCE': 'HeatExchangerPerformance'
    }

    def __init__(self, type='HEAT_EXCHANGER_PERFORMANCE', ref_temperature=None, heat_transfer_coefficient=None, surface_area_density=None, heat_distribution=None, performance=None, local_vars_configuration=None):  # noqa: E501
        """OneOfHeatExchangerSourceHeatExchangerMode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._ref_temperature = None
        self._heat_transfer_coefficient = None
        self._surface_area_density = None
        self._heat_distribution = None
        self._performance = None
        self.discriminator = 'type'

        self.type = type
        if ref_temperature is not None:
            self.ref_temperature = ref_temperature
        if heat_transfer_coefficient is not None:
            self.heat_transfer_coefficient = heat_transfer_coefficient
        if surface_area_density is not None:
            self.surface_area_density = surface_area_density
        if heat_distribution is not None:
            self.heat_distribution = heat_distribution
        if performance is not None:
            self.performance = performance

    @property
    def type(self):
        """Gets the type of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501

        Schema name: HeatExchangerPerformance  # noqa: E501

        :return: The type of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfHeatExchangerSourceHeatExchangerMode.

        Schema name: HeatExchangerPerformance  # noqa: E501

        :param type: The type of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def ref_temperature(self):
        """Gets the ref_temperature of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501


        :return: The ref_temperature of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :rtype: DimensionalFunctionTemperature
        """
        return self._ref_temperature

    @ref_temperature.setter
    def ref_temperature(self, ref_temperature):
        """Sets the ref_temperature of this OneOfHeatExchangerSourceHeatExchangerMode.


        :param ref_temperature: The ref_temperature of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :type: DimensionalFunctionTemperature
        """

        self._ref_temperature = ref_temperature

    @property
    def heat_transfer_coefficient(self):
        """Gets the heat_transfer_coefficient of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501


        :return: The heat_transfer_coefficient of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :rtype: DimensionalFunctionThermalTransmittance
        """
        return self._heat_transfer_coefficient

    @heat_transfer_coefficient.setter
    def heat_transfer_coefficient(self, heat_transfer_coefficient):
        """Sets the heat_transfer_coefficient of this OneOfHeatExchangerSourceHeatExchangerMode.


        :param heat_transfer_coefficient: The heat_transfer_coefficient of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :type: DimensionalFunctionThermalTransmittance
        """

        self._heat_transfer_coefficient = heat_transfer_coefficient

    @property
    def surface_area_density(self):
        """Gets the surface_area_density of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501


        :return: The surface_area_density of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :rtype: DimensionalAbsorptivity
        """
        return self._surface_area_density

    @surface_area_density.setter
    def surface_area_density(self, surface_area_density):
        """Sets the surface_area_density of this OneOfHeatExchangerSourceHeatExchangerMode.


        :param surface_area_density: The surface_area_density of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :type: DimensionalAbsorptivity
        """

        self._surface_area_density = surface_area_density

    @property
    def heat_distribution(self):
        """Gets the heat_distribution of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501

        Sampling method for the field temperature (T) in T - Tref. This indicates whether the temperature (T) is averaged on the complete heat exchanger or sampled at each position.  # noqa: E501

        :return: The heat_distribution of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :rtype: str
        """
        return self._heat_distribution

    @heat_distribution.setter
    def heat_distribution(self, heat_distribution):
        """Sets the heat_distribution of this OneOfHeatExchangerSourceHeatExchangerMode.

        Sampling method for the field temperature (T) in T - Tref. This indicates whether the temperature (T) is averaged on the complete heat exchanger or sampled at each position.  # noqa: E501

        :param heat_distribution: The heat_distribution of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["LOCAL", "AVERAGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and heat_distribution not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `heat_distribution` ({0}), must be one of {1}"  # noqa: E501
                .format(heat_distribution, allowed_values)
            )

        self._heat_distribution = heat_distribution

    @property
    def performance(self):
        """Gets the performance of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501


        :return: The performance of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :rtype: DimensionalFunctionTotalThermalTransmittance
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this OneOfHeatExchangerSourceHeatExchangerMode.


        :param performance: The performance of this OneOfHeatExchangerSourceHeatExchangerMode.  # noqa: E501
        :type: DimensionalFunctionTotalThermalTransmittance
        """

        self._performance = performance

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, OneOfHeatExchangerSourceHeatExchangerMode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfHeatExchangerSourceHeatExchangerMode):
            return True

        return self.to_dict() != other.to_dict()
