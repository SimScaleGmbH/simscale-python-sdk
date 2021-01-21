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


class CircularHoleShape(object):
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
        'average_hole_diameter': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'average_hole_diameter': 'averageHoleDiameter'
    }

    def __init__(self, type='CIRCULAR', average_hole_diameter=None, local_vars_configuration=None):  # noqa: E501
        """CircularHoleShape - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._average_hole_diameter = None
        self.discriminator = None

        self.type = type
        if average_hole_diameter is not None:
            self.average_hole_diameter = average_hole_diameter

    @property
    def type(self):
        """Gets the type of this CircularHoleShape.  # noqa: E501


        :return: The type of this CircularHoleShape.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CircularHoleShape.


        :param type: The type of this CircularHoleShape.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def average_hole_diameter(self):
        """Gets the average_hole_diameter of this CircularHoleShape.  # noqa: E501


        :return: The average_hole_diameter of this CircularHoleShape.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._average_hole_diameter

    @average_hole_diameter.setter
    def average_hole_diameter(self, average_hole_diameter):
        """Sets the average_hole_diameter of this CircularHoleShape.


        :param average_hole_diameter: The average_hole_diameter of this CircularHoleShape.  # noqa: E501
        :type: DimensionalLength
        """

        self._average_hole_diameter = average_hole_diameter

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
        if not isinstance(other, CircularHoleShape):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CircularHoleShape):
            return True

        return self.to_dict() != other.to_dict()
