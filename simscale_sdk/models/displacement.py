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


class Displacement(object):
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
        'field': 'VectorField',
        'scale_factor': 'float'
    }

    attribute_map = {
        'field': 'field',
        'scale_factor': 'scaleFactor'
    }

    def __init__(self, field=None, scale_factor=1.0, local_vars_configuration=None):  # noqa: E501
        """Displacement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._scale_factor = None
        self.discriminator = None

        self.field = field
        self.scale_factor = scale_factor

    @property
    def field(self):
        """Gets the field of this Displacement.  # noqa: E501


        :return: The field of this Displacement.  # noqa: E501
        :rtype: VectorField
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Displacement.


        :param field: The field of this Displacement.  # noqa: E501
        :type: VectorField
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def scale_factor(self):
        """Gets the scale_factor of this Displacement.  # noqa: E501


        :return: The scale_factor of this Displacement.  # noqa: E501
        :rtype: float
        """
        return self._scale_factor

    @scale_factor.setter
    def scale_factor(self, scale_factor):
        """Sets the scale_factor of this Displacement.


        :param scale_factor: The scale_factor of this Displacement.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and scale_factor is None:  # noqa: E501
            raise ValueError("Invalid value for `scale_factor`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scale_factor is not None and scale_factor < 0.01):  # noqa: E501
            raise ValueError("Invalid value for `scale_factor`, must be a value greater than or equal to `0.01`")  # noqa: E501

        self._scale_factor = scale_factor

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
        if not isinstance(other, Displacement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Displacement):
            return True

        return self.to_dict() != other.to_dict()
