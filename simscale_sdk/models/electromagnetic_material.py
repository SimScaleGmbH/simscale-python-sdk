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


class ElectromagneticMaterial(object):
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
        'name': 'str',
        'electric_conductivity': 'DimensionalElectricConductivity',
        'relative_magnetic_permeability': 'float',
        'topological_reference': 'TopologicalReference',
        'built_in_material': 'str',
        'material_library_reference': 'MaterialLibraryReference'
    }

    attribute_map = {
        'name': 'name',
        'electric_conductivity': 'electricConductivity',
        'relative_magnetic_permeability': 'relativeMagneticPermeability',
        'topological_reference': 'topologicalReference',
        'built_in_material': 'builtInMaterial',
        'material_library_reference': 'materialLibraryReference'
    }

    def __init__(self, name=None, electric_conductivity=None, relative_magnetic_permeability=None, topological_reference=None, built_in_material=None, material_library_reference=None, local_vars_configuration=None):  # noqa: E501
        """ElectromagneticMaterial - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._electric_conductivity = None
        self._relative_magnetic_permeability = None
        self._topological_reference = None
        self._built_in_material = None
        self._material_library_reference = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if electric_conductivity is not None:
            self.electric_conductivity = electric_conductivity
        if relative_magnetic_permeability is not None:
            self.relative_magnetic_permeability = relative_magnetic_permeability
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if built_in_material is not None:
            self.built_in_material = built_in_material
        if material_library_reference is not None:
            self.material_library_reference = material_library_reference

    @property
    def name(self):
        """Gets the name of this ElectromagneticMaterial.  # noqa: E501


        :return: The name of this ElectromagneticMaterial.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ElectromagneticMaterial.


        :param name: The name of this ElectromagneticMaterial.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def electric_conductivity(self):
        """Gets the electric_conductivity of this ElectromagneticMaterial.  # noqa: E501


        :return: The electric_conductivity of this ElectromagneticMaterial.  # noqa: E501
        :rtype: DimensionalElectricConductivity
        """
        return self._electric_conductivity

    @electric_conductivity.setter
    def electric_conductivity(self, electric_conductivity):
        """Sets the electric_conductivity of this ElectromagneticMaterial.


        :param electric_conductivity: The electric_conductivity of this ElectromagneticMaterial.  # noqa: E501
        :type: DimensionalElectricConductivity
        """

        self._electric_conductivity = electric_conductivity

    @property
    def relative_magnetic_permeability(self):
        """Gets the relative_magnetic_permeability of this ElectromagneticMaterial.  # noqa: E501


        :return: The relative_magnetic_permeability of this ElectromagneticMaterial.  # noqa: E501
        :rtype: float
        """
        return self._relative_magnetic_permeability

    @relative_magnetic_permeability.setter
    def relative_magnetic_permeability(self, relative_magnetic_permeability):
        """Sets the relative_magnetic_permeability of this ElectromagneticMaterial.


        :param relative_magnetic_permeability: The relative_magnetic_permeability of this ElectromagneticMaterial.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                relative_magnetic_permeability is not None and relative_magnetic_permeability < 0):  # noqa: E501
            raise ValueError("Invalid value for `relative_magnetic_permeability`, must be a value greater than or equal to `0`")  # noqa: E501

        self._relative_magnetic_permeability = relative_magnetic_permeability

    @property
    def topological_reference(self):
        """Gets the topological_reference of this ElectromagneticMaterial.  # noqa: E501


        :return: The topological_reference of this ElectromagneticMaterial.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this ElectromagneticMaterial.


        :param topological_reference: The topological_reference of this ElectromagneticMaterial.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def built_in_material(self):
        """Gets the built_in_material of this ElectromagneticMaterial.  # noqa: E501


        :return: The built_in_material of this ElectromagneticMaterial.  # noqa: E501
        :rtype: str
        """
        return self._built_in_material

    @built_in_material.setter
    def built_in_material(self, built_in_material):
        """Sets the built_in_material of this ElectromagneticMaterial.


        :param built_in_material: The built_in_material of this ElectromagneticMaterial.  # noqa: E501
        :type: str
        """

        self._built_in_material = built_in_material

    @property
    def material_library_reference(self):
        """Gets the material_library_reference of this ElectromagneticMaterial.  # noqa: E501


        :return: The material_library_reference of this ElectromagneticMaterial.  # noqa: E501
        :rtype: MaterialLibraryReference
        """
        return self._material_library_reference

    @material_library_reference.setter
    def material_library_reference(self, material_library_reference):
        """Sets the material_library_reference of this ElectromagneticMaterial.


        :param material_library_reference: The material_library_reference of this ElectromagneticMaterial.  # noqa: E501
        :type: MaterialLibraryReference
        """

        self._material_library_reference = material_library_reference

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
        if not isinstance(other, ElectromagneticMaterial):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectromagneticMaterial):
            return True

        return self.to_dict() != other.to_dict()
