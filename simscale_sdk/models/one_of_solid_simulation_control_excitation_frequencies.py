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


class OneOfSolidSimulationControlExcitationFrequencies(object):
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
        'start_frequency': 'DimensionalFrequency',
        'end_frequency': 'DimensionalFrequency',
        'frequency_stepping': 'RestrictedDimensionalFunctionFrequency'
    }

    attribute_map = {
        'type': 'type',
        'frequency': 'frequency',
        'start_frequency': 'startFrequency',
        'end_frequency': 'endFrequency',
        'frequency_stepping': 'frequencyStepping'
    }

    discriminator_value_class_map = {
        'SINGLE': 'SingleFrequency',
        'LIST_V20': 'FrequencyList'
    }

    def __init__(self, type='LIST_V20', frequency=None, start_frequency=None, end_frequency=None, frequency_stepping=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSolidSimulationControlExcitationFrequencies - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._frequency = None
        self._start_frequency = None
        self._end_frequency = None
        self._frequency_stepping = None
        self.discriminator = 'type'

        self.type = type
        if frequency is not None:
            self.frequency = frequency
        if start_frequency is not None:
            self.start_frequency = start_frequency
        if end_frequency is not None:
            self.end_frequency = end_frequency
        if frequency_stepping is not None:
            self.frequency_stepping = frequency_stepping

    @property
    def type(self):
        """Gets the type of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501

        Schema name: FrequencyList  # noqa: E501

        :return: The type of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSolidSimulationControlExcitationFrequencies.

        Schema name: FrequencyList  # noqa: E501

        :param type: The type of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def frequency(self):
        """Gets the frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501


        :return: The frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this OneOfSolidSimulationControlExcitationFrequencies.


        :param frequency: The frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._frequency = frequency

    @property
    def start_frequency(self):
        """Gets the start_frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501


        :return: The start_frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._start_frequency

    @start_frequency.setter
    def start_frequency(self, start_frequency):
        """Sets the start_frequency of this OneOfSolidSimulationControlExcitationFrequencies.


        :param start_frequency: The start_frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._start_frequency = start_frequency

    @property
    def end_frequency(self):
        """Gets the end_frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501


        :return: The end_frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._end_frequency

    @end_frequency.setter
    def end_frequency(self, end_frequency):
        """Sets the end_frequency of this OneOfSolidSimulationControlExcitationFrequencies.


        :param end_frequency: The end_frequency of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._end_frequency = end_frequency

    @property
    def frequency_stepping(self):
        """Gets the frequency_stepping of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501


        :return: The frequency_stepping of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :rtype: RestrictedDimensionalFunctionFrequency
        """
        return self._frequency_stepping

    @frequency_stepping.setter
    def frequency_stepping(self, frequency_stepping):
        """Sets the frequency_stepping of this OneOfSolidSimulationControlExcitationFrequencies.


        :param frequency_stepping: The frequency_stepping of this OneOfSolidSimulationControlExcitationFrequencies.  # noqa: E501
        :type: RestrictedDimensionalFunctionFrequency
        """

        self._frequency_stepping = frequency_stepping

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
        if not isinstance(other, OneOfSolidSimulationControlExcitationFrequencies):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSolidSimulationControlExcitationFrequencies):
            return True

        return self.to_dict() != other.to_dict()
