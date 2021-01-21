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


class OneOfAdvancedConceptsRotatingZones(object):
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
        'motion_type': 'OneOfAMIRotatingZoneMotionType',
        'topological_reference': 'TopologicalReference',
        'origin': 'DimensionalVectorLength',
        'axis': 'DimensionalVectorLength',
        'angular_velocity': 'DimensionalFunctionRotationSpeed'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'motion_type': 'motionType',
        'topological_reference': 'topologicalReference',
        'origin': 'origin',
        'axis': 'axis',
        'angular_velocity': 'angularVelocity'
    }

    discriminator_value_class_map = {
        'ARBITRARY_MESH_INTERFACE': 'AMIRotatingZone',
        'MULTI_REFERENCE_FRAME': 'MRFRotatingZone'
    }

    def __init__(self, type='MULTI_REFERENCE_FRAME', name=None, motion_type=None, topological_reference=None, origin=None, axis=None, angular_velocity=None, local_vars_configuration=None):  # noqa: E501
        """OneOfAdvancedConceptsRotatingZones - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._motion_type = None
        self._topological_reference = None
        self._origin = None
        self._axis = None
        self._angular_velocity = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if motion_type is not None:
            self.motion_type = motion_type
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if origin is not None:
            self.origin = origin
        if axis is not None:
            self.axis = axis
        if angular_velocity is not None:
            self.angular_velocity = angular_velocity

    @property
    def type(self):
        """Gets the type of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501


        :return: The type of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfAdvancedConceptsRotatingZones.


        :param type: The type of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501


        :return: The name of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfAdvancedConceptsRotatingZones.


        :param name: The name of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def motion_type(self):
        """Gets the motion_type of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501


        :return: The motion_type of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :rtype: OneOfAMIRotatingZoneMotionType
        """
        return self._motion_type

    @motion_type.setter
    def motion_type(self, motion_type):
        """Sets the motion_type of this OneOfAdvancedConceptsRotatingZones.


        :param motion_type: The motion_type of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :type: OneOfAMIRotatingZoneMotionType
        """

        self._motion_type = motion_type

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501


        :return: The topological_reference of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfAdvancedConceptsRotatingZones.


        :param topological_reference: The topological_reference of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def origin(self):
        """Gets the origin of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501


        :return: The origin of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this OneOfAdvancedConceptsRotatingZones.


        :param origin: The origin of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._origin = origin

    @property
    def axis(self):
        """Gets the axis of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501


        :return: The axis of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._axis

    @axis.setter
    def axis(self, axis):
        """Sets the axis of this OneOfAdvancedConceptsRotatingZones.


        :param axis: The axis of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._axis = axis

    @property
    def angular_velocity(self):
        """Gets the angular_velocity of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501


        :return: The angular_velocity of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :rtype: DimensionalFunctionRotationSpeed
        """
        return self._angular_velocity

    @angular_velocity.setter
    def angular_velocity(self, angular_velocity):
        """Sets the angular_velocity of this OneOfAdvancedConceptsRotatingZones.


        :param angular_velocity: The angular_velocity of this OneOfAdvancedConceptsRotatingZones.  # noqa: E501
        :type: DimensionalFunctionRotationSpeed
        """

        self._angular_velocity = angular_velocity

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
        if not isinstance(other, OneOfAdvancedConceptsRotatingZones):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfAdvancedConceptsRotatingZones):
            return True

        return self.to_dict() != other.to_dict()
