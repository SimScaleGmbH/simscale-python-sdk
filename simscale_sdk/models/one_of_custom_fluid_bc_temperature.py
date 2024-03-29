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


class OneOfCustomFluidBCTemperature(object):
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
        'heat_flux': 'OneOfExternalWallHeatFluxTBCHeatFlux',
        'value': 'DimensionalTemperature',
        'gradient': 'DimensionalFunctionTemperatureGradient',
        'total_temperature': 'DimensionalTemperature',
        'total_temperature_function': 'DimensionalFunctionTemperature',
        'specific_heat_ratio': 'float',
        'heat_source': 'OneOfTurbulentHeatFluxTBCHeatSource',
        'wall_temperature': 'DimensionalTemperature',
        'thermal_diffusivity': 'DimensionalKinematicViscosity'
    }

    attribute_map = {
        'type': 'type',
        'heat_flux': 'heatFlux',
        'value': 'value',
        'gradient': 'gradient',
        'total_temperature': 'totalTemperature',
        'total_temperature_function': 'totalTemperatureFunction',
        'specific_heat_ratio': 'specificHeatRatio',
        'heat_source': 'heatSource',
        'wall_temperature': 'wallTemperature',
        'thermal_diffusivity': 'thermalDiffusivity'
    }

    discriminator_value_class_map = {
        'EXTERNAL_WALL_HEAT_FLUX_TEMPERATURE': 'ExternalWallHeatFluxTBC',
        'FIXED_GRADIENT': 'FixedGradientTBC',
        'FIXED_VALUE': 'FixedValueTBC',
        'INLET_OUTLET': 'InletOutletTBC',
        'ADIABATIC': 'AdiabaticTBC',
        'SYMMETRY': 'SymmetryTBC',
        'TOTAL_TEMPERATURE': 'TotalTBC',
        'TURBULENT_HEAT_FLUX_TEMPERATURE': 'TurbulentHeatFluxTBC',
        'WALL_HEAT_TRANSFER': 'WallHeatTransferTBC'
    }

    def __init__(self, type='WALL_HEAT_TRANSFER', heat_flux=None, value=None, gradient=None, total_temperature=None, total_temperature_function=None, specific_heat_ratio=None, heat_source=None, wall_temperature=None, thermal_diffusivity=None, local_vars_configuration=None):  # noqa: E501
        """OneOfCustomFluidBCTemperature - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._heat_flux = None
        self._value = None
        self._gradient = None
        self._total_temperature = None
        self._total_temperature_function = None
        self._specific_heat_ratio = None
        self._heat_source = None
        self._wall_temperature = None
        self._thermal_diffusivity = None
        self.discriminator = 'type'

        self.type = type
        if heat_flux is not None:
            self.heat_flux = heat_flux
        if value is not None:
            self.value = value
        if gradient is not None:
            self.gradient = gradient
        if total_temperature is not None:
            self.total_temperature = total_temperature
        if total_temperature_function is not None:
            self.total_temperature_function = total_temperature_function
        if specific_heat_ratio is not None:
            self.specific_heat_ratio = specific_heat_ratio
        if heat_source is not None:
            self.heat_source = heat_source
        if wall_temperature is not None:
            self.wall_temperature = wall_temperature
        if thermal_diffusivity is not None:
            self.thermal_diffusivity = thermal_diffusivity

    @property
    def type(self):
        """Gets the type of this OneOfCustomFluidBCTemperature.  # noqa: E501

        Schema name: WallHeatTransferTBC  # noqa: E501

        :return: The type of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfCustomFluidBCTemperature.

        Schema name: WallHeatTransferTBC  # noqa: E501

        :param type: The type of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def heat_flux(self):
        """Gets the heat_flux of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The heat_flux of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: OneOfExternalWallHeatFluxTBCHeatFlux
        """
        return self._heat_flux

    @heat_flux.setter
    def heat_flux(self, heat_flux):
        """Sets the heat_flux of this OneOfCustomFluidBCTemperature.


        :param heat_flux: The heat_flux of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: OneOfExternalWallHeatFluxTBCHeatFlux
        """

        self._heat_flux = heat_flux

    @property
    def value(self):
        """Gets the value of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The value of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneOfCustomFluidBCTemperature.


        :param value: The value of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._value = value

    @property
    def gradient(self):
        """Gets the gradient of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The gradient of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: DimensionalFunctionTemperatureGradient
        """
        return self._gradient

    @gradient.setter
    def gradient(self, gradient):
        """Sets the gradient of this OneOfCustomFluidBCTemperature.


        :param gradient: The gradient of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: DimensionalFunctionTemperatureGradient
        """

        self._gradient = gradient

    @property
    def total_temperature(self):
        """Gets the total_temperature of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The total_temperature of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._total_temperature

    @total_temperature.setter
    def total_temperature(self, total_temperature):
        """Sets the total_temperature of this OneOfCustomFluidBCTemperature.


        :param total_temperature: The total_temperature of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._total_temperature = total_temperature

    @property
    def total_temperature_function(self):
        """Gets the total_temperature_function of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The total_temperature_function of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: DimensionalFunctionTemperature
        """
        return self._total_temperature_function

    @total_temperature_function.setter
    def total_temperature_function(self, total_temperature_function):
        """Sets the total_temperature_function of this OneOfCustomFluidBCTemperature.


        :param total_temperature_function: The total_temperature_function of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: DimensionalFunctionTemperature
        """

        self._total_temperature_function = total_temperature_function

    @property
    def specific_heat_ratio(self):
        """Gets the specific_heat_ratio of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The specific_heat_ratio of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: float
        """
        return self._specific_heat_ratio

    @specific_heat_ratio.setter
    def specific_heat_ratio(self, specific_heat_ratio):
        """Sets the specific_heat_ratio of this OneOfCustomFluidBCTemperature.


        :param specific_heat_ratio: The specific_heat_ratio of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                specific_heat_ratio is not None and specific_heat_ratio <= 0):  # noqa: E501
            raise ValueError("Invalid value for `specific_heat_ratio`, must be a value greater than `0`")  # noqa: E501

        self._specific_heat_ratio = specific_heat_ratio

    @property
    def heat_source(self):
        """Gets the heat_source of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The heat_source of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: OneOfTurbulentHeatFluxTBCHeatSource
        """
        return self._heat_source

    @heat_source.setter
    def heat_source(self, heat_source):
        """Sets the heat_source of this OneOfCustomFluidBCTemperature.


        :param heat_source: The heat_source of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: OneOfTurbulentHeatFluxTBCHeatSource
        """

        self._heat_source = heat_source

    @property
    def wall_temperature(self):
        """Gets the wall_temperature of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The wall_temperature of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._wall_temperature

    @wall_temperature.setter
    def wall_temperature(self, wall_temperature):
        """Sets the wall_temperature of this OneOfCustomFluidBCTemperature.


        :param wall_temperature: The wall_temperature of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._wall_temperature = wall_temperature

    @property
    def thermal_diffusivity(self):
        """Gets the thermal_diffusivity of this OneOfCustomFluidBCTemperature.  # noqa: E501


        :return: The thermal_diffusivity of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :rtype: DimensionalKinematicViscosity
        """
        return self._thermal_diffusivity

    @thermal_diffusivity.setter
    def thermal_diffusivity(self, thermal_diffusivity):
        """Sets the thermal_diffusivity of this OneOfCustomFluidBCTemperature.


        :param thermal_diffusivity: The thermal_diffusivity of this OneOfCustomFluidBCTemperature.  # noqa: E501
        :type: DimensionalKinematicViscosity
        """

        self._thermal_diffusivity = thermal_diffusivity

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
        if not isinstance(other, OneOfCustomFluidBCTemperature):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfCustomFluidBCTemperature):
            return True

        return self.to_dict() != other.to_dict()
