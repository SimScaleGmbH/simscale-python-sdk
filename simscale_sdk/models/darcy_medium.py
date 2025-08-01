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


class DarcyMedium(object):
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
        'porosity': 'float',
        'permeability': 'DimensionalArea',
        'drag_coefficient': 'float',
        'porous_material_type': 'OneOfDarcyMediumPorousMaterialType',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'porosity': 'porosity',
        'permeability': 'permeability',
        'drag_coefficient': 'dragCoefficient',
        'porous_material_type': 'porousMaterialType',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='DARCY', name=None, porosity=None, permeability=None, drag_coefficient=None, porous_material_type=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """DarcyMedium - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._porosity = None
        self._permeability = None
        self._drag_coefficient = None
        self._porous_material_type = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if porosity is not None:
            self.porosity = porosity
        if permeability is not None:
            self.permeability = permeability
        if drag_coefficient is not None:
            self.drag_coefficient = drag_coefficient
        if porous_material_type is not None:
            self.porous_material_type = porous_material_type
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this DarcyMedium.  # noqa: E501

        Schema name: DarcyMedium  # noqa: E501

        :return: The type of this DarcyMedium.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DarcyMedium.

        Schema name: DarcyMedium  # noqa: E501

        :param type: The type of this DarcyMedium.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this DarcyMedium.  # noqa: E501


        :return: The name of this DarcyMedium.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DarcyMedium.


        :param name: The name of this DarcyMedium.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def porosity(self):
        """Gets the porosity of this DarcyMedium.  # noqa: E501

        Porosity is the fraction of a volume of material is that is void. It ranges from φ = 1 (completely empty) to φ = 0 (completely solid).  # noqa: E501

        :return: The porosity of this DarcyMedium.  # noqa: E501
        :rtype: float
        """
        return self._porosity

    @porosity.setter
    def porosity(self, porosity):
        """Sets the porosity of this DarcyMedium.

        Porosity is the fraction of a volume of material is that is void. It ranges from φ = 1 (completely empty) to φ = 0 (completely solid).  # noqa: E501

        :param porosity: The porosity of this DarcyMedium.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                porosity is not None and porosity > 1):  # noqa: E501
            raise ValueError("Invalid value for `porosity`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                porosity is not None and porosity < 0):  # noqa: E501
            raise ValueError("Invalid value for `porosity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._porosity = porosity

    @property
    def permeability(self):
        """Gets the permeability of this DarcyMedium.  # noqa: E501


        :return: The permeability of this DarcyMedium.  # noqa: E501
        :rtype: DimensionalArea
        """
        return self._permeability

    @permeability.setter
    def permeability(self, permeability):
        """Sets the permeability of this DarcyMedium.


        :param permeability: The permeability of this DarcyMedium.  # noqa: E501
        :type: DimensionalArea
        """

        self._permeability = permeability

    @property
    def drag_coefficient(self):
        """Gets the drag_coefficient of this DarcyMedium.  # noqa: E501

        The Darcy law may be extended to include the Forchheimer drag term for more inertial flows (Re > 10). This term is quadratic in flow velocity. Its coefficient includes the fluid drag coefficient Cd.  # noqa: E501

        :return: The drag_coefficient of this DarcyMedium.  # noqa: E501
        :rtype: float
        """
        return self._drag_coefficient

    @drag_coefficient.setter
    def drag_coefficient(self, drag_coefficient):
        """Sets the drag_coefficient of this DarcyMedium.

        The Darcy law may be extended to include the Forchheimer drag term for more inertial flows (Re > 10). This term is quadratic in flow velocity. Its coefficient includes the fluid drag coefficient Cd.  # noqa: E501

        :param drag_coefficient: The drag_coefficient of this DarcyMedium.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                drag_coefficient is not None and drag_coefficient < 0):  # noqa: E501
            raise ValueError("Invalid value for `drag_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._drag_coefficient = drag_coefficient

    @property
    def porous_material_type(self):
        """Gets the porous_material_type of this DarcyMedium.  # noqa: E501


        :return: The porous_material_type of this DarcyMedium.  # noqa: E501
        :rtype: OneOfDarcyMediumPorousMaterialType
        """
        return self._porous_material_type

    @porous_material_type.setter
    def porous_material_type(self, porous_material_type):
        """Sets the porous_material_type of this DarcyMedium.


        :param porous_material_type: The porous_material_type of this DarcyMedium.  # noqa: E501
        :type: OneOfDarcyMediumPorousMaterialType
        """

        self._porous_material_type = porous_material_type

    @property
    def topological_reference(self):
        """Gets the topological_reference of this DarcyMedium.  # noqa: E501


        :return: The topological_reference of this DarcyMedium.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this DarcyMedium.


        :param topological_reference: The topological_reference of this DarcyMedium.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

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
        if not isinstance(other, DarcyMedium):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DarcyMedium):
            return True

        return self.to_dict() != other.to_dict()
