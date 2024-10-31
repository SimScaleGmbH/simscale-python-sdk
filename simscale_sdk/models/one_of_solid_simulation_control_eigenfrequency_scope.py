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


class OneOfSolidSimulationControlEigenfrequencyScope(object):
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
        'number_of_modes': 'int',
        'start_frequency': 'DimensionalFrequency',
        'end_frequency': 'DimensionalFrequency',
        'number_of_sub_bands': 'int',
        'parallelization_level': 'str',
        'center_frequency': 'DimensionalFrequency'
    }

    attribute_map = {
        'type': 'type',
        'number_of_modes': 'numberOfModes',
        'start_frequency': 'startFrequency',
        'end_frequency': 'endFrequency',
        'number_of_sub_bands': 'numberOfSubBands',
        'parallelization_level': 'parallelizationLevel',
        'center_frequency': 'centerFrequency'
    }

    discriminator_value_class_map = {
        'FIRSTMODE': 'FirstMode',
        'RANGE': 'FrequencyRange',
        'CENTER': 'CenterFrequency'
    }

    def __init__(self, type='CENTER', number_of_modes=None, start_frequency=None, end_frequency=None, number_of_sub_bands=None, parallelization_level=None, center_frequency=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSolidSimulationControlEigenfrequencyScope - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._number_of_modes = None
        self._start_frequency = None
        self._end_frequency = None
        self._number_of_sub_bands = None
        self._parallelization_level = None
        self._center_frequency = None
        self.discriminator = 'type'

        self.type = type
        if number_of_modes is not None:
            self.number_of_modes = number_of_modes
        if start_frequency is not None:
            self.start_frequency = start_frequency
        if end_frequency is not None:
            self.end_frequency = end_frequency
        if number_of_sub_bands is not None:
            self.number_of_sub_bands = number_of_sub_bands
        if parallelization_level is not None:
            self.parallelization_level = parallelization_level
        if center_frequency is not None:
            self.center_frequency = center_frequency

    @property
    def type(self):
        """Gets the type of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501

        Schema name: CenterFrequency  # noqa: E501

        :return: The type of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSolidSimulationControlEigenfrequencyScope.

        Schema name: CenterFrequency  # noqa: E501

        :param type: The type of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def number_of_modes(self):
        """Gets the number_of_modes of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501

        <p>Define the maximum number of eigenfrequencies/eigenmodes, that should be calculated.</p>  # noqa: E501

        :return: The number_of_modes of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :rtype: int
        """
        return self._number_of_modes

    @number_of_modes.setter
    def number_of_modes(self, number_of_modes):
        """Sets the number_of_modes of this OneOfSolidSimulationControlEigenfrequencyScope.

        <p>Define the maximum number of eigenfrequencies/eigenmodes, that should be calculated.</p>  # noqa: E501

        :param number_of_modes: The number_of_modes of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_modes is not None and number_of_modes < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_of_modes`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_modes = number_of_modes

    @property
    def start_frequency(self):
        """Gets the start_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501


        :return: The start_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._start_frequency

    @start_frequency.setter
    def start_frequency(self, start_frequency):
        """Sets the start_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.


        :param start_frequency: The start_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._start_frequency = start_frequency

    @property
    def end_frequency(self):
        """Gets the end_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501


        :return: The end_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._end_frequency

    @end_frequency.setter
    def end_frequency(self, end_frequency):
        """Sets the end_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.


        :param end_frequency: The end_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._end_frequency = end_frequency

    @property
    def number_of_sub_bands(self):
        """Gets the number_of_sub_bands of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501


        :return: The number_of_sub_bands of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :rtype: int
        """
        return self._number_of_sub_bands

    @number_of_sub_bands.setter
    def number_of_sub_bands(self, number_of_sub_bands):
        """Sets the number_of_sub_bands of this OneOfSolidSimulationControlEigenfrequencyScope.


        :param number_of_sub_bands: The number_of_sub_bands of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_sub_bands is not None and number_of_sub_bands > 1000):  # noqa: E501
            raise ValueError("Invalid value for `number_of_sub_bands`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_sub_bands is not None and number_of_sub_bands < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_of_sub_bands`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_sub_bands = number_of_sub_bands

    @property
    def parallelization_level(self):
        """Gets the parallelization_level of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501


        :return: The parallelization_level of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :rtype: str
        """
        return self._parallelization_level

    @parallelization_level.setter
    def parallelization_level(self, parallelization_level):
        """Sets the parallelization_level of this OneOfSolidSimulationControlEigenfrequencyScope.


        :param parallelization_level: The parallelization_level of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMPLETE", "PARTIAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and parallelization_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `parallelization_level` ({0}), must be one of {1}"  # noqa: E501
                .format(parallelization_level, allowed_values)
            )

        self._parallelization_level = parallelization_level

    @property
    def center_frequency(self):
        """Gets the center_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501


        :return: The center_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._center_frequency

    @center_frequency.setter
    def center_frequency(self, center_frequency):
        """Sets the center_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.


        :param center_frequency: The center_frequency of this OneOfSolidSimulationControlEigenfrequencyScope.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._center_frequency = center_frequency

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
        if not isinstance(other, OneOfSolidSimulationControlEigenfrequencyScope):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSolidSimulationControlEigenfrequencyScope):
            return True

        return self.to_dict() != other.to_dict()