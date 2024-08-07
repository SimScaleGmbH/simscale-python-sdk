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


class ElectromagneticVoltageTypeSinusoidal(object):
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
        'frequency': 'DimensionalFrequency',
        'amplitude': 'DimensionalElectricPotential',
        'offset': 'DimensionalElectricPotential',
        'time_offset': 'DimensionalTime'
    }

    attribute_map = {
        'type': 'type',
        'frequency': 'frequency',
        'amplitude': 'amplitude',
        'offset': 'offset',
        'time_offset': 'timeOffset'
    }

    def __init__(self, type='VOLTAGE_TYPE_SINUSOIDAL', frequency=None, amplitude=None, offset=None, time_offset=None, local_vars_configuration=None):  # noqa: E501
        """ElectromagneticVoltageTypeSinusoidal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._frequency = None
        self._amplitude = None
        self._offset = None
        self._time_offset = None
        self.discriminator = None

        self.type = type
        if frequency is not None:
            self.frequency = frequency
        if amplitude is not None:
            self.amplitude = amplitude
        if offset is not None:
            self.offset = offset
        if time_offset is not None:
            self.time_offset = time_offset

    @property
    def type(self):
        """Gets the type of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501

        Schema name: ElectromagneticVoltageTypeSinusoidal  # noqa: E501

        :return: The type of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElectromagneticVoltageTypeSinusoidal.

        Schema name: ElectromagneticVoltageTypeSinusoidal  # noqa: E501

        :param type: The type of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def frequency(self):
        """Gets the frequency of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501


        :return: The frequency of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ElectromagneticVoltageTypeSinusoidal.


        :param frequency: The frequency of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._frequency = frequency

    @property
    def amplitude(self):
        """Gets the amplitude of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501


        :return: The amplitude of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :rtype: DimensionalElectricPotential
        """
        return self._amplitude

    @amplitude.setter
    def amplitude(self, amplitude):
        """Sets the amplitude of this ElectromagneticVoltageTypeSinusoidal.


        :param amplitude: The amplitude of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :type: DimensionalElectricPotential
        """

        self._amplitude = amplitude

    @property
    def offset(self):
        """Gets the offset of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501


        :return: The offset of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :rtype: DimensionalElectricPotential
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ElectromagneticVoltageTypeSinusoidal.


        :param offset: The offset of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :type: DimensionalElectricPotential
        """

        self._offset = offset

    @property
    def time_offset(self):
        """Gets the time_offset of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501


        :return: The time_offset of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._time_offset

    @time_offset.setter
    def time_offset(self, time_offset):
        """Sets the time_offset of this ElectromagneticVoltageTypeSinusoidal.


        :param time_offset: The time_offset of this ElectromagneticVoltageTypeSinusoidal.  # noqa: E501
        :type: DimensionalTime
        """

        self._time_offset = time_offset

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
        if not isinstance(other, ElectromagneticVoltageTypeSinusoidal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectromagneticVoltageTypeSinusoidal):
            return True

        return self.to_dict() != other.to_dict()
