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


class GeometricGrowth(object):
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
        'number_of_layers': 'int',
        'total_absolute_thickness': 'DimensionalLength',
        'first_layer_size': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'number_of_layers': 'numberOfLayers',
        'total_absolute_thickness': 'totalAbsoluteThickness',
        'first_layer_size': 'firstLayerSize'
    }

    def __init__(self, type='GEOMETRIC_GROWTH', number_of_layers=None, total_absolute_thickness=None, first_layer_size=None, local_vars_configuration=None):  # noqa: E501
        """GeometricGrowth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._number_of_layers = None
        self._total_absolute_thickness = None
        self._first_layer_size = None
        self.discriminator = None

        self.type = type
        if number_of_layers is not None:
            self.number_of_layers = number_of_layers
        if total_absolute_thickness is not None:
            self.total_absolute_thickness = total_absolute_thickness
        if first_layer_size is not None:
            self.first_layer_size = first_layer_size

    @property
    def type(self):
        """Gets the type of this GeometricGrowth.  # noqa: E501

        Schema name: GeometricGrowth  # noqa: E501

        :return: The type of this GeometricGrowth.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GeometricGrowth.

        Schema name: GeometricGrowth  # noqa: E501

        :param type: The type of this GeometricGrowth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def number_of_layers(self):
        """Gets the number_of_layers of this GeometricGrowth.  # noqa: E501

        The <i>Number of layers</i> defines how many prismatic boundary layers should be created. 3 is default.  # noqa: E501

        :return: The number_of_layers of this GeometricGrowth.  # noqa: E501
        :rtype: int
        """
        return self._number_of_layers

    @number_of_layers.setter
    def number_of_layers(self, number_of_layers):
        """Sets the number_of_layers of this GeometricGrowth.

        The <i>Number of layers</i> defines how many prismatic boundary layers should be created. 3 is default.  # noqa: E501

        :param number_of_layers: The number_of_layers of this GeometricGrowth.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_layers is not None and number_of_layers > 20):  # noqa: E501
            raise ValueError("Invalid value for `number_of_layers`, must be a value less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_layers is not None and number_of_layers < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_of_layers`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_layers = number_of_layers

    @property
    def total_absolute_thickness(self):
        """Gets the total_absolute_thickness of this GeometricGrowth.  # noqa: E501


        :return: The total_absolute_thickness of this GeometricGrowth.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._total_absolute_thickness

    @total_absolute_thickness.setter
    def total_absolute_thickness(self, total_absolute_thickness):
        """Sets the total_absolute_thickness of this GeometricGrowth.


        :param total_absolute_thickness: The total_absolute_thickness of this GeometricGrowth.  # noqa: E501
        :type: DimensionalLength
        """

        self._total_absolute_thickness = total_absolute_thickness

    @property
    def first_layer_size(self):
        """Gets the first_layer_size of this GeometricGrowth.  # noqa: E501


        :return: The first_layer_size of this GeometricGrowth.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._first_layer_size

    @first_layer_size.setter
    def first_layer_size(self, first_layer_size):
        """Sets the first_layer_size of this GeometricGrowth.


        :param first_layer_size: The first_layer_size of this GeometricGrowth.  # noqa: E501
        :type: DimensionalLength
        """

        self._first_layer_size = first_layer_size

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
        if not isinstance(other, GeometricGrowth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeometricGrowth):
            return True

        return self.to_dict() != other.to_dict()
