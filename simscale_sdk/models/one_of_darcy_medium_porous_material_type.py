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


class OneOfDarcyMediumPorousMaterialType(object):
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
        'mode': 'OneOfDirectionalMaterialStructureMode',
        'direction': 'DimensionalVectorDimensionless',
        'orientation': 'OneOfDirectionalMaterialStructureOrientation'
    }

    attribute_map = {
        'type': 'type',
        'mode': 'mode',
        'direction': 'direction',
        'orientation': 'orientation'
    }

    discriminator_value_class_map = {
        'HOMOGENEOUS': 'HomogeneousMaterialStructure',
        'DIRECTIONAL': 'DirectionalMaterialStructure'
    }

    def __init__(self, type='DIRECTIONAL', mode=None, direction=None, orientation=None, local_vars_configuration=None):  # noqa: E501
        """OneOfDarcyMediumPorousMaterialType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._mode = None
        self._direction = None
        self._orientation = None
        self.discriminator = 'type'

        self.type = type
        if mode is not None:
            self.mode = mode
        if direction is not None:
            self.direction = direction
        if orientation is not None:
            self.orientation = orientation

    @property
    def type(self):
        """Gets the type of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501

        Schema name: DirectionalMaterialStructure  # noqa: E501

        :return: The type of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfDarcyMediumPorousMaterialType.

        Schema name: DirectionalMaterialStructure  # noqa: E501

        :param type: The type of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def mode(self):
        """Gets the mode of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501


        :return: The mode of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501
        :rtype: OneOfDirectionalMaterialStructureMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this OneOfDarcyMediumPorousMaterialType.


        :param mode: The mode of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501
        :type: OneOfDirectionalMaterialStructureMode
        """

        self._mode = mode

    @property
    def direction(self):
        """Gets the direction of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501


        :return: The direction of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501
        :rtype: DimensionalVectorDimensionless
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this OneOfDarcyMediumPorousMaterialType.


        :param direction: The direction of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501
        :type: DimensionalVectorDimensionless
        """

        self._direction = direction

    @property
    def orientation(self):
        """Gets the orientation of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501


        :return: The orientation of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501
        :rtype: OneOfDirectionalMaterialStructureOrientation
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this OneOfDarcyMediumPorousMaterialType.


        :param orientation: The orientation of this OneOfDarcyMediumPorousMaterialType.  # noqa: E501
        :type: OneOfDirectionalMaterialStructureOrientation
        """

        self._orientation = orientation

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
        if not isinstance(other, OneOfDarcyMediumPorousMaterialType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfDarcyMediumPorousMaterialType):
            return True

        return self.to_dict() != other.to_dict()
