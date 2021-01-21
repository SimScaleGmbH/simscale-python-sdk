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


class GeneralDarcyForchheimerPacefish(object):
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
        'darcy_forchheimer_type': 'OneOfGeneralDarcyForchheimerPacefishDarcyForchheimerType',
        'permeability': 'DimensionalArea',
        'friction_form_coefficient': 'float',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'darcy_forchheimer_type': 'darcyForchheimerType',
        'permeability': 'permeability',
        'friction_form_coefficient': 'frictionFormCoefficient',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids'
    }

    def __init__(self, type='GENERAL_POROSITY', name=None, darcy_forchheimer_type=None, permeability=None, friction_form_coefficient=None, topological_reference=None, geometry_primitive_uuids=None, local_vars_configuration=None):  # noqa: E501
        """GeneralDarcyForchheimerPacefish - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._darcy_forchheimer_type = None
        self._permeability = None
        self._friction_form_coefficient = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if darcy_forchheimer_type is not None:
            self.darcy_forchheimer_type = darcy_forchheimer_type
        if permeability is not None:
            self.permeability = permeability
        if friction_form_coefficient is not None:
            self.friction_form_coefficient = friction_form_coefficient
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def type(self):
        """Gets the type of this GeneralDarcyForchheimerPacefish.  # noqa: E501


        :return: The type of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GeneralDarcyForchheimerPacefish.


        :param type: The type of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this GeneralDarcyForchheimerPacefish.  # noqa: E501


        :return: The name of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GeneralDarcyForchheimerPacefish.


        :param name: The name of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def darcy_forchheimer_type(self):
        """Gets the darcy_forchheimer_type of this GeneralDarcyForchheimerPacefish.  # noqa: E501


        :return: The darcy_forchheimer_type of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :rtype: OneOfGeneralDarcyForchheimerPacefishDarcyForchheimerType
        """
        return self._darcy_forchheimer_type

    @darcy_forchheimer_type.setter
    def darcy_forchheimer_type(self, darcy_forchheimer_type):
        """Sets the darcy_forchheimer_type of this GeneralDarcyForchheimerPacefish.


        :param darcy_forchheimer_type: The darcy_forchheimer_type of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :type: OneOfGeneralDarcyForchheimerPacefishDarcyForchheimerType
        """

        self._darcy_forchheimer_type = darcy_forchheimer_type

    @property
    def permeability(self):
        """Gets the permeability of this GeneralDarcyForchheimerPacefish.  # noqa: E501


        :return: The permeability of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :rtype: DimensionalArea
        """
        return self._permeability

    @permeability.setter
    def permeability(self, permeability):
        """Sets the permeability of this GeneralDarcyForchheimerPacefish.


        :param permeability: The permeability of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :type: DimensionalArea
        """

        self._permeability = permeability

    @property
    def friction_form_coefficient(self):
        """Gets the friction_form_coefficient of this GeneralDarcyForchheimerPacefish.  # noqa: E501

        Friction form coefficient defines the pressure losses due to inertial effects through the porous object. The greater the friction form coefficient, the greater the pressure losses due to inertial effects  are. Friction form coefficient of zero means that there are no inertial losses through the porous object.  # noqa: E501

        :return: The friction_form_coefficient of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :rtype: float
        """
        return self._friction_form_coefficient

    @friction_form_coefficient.setter
    def friction_form_coefficient(self, friction_form_coefficient):
        """Sets the friction_form_coefficient of this GeneralDarcyForchheimerPacefish.

        Friction form coefficient defines the pressure losses due to inertial effects through the porous object. The greater the friction form coefficient, the greater the pressure losses due to inertial effects  are. Friction form coefficient of zero means that there are no inertial losses through the porous object.  # noqa: E501

        :param friction_form_coefficient: The friction_form_coefficient of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                friction_form_coefficient is not None and friction_form_coefficient < 0):  # noqa: E501
            raise ValueError("Invalid value for `friction_form_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._friction_form_coefficient = friction_form_coefficient

    @property
    def topological_reference(self):
        """Gets the topological_reference of this GeneralDarcyForchheimerPacefish.  # noqa: E501


        :return: The topological_reference of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this GeneralDarcyForchheimerPacefish.


        :param topological_reference: The topological_reference of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this GeneralDarcyForchheimerPacefish.  # noqa: E501


        :return: The geometry_primitive_uuids of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this GeneralDarcyForchheimerPacefish.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this GeneralDarcyForchheimerPacefish.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

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
        if not isinstance(other, GeneralDarcyForchheimerPacefish):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralDarcyForchheimerPacefish):
            return True

        return self.to_dict() != other.to_dict()
