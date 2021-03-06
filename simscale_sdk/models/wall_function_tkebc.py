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


class WallFunctionTKEBC(object):
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
        'wall_roughness': 'bool',
        'roughness_height': 'DimensionalLength',
        'roughness_constant': 'float'
    }

    attribute_map = {
        'type': 'type',
        'wall_roughness': 'wallRoughness',
        'roughness_height': 'roughnessHeight',
        'roughness_constant': 'roughnessConstant'
    }

    def __init__(self, type='WALL_FUNCTION', wall_roughness=None, roughness_height=None, roughness_constant=None, local_vars_configuration=None):  # noqa: E501
        """WallFunctionTKEBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._wall_roughness = None
        self._roughness_height = None
        self._roughness_constant = None
        self.discriminator = None

        self.type = type
        if wall_roughness is not None:
            self.wall_roughness = wall_roughness
        if roughness_height is not None:
            self.roughness_height = roughness_height
        if roughness_constant is not None:
            self.roughness_constant = roughness_constant

    @property
    def type(self):
        """Gets the type of this WallFunctionTKEBC.  # noqa: E501

        Schema name: WallFunctionTKEBC  # noqa: E501

        :return: The type of this WallFunctionTKEBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WallFunctionTKEBC.

        Schema name: WallFunctionTKEBC  # noqa: E501

        :param type: The type of this WallFunctionTKEBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def wall_roughness(self):
        """Gets the wall_roughness of this WallFunctionTKEBC.  # noqa: E501


        :return: The wall_roughness of this WallFunctionTKEBC.  # noqa: E501
        :rtype: bool
        """
        return self._wall_roughness

    @wall_roughness.setter
    def wall_roughness(self, wall_roughness):
        """Sets the wall_roughness of this WallFunctionTKEBC.


        :param wall_roughness: The wall_roughness of this WallFunctionTKEBC.  # noqa: E501
        :type: bool
        """

        self._wall_roughness = wall_roughness

    @property
    def roughness_height(self):
        """Gets the roughness_height of this WallFunctionTKEBC.  # noqa: E501


        :return: The roughness_height of this WallFunctionTKEBC.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._roughness_height

    @roughness_height.setter
    def roughness_height(self, roughness_height):
        """Sets the roughness_height of this WallFunctionTKEBC.


        :param roughness_height: The roughness_height of this WallFunctionTKEBC.  # noqa: E501
        :type: DimensionalLength
        """

        self._roughness_height = roughness_height

    @property
    def roughness_constant(self):
        """Gets the roughness_constant of this WallFunctionTKEBC.  # noqa: E501


        :return: The roughness_constant of this WallFunctionTKEBC.  # noqa: E501
        :rtype: float
        """
        return self._roughness_constant

    @roughness_constant.setter
    def roughness_constant(self, roughness_constant):
        """Sets the roughness_constant of this WallFunctionTKEBC.


        :param roughness_constant: The roughness_constant of this WallFunctionTKEBC.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                roughness_constant is not None and roughness_constant < 0.5):  # noqa: E501
            raise ValueError("Invalid value for `roughness_constant`, must be a value greater than or equal to `0.5`")  # noqa: E501

        self._roughness_constant = roughness_constant

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
        if not isinstance(other, WallFunctionTKEBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WallFunctionTKEBC):
            return True

        return self.to_dict() != other.to_dict()
