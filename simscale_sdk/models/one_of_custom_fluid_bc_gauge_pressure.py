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


class OneOfCustomFluidBCGaugePressure(object):
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
        'fan_pressure': 'DimensionalFunctionPressure',
        'direction': 'str',
        'environmental_total_pressure': 'DimensionalPressure',
        'gamma': 'DimensionalFunctionDimensionless',
        'gradient': 'DimensionalForceDensity',
        'value': 'DimensionalPressure',
        'total_pressure': 'DimensionalFunctionPressure'
    }

    attribute_map = {
        'type': 'type',
        'fan_pressure': 'fanPressure',
        'direction': 'direction',
        'environmental_total_pressure': 'environmentalTotalPressure',
        'gamma': 'gamma',
        'gradient': 'gradient',
        'value': 'value',
        'total_pressure': 'totalPressure'
    }

    discriminator_value_class_map = {
        'SYMMETRY': 'SymmetryPBC',
        'FAN_PRESSURE': 'FanPBC',
        'FIXED_GRADIENT': 'FixedGradientPBC',
        'FIXED_VALUE': 'FixedValuePBC',
        'FREESTREAM': 'FreestreamPBC',
        'FIXED_MEAN': 'MeanValuePBC',
        'ZERO_GRADIENT': 'ZeroGradientPBC',
        'TOTAL_PRESSURE': 'TotalPBC'
    }

    def __init__(self, type='TOTAL_PRESSURE', fan_pressure=None, direction=None, environmental_total_pressure=None, gamma=None, gradient=None, value=None, total_pressure=None, local_vars_configuration=None):  # noqa: E501
        """OneOfCustomFluidBCGaugePressure - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._fan_pressure = None
        self._direction = None
        self._environmental_total_pressure = None
        self._gamma = None
        self._gradient = None
        self._value = None
        self._total_pressure = None
        self.discriminator = 'type'

        self.type = type
        if fan_pressure is not None:
            self.fan_pressure = fan_pressure
        if direction is not None:
            self.direction = direction
        if environmental_total_pressure is not None:
            self.environmental_total_pressure = environmental_total_pressure
        if gamma is not None:
            self.gamma = gamma
        if gradient is not None:
            self.gradient = gradient
        if value is not None:
            self.value = value
        if total_pressure is not None:
            self.total_pressure = total_pressure

    @property
    def type(self):
        """Gets the type of this OneOfCustomFluidBCGaugePressure.  # noqa: E501


        :return: The type of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfCustomFluidBCGaugePressure.


        :param type: The type of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fan_pressure(self):
        """Gets the fan_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501


        :return: The fan_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._fan_pressure

    @fan_pressure.setter
    def fan_pressure(self, fan_pressure):
        """Sets the fan_pressure of this OneOfCustomFluidBCGaugePressure.


        :param fan_pressure: The fan_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._fan_pressure = fan_pressure

    @property
    def direction(self):
        """Gets the direction of this OneOfCustomFluidBCGaugePressure.  # noqa: E501


        :return: The direction of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this OneOfCustomFluidBCGaugePressure.


        :param direction: The direction of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN", "OUT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and direction not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def environmental_total_pressure(self):
        """Gets the environmental_total_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501


        :return: The environmental_total_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._environmental_total_pressure

    @environmental_total_pressure.setter
    def environmental_total_pressure(self, environmental_total_pressure):
        """Sets the environmental_total_pressure of this OneOfCustomFluidBCGaugePressure.


        :param environmental_total_pressure: The environmental_total_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :type: DimensionalPressure
        """

        self._environmental_total_pressure = environmental_total_pressure

    @property
    def gamma(self):
        """Gets the gamma of this OneOfCustomFluidBCGaugePressure.  # noqa: E501


        :return: The gamma of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :rtype: DimensionalFunctionDimensionless
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this OneOfCustomFluidBCGaugePressure.


        :param gamma: The gamma of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :type: DimensionalFunctionDimensionless
        """

        self._gamma = gamma

    @property
    def gradient(self):
        """Gets the gradient of this OneOfCustomFluidBCGaugePressure.  # noqa: E501


        :return: The gradient of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :rtype: DimensionalForceDensity
        """
        return self._gradient

    @gradient.setter
    def gradient(self, gradient):
        """Sets the gradient of this OneOfCustomFluidBCGaugePressure.


        :param gradient: The gradient of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :type: DimensionalForceDensity
        """

        self._gradient = gradient

    @property
    def value(self):
        """Gets the value of this OneOfCustomFluidBCGaugePressure.  # noqa: E501


        :return: The value of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneOfCustomFluidBCGaugePressure.


        :param value: The value of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :type: DimensionalPressure
        """

        self._value = value

    @property
    def total_pressure(self):
        """Gets the total_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501


        :return: The total_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._total_pressure

    @total_pressure.setter
    def total_pressure(self, total_pressure):
        """Sets the total_pressure of this OneOfCustomFluidBCGaugePressure.


        :param total_pressure: The total_pressure of this OneOfCustomFluidBCGaugePressure.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._total_pressure = total_pressure

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
        if not isinstance(other, OneOfCustomFluidBCGaugePressure):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfCustomFluidBCGaugePressure):
            return True

        return self.to_dict() != other.to_dict()
