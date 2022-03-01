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


class MovingWallVBC(object):
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
        'value': 'DimensionalVectorSpeed',
        'turbulence_wall': 'str',
        'orientation_reference': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'turbulence_wall': 'turbulenceWall',
        'orientation_reference': 'orientationReference'
    }

    def __init__(self, type='MOVING_WALL_VELOCITY', value=None, turbulence_wall=None, orientation_reference=None, local_vars_configuration=None):  # noqa: E501
        """MovingWallVBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._value = None
        self._turbulence_wall = None
        self._orientation_reference = None
        self.discriminator = None

        self.type = type
        if value is not None:
            self.value = value
        if turbulence_wall is not None:
            self.turbulence_wall = turbulence_wall
        if orientation_reference is not None:
            self.orientation_reference = orientation_reference

    @property
    def type(self):
        """Gets the type of this MovingWallVBC.  # noqa: E501

        Schema name: MovingWallVBC  # noqa: E501

        :return: The type of this MovingWallVBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MovingWallVBC.

        Schema name: MovingWallVBC  # noqa: E501

        :param type: The type of this MovingWallVBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this MovingWallVBC.  # noqa: E501


        :return: The value of this MovingWallVBC.  # noqa: E501
        :rtype: DimensionalVectorSpeed
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MovingWallVBC.


        :param value: The value of this MovingWallVBC.  # noqa: E501
        :type: DimensionalVectorSpeed
        """

        self._value = value

    @property
    def turbulence_wall(self):
        """Gets the turbulence_wall of this MovingWallVBC.  # noqa: E501


        :return: The turbulence_wall of this MovingWallVBC.  # noqa: E501
        :rtype: str
        """
        return self._turbulence_wall

    @turbulence_wall.setter
    def turbulence_wall(self, turbulence_wall):
        """Sets the turbulence_wall of this MovingWallVBC.


        :param turbulence_wall: The turbulence_wall of this MovingWallVBC.  # noqa: E501
        :type: str
        """
        allowed_values = ["WALL_FUNCTION", "FULL_RESOLUTION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and turbulence_wall not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `turbulence_wall` ({0}), must be one of {1}"  # noqa: E501
                .format(turbulence_wall, allowed_values)
            )

        self._turbulence_wall = turbulence_wall

    @property
    def orientation_reference(self):
        """Gets the orientation_reference of this MovingWallVBC.  # noqa: E501


        :return: The orientation_reference of this MovingWallVBC.  # noqa: E501
        :rtype: str
        """
        return self._orientation_reference

    @orientation_reference.setter
    def orientation_reference(self, orientation_reference):
        """Sets the orientation_reference of this MovingWallVBC.


        :param orientation_reference: The orientation_reference of this MovingWallVBC.  # noqa: E501
        :type: str
        """
        allowed_values = ["GEOMETRY", "FLOW_DOMAIN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and orientation_reference not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `orientation_reference` ({0}), must be one of {1}"  # noqa: E501
                .format(orientation_reference, allowed_values)
            )

        self._orientation_reference = orientation_reference

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
        if not isinstance(other, MovingWallVBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MovingWallVBC):
            return True

        return self.to_dict() != other.to_dict()