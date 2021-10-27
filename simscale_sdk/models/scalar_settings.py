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


class ScalarSettings(object):
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
        'scalar_field': 'ScalarField',
        'minimum_range': 'float',
        'maximum_range': 'float',
        'number_of_divisions': 'int',
        'color_scheme': 'str'
    }

    attribute_map = {
        'scalar_field': 'scalarField',
        'minimum_range': 'minimumRange',
        'maximum_range': 'maximumRange',
        'number_of_divisions': 'numberOfDivisions',
        'color_scheme': 'colorScheme'
    }

    def __init__(self, scalar_field=None, minimum_range=None, maximum_range=None, number_of_divisions=None, color_scheme=None, local_vars_configuration=None):  # noqa: E501
        """ScalarSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scalar_field = None
        self._minimum_range = None
        self._maximum_range = None
        self._number_of_divisions = None
        self._color_scheme = None
        self.discriminator = None

        self.scalar_field = scalar_field
        if minimum_range is not None:
            self.minimum_range = minimum_range
        if maximum_range is not None:
            self.maximum_range = maximum_range
        if number_of_divisions is not None:
            self.number_of_divisions = number_of_divisions
        if color_scheme is not None:
            self.color_scheme = color_scheme

    @property
    def scalar_field(self):
        """Gets the scalar_field of this ScalarSettings.  # noqa: E501


        :return: The scalar_field of this ScalarSettings.  # noqa: E501
        :rtype: ScalarField
        """
        return self._scalar_field

    @scalar_field.setter
    def scalar_field(self, scalar_field):
        """Sets the scalar_field of this ScalarSettings.


        :param scalar_field: The scalar_field of this ScalarSettings.  # noqa: E501
        :type: ScalarField
        """
        if self.local_vars_configuration.client_side_validation and scalar_field is None:  # noqa: E501
            raise ValueError("Invalid value for `scalar_field`, must not be `None`")  # noqa: E501

        self._scalar_field = scalar_field

    @property
    def minimum_range(self):
        """Gets the minimum_range of this ScalarSettings.  # noqa: E501

        The minimum value for the color scheme to fill. Default is the minimum value of the scalar.  # noqa: E501

        :return: The minimum_range of this ScalarSettings.  # noqa: E501
        :rtype: float
        """
        return self._minimum_range

    @minimum_range.setter
    def minimum_range(self, minimum_range):
        """Sets the minimum_range of this ScalarSettings.

        The minimum value for the color scheme to fill. Default is the minimum value of the scalar.  # noqa: E501

        :param minimum_range: The minimum_range of this ScalarSettings.  # noqa: E501
        :type: float
        """

        self._minimum_range = minimum_range

    @property
    def maximum_range(self):
        """Gets the maximum_range of this ScalarSettings.  # noqa: E501

        The maximum value for the color scheme to fill. Default is the maximum value of the scalar.  # noqa: E501

        :return: The maximum_range of this ScalarSettings.  # noqa: E501
        :rtype: float
        """
        return self._maximum_range

    @maximum_range.setter
    def maximum_range(self, maximum_range):
        """Sets the maximum_range of this ScalarSettings.

        The maximum value for the color scheme to fill. Default is the maximum value of the scalar.  # noqa: E501

        :param maximum_range: The maximum_range of this ScalarSettings.  # noqa: E501
        :type: float
        """

        self._maximum_range = maximum_range

    @property
    def number_of_divisions(self):
        """Gets the number_of_divisions of this ScalarSettings.  # noqa: E501

        The number of divisions in the legend.  # noqa: E501

        :return: The number_of_divisions of this ScalarSettings.  # noqa: E501
        :rtype: int
        """
        return self._number_of_divisions

    @number_of_divisions.setter
    def number_of_divisions(self, number_of_divisions):
        """Sets the number_of_divisions of this ScalarSettings.

        The number of divisions in the legend.  # noqa: E501

        :param number_of_divisions: The number_of_divisions of this ScalarSettings.  # noqa: E501
        :type: int
        """

        self._number_of_divisions = number_of_divisions

    @property
    def color_scheme(self):
        """Gets the color_scheme of this ScalarSettings.  # noqa: E501

        The color scheme to use to map scalar values on the model and legend bar.  # noqa: E501

        :return: The color_scheme of this ScalarSettings.  # noqa: E501
        :rtype: str
        """
        return self._color_scheme

    @color_scheme.setter
    def color_scheme(self, color_scheme):
        """Sets the color_scheme of this ScalarSettings.

        The color scheme to use to map scalar values on the model and legend bar.  # noqa: E501

        :param color_scheme: The color_scheme of this ScalarSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["NORMAL", "NORMAL_INVERTED", "BLACK_TO_WHITE", "WHITE_TO_BLACK", "GREEN_TO_BROWN", "WHITE_TO_BROWN", "METAL_CASTING", "BLUE_TO_WHITE_TO_RED", "THERMAL_1", "THERMAL_2", "THERMAL_3"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and color_scheme not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `color_scheme` ({0}), must be one of {1}"  # noqa: E501
                .format(color_scheme, allowed_values)
            )

        self._color_scheme = color_scheme

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
        if not isinstance(other, ScalarSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScalarSettings):
            return True

        return self.to_dict() != other.to_dict()
