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


class OneOfVoltageExcitationVoltageType(object):
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
        'value': 'DimensionalElectricPotential',
        'frequency': 'DimensionalFrequency',
        'amplitude': 'DimensionalElectricPotential',
        'offset': 'DimensionalElectricPotential',
        'time_offset': 'DimensionalTime',
        'values': 'DimensionalFunctionElectricPotential'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'frequency': 'frequency',
        'amplitude': 'amplitude',
        'offset': 'offset',
        'time_offset': 'timeOffset',
        'values': 'values'
    }

    discriminator_value_class_map = {
        'VOLTAGE_TYPE_CONSTANT': 'ElectromagneticVoltageTypeConstant',
        'VOLTAGE_TYPE_SINUSOIDAL': 'ElectromagneticVoltageTypeSinusoidal',
        'VOLTAGE_TYPE_TABLE': 'ElectromagneticVoltageTypeTable'
    }

    def __init__(self, type='VOLTAGE_TYPE_TABLE', value=None, frequency=None, amplitude=None, offset=None, time_offset=None, values=None, local_vars_configuration=None):  # noqa: E501
        """OneOfVoltageExcitationVoltageType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._value = None
        self._frequency = None
        self._amplitude = None
        self._offset = None
        self._time_offset = None
        self._values = None
        self.discriminator = 'type'

        self.type = type
        if value is not None:
            self.value = value
        if frequency is not None:
            self.frequency = frequency
        if amplitude is not None:
            self.amplitude = amplitude
        if offset is not None:
            self.offset = offset
        if time_offset is not None:
            self.time_offset = time_offset
        if values is not None:
            self.values = values

    @property
    def type(self):
        """Gets the type of this OneOfVoltageExcitationVoltageType.  # noqa: E501

        Schema name: ElectromagneticVoltageTypeTable  # noqa: E501

        :return: The type of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfVoltageExcitationVoltageType.

        Schema name: ElectromagneticVoltageTypeTable  # noqa: E501

        :param type: The type of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this OneOfVoltageExcitationVoltageType.  # noqa: E501


        :return: The value of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :rtype: DimensionalElectricPotential
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneOfVoltageExcitationVoltageType.


        :param value: The value of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :type: DimensionalElectricPotential
        """

        self._value = value

    @property
    def frequency(self):
        """Gets the frequency of this OneOfVoltageExcitationVoltageType.  # noqa: E501


        :return: The frequency of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this OneOfVoltageExcitationVoltageType.


        :param frequency: The frequency of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._frequency = frequency

    @property
    def amplitude(self):
        """Gets the amplitude of this OneOfVoltageExcitationVoltageType.  # noqa: E501


        :return: The amplitude of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :rtype: DimensionalElectricPotential
        """
        return self._amplitude

    @amplitude.setter
    def amplitude(self, amplitude):
        """Sets the amplitude of this OneOfVoltageExcitationVoltageType.


        :param amplitude: The amplitude of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :type: DimensionalElectricPotential
        """

        self._amplitude = amplitude

    @property
    def offset(self):
        """Gets the offset of this OneOfVoltageExcitationVoltageType.  # noqa: E501


        :return: The offset of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :rtype: DimensionalElectricPotential
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this OneOfVoltageExcitationVoltageType.


        :param offset: The offset of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :type: DimensionalElectricPotential
        """

        self._offset = offset

    @property
    def time_offset(self):
        """Gets the time_offset of this OneOfVoltageExcitationVoltageType.  # noqa: E501


        :return: The time_offset of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._time_offset

    @time_offset.setter
    def time_offset(self, time_offset):
        """Sets the time_offset of this OneOfVoltageExcitationVoltageType.


        :param time_offset: The time_offset of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :type: DimensionalTime
        """

        self._time_offset = time_offset

    @property
    def values(self):
        """Gets the values of this OneOfVoltageExcitationVoltageType.  # noqa: E501


        :return: The values of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :rtype: DimensionalFunctionElectricPotential
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this OneOfVoltageExcitationVoltageType.


        :param values: The values of this OneOfVoltageExcitationVoltageType.  # noqa: E501
        :type: DimensionalFunctionElectricPotential
        """

        self._values = values

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
        if not isinstance(other, OneOfVoltageExcitationVoltageType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfVoltageExcitationVoltageType):
            return True

        return self.to_dict() != other.to_dict()
