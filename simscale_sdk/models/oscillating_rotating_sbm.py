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


class OscillatingRotatingSBM(object):
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
        'name': 'str',
        'rotation_center': 'DimensionalVectorLength',
        'amplitude': 'DimensionalVectorAngle',
        'angular_velocity': 'DimensionalRotationSpeed'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'rotation_center': 'rotationCenter',
        'amplitude': 'amplitude',
        'angular_velocity': 'angularVelocity'
    }

    def __init__(self, type='OSCILLATING_ROTATING_MOTION', name=None, rotation_center=None, amplitude=None, angular_velocity=None, local_vars_configuration=None):  # noqa: E501
        """OscillatingRotatingSBM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._rotation_center = None
        self._amplitude = None
        self._angular_velocity = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if rotation_center is not None:
            self.rotation_center = rotation_center
        if amplitude is not None:
            self.amplitude = amplitude
        if angular_velocity is not None:
            self.angular_velocity = angular_velocity

    @property
    def type(self):
        """Gets the type of this OscillatingRotatingSBM.  # noqa: E501


        :return: The type of this OscillatingRotatingSBM.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OscillatingRotatingSBM.


        :param type: The type of this OscillatingRotatingSBM.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OscillatingRotatingSBM.  # noqa: E501


        :return: The name of this OscillatingRotatingSBM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OscillatingRotatingSBM.


        :param name: The name of this OscillatingRotatingSBM.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rotation_center(self):
        """Gets the rotation_center of this OscillatingRotatingSBM.  # noqa: E501


        :return: The rotation_center of this OscillatingRotatingSBM.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._rotation_center

    @rotation_center.setter
    def rotation_center(self, rotation_center):
        """Sets the rotation_center of this OscillatingRotatingSBM.


        :param rotation_center: The rotation_center of this OscillatingRotatingSBM.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._rotation_center = rotation_center

    @property
    def amplitude(self):
        """Gets the amplitude of this OscillatingRotatingSBM.  # noqa: E501


        :return: The amplitude of this OscillatingRotatingSBM.  # noqa: E501
        :rtype: DimensionalVectorAngle
        """
        return self._amplitude

    @amplitude.setter
    def amplitude(self, amplitude):
        """Sets the amplitude of this OscillatingRotatingSBM.


        :param amplitude: The amplitude of this OscillatingRotatingSBM.  # noqa: E501
        :type: DimensionalVectorAngle
        """

        self._amplitude = amplitude

    @property
    def angular_velocity(self):
        """Gets the angular_velocity of this OscillatingRotatingSBM.  # noqa: E501


        :return: The angular_velocity of this OscillatingRotatingSBM.  # noqa: E501
        :rtype: DimensionalRotationSpeed
        """
        return self._angular_velocity

    @angular_velocity.setter
    def angular_velocity(self, angular_velocity):
        """Sets the angular_velocity of this OscillatingRotatingSBM.


        :param angular_velocity: The angular_velocity of this OscillatingRotatingSBM.  # noqa: E501
        :type: DimensionalRotationSpeed
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
        if not isinstance(other, OscillatingRotatingSBM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OscillatingRotatingSBM):
            return True

        return self.to_dict() != other.to_dict()
