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


class VectorRotation(object):
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
        'rotation_center': 'DimensionalVectorLength',
        'angular_velocity': 'DimensionalVectorRotationSpeed'
    }

    attribute_map = {
        'type': 'type',
        'rotation_center': 'rotationCenter',
        'angular_velocity': 'angularVelocity'
    }

    def __init__(self, type='VECTOR_ROTATION', rotation_center=None, angular_velocity=None, local_vars_configuration=None):  # noqa: E501
        """VectorRotation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._rotation_center = None
        self._angular_velocity = None
        self.discriminator = None

        self.type = type
        if rotation_center is not None:
            self.rotation_center = rotation_center
        if angular_velocity is not None:
            self.angular_velocity = angular_velocity

    @property
    def type(self):
        """Gets the type of this VectorRotation.  # noqa: E501

        Schema name: VectorRotation  # noqa: E501

        :return: The type of this VectorRotation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VectorRotation.

        Schema name: VectorRotation  # noqa: E501

        :param type: The type of this VectorRotation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def rotation_center(self):
        """Gets the rotation_center of this VectorRotation.  # noqa: E501


        :return: The rotation_center of this VectorRotation.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._rotation_center

    @rotation_center.setter
    def rotation_center(self, rotation_center):
        """Sets the rotation_center of this VectorRotation.


        :param rotation_center: The rotation_center of this VectorRotation.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._rotation_center = rotation_center

    @property
    def angular_velocity(self):
        """Gets the angular_velocity of this VectorRotation.  # noqa: E501


        :return: The angular_velocity of this VectorRotation.  # noqa: E501
        :rtype: DimensionalVectorRotationSpeed
        """
        return self._angular_velocity

    @angular_velocity.setter
    def angular_velocity(self, angular_velocity):
        """Sets the angular_velocity of this VectorRotation.


        :param angular_velocity: The angular_velocity of this VectorRotation.  # noqa: E501
        :type: DimensionalVectorRotationSpeed
        """

        self._angular_velocity = angular_velocity

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
        if not isinstance(other, VectorRotation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VectorRotation):
            return True

        return self.to_dict() != other.to_dict()
