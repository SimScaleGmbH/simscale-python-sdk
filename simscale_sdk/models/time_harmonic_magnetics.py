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


class TimeHarmonicMagnetics(object):
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
        'thermal': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'frequency': 'frequency',
        'thermal': 'thermal'
    }

    def __init__(self, type='TIME_HARMONIC_MAGNETICS', frequency=None, thermal=None, local_vars_configuration=None):  # noqa: E501
        """TimeHarmonicMagnetics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._frequency = None
        self._thermal = None
        self.discriminator = None

        self.type = type
        if frequency is not None:
            self.frequency = frequency
        if thermal is not None:
            self.thermal = thermal

    @property
    def type(self):
        """Gets the type of this TimeHarmonicMagnetics.  # noqa: E501

        Schema name: TimeHarmonicMagnetics  # noqa: E501

        :return: The type of this TimeHarmonicMagnetics.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimeHarmonicMagnetics.

        Schema name: TimeHarmonicMagnetics  # noqa: E501

        :param type: The type of this TimeHarmonicMagnetics.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def frequency(self):
        """Gets the frequency of this TimeHarmonicMagnetics.  # noqa: E501


        :return: The frequency of this TimeHarmonicMagnetics.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this TimeHarmonicMagnetics.


        :param frequency: The frequency of this TimeHarmonicMagnetics.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._frequency = frequency

    @property
    def thermal(self):
        """Gets the thermal of this TimeHarmonicMagnetics.  # noqa: E501

        Coupling with thermal solves for the temperature by considering electromagnetic losses such as Ohmic, hysteric or displacement losses.  # noqa: E501

        :return: The thermal of this TimeHarmonicMagnetics.  # noqa: E501
        :rtype: bool
        """
        return self._thermal

    @thermal.setter
    def thermal(self, thermal):
        """Sets the thermal of this TimeHarmonicMagnetics.

        Coupling with thermal solves for the temperature by considering electromagnetic losses such as Ohmic, hysteric or displacement losses.  # noqa: E501

        :param thermal: The thermal of this TimeHarmonicMagnetics.  # noqa: E501
        :type: bool
        """

        self._thermal = thermal

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
        if not isinstance(other, TimeHarmonicMagnetics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeHarmonicMagnetics):
            return True

        return self.to_dict() != other.to_dict()
