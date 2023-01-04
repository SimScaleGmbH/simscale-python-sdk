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


class OneOfSolidCompressibleMaterialElectricConductivityType(object):
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
        'electric_resistivity': 'DimensionalFunctionElectricResistivity',
        'electric_resistivity_x': 'DimensionalFunctionElectricResistivity',
        'electric_resistivity_y': 'DimensionalFunctionElectricResistivity',
        'electric_resistivity_z': 'DimensionalFunctionElectricResistivity'
    }

    attribute_map = {
        'type': 'type',
        'electric_resistivity': 'electricResistivity',
        'electric_resistivity_x': 'electricResistivityX',
        'electric_resistivity_y': 'electricResistivityY',
        'electric_resistivity_z': 'electricResistivityZ'
    }

    discriminator_value_class_map = {
        'DIELECTRIC': 'Dielectric',
        'ISOTROPIC_ELECTRIC_CONDUCTIVITY': 'IsotropicElectricConductivity',
        'ORTHOTROPIC_ELECTRIC_CONDUCTIVITY': 'OrthotropicElectricConductivity'
    }

    def __init__(self, type='ORTHOTROPIC_ELECTRIC_CONDUCTIVITY', electric_resistivity=None, electric_resistivity_x=None, electric_resistivity_y=None, electric_resistivity_z=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSolidCompressibleMaterialElectricConductivityType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._electric_resistivity = None
        self._electric_resistivity_x = None
        self._electric_resistivity_y = None
        self._electric_resistivity_z = None
        self.discriminator = 'type'

        self.type = type
        if electric_resistivity is not None:
            self.electric_resistivity = electric_resistivity
        if electric_resistivity_x is not None:
            self.electric_resistivity_x = electric_resistivity_x
        if electric_resistivity_y is not None:
            self.electric_resistivity_y = electric_resistivity_y
        if electric_resistivity_z is not None:
            self.electric_resistivity_z = electric_resistivity_z

    @property
    def type(self):
        """Gets the type of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501

        <p>Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent.</p>  Schema name: OrthotropicElectricConductivity  # noqa: E501

        :return: The type of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSolidCompressibleMaterialElectricConductivityType.

        <p>Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent.</p>  Schema name: OrthotropicElectricConductivity  # noqa: E501

        :param type: The type of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def electric_resistivity(self):
        """Gets the electric_resistivity of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501


        :return: The electric_resistivity of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :rtype: DimensionalFunctionElectricResistivity
        """
        return self._electric_resistivity

    @electric_resistivity.setter
    def electric_resistivity(self, electric_resistivity):
        """Sets the electric_resistivity of this OneOfSolidCompressibleMaterialElectricConductivityType.


        :param electric_resistivity: The electric_resistivity of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :type: DimensionalFunctionElectricResistivity
        """

        self._electric_resistivity = electric_resistivity

    @property
    def electric_resistivity_x(self):
        """Gets the electric_resistivity_x of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501


        :return: The electric_resistivity_x of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :rtype: DimensionalFunctionElectricResistivity
        """
        return self._electric_resistivity_x

    @electric_resistivity_x.setter
    def electric_resistivity_x(self, electric_resistivity_x):
        """Sets the electric_resistivity_x of this OneOfSolidCompressibleMaterialElectricConductivityType.


        :param electric_resistivity_x: The electric_resistivity_x of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :type: DimensionalFunctionElectricResistivity
        """

        self._electric_resistivity_x = electric_resistivity_x

    @property
    def electric_resistivity_y(self):
        """Gets the electric_resistivity_y of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501


        :return: The electric_resistivity_y of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :rtype: DimensionalFunctionElectricResistivity
        """
        return self._electric_resistivity_y

    @electric_resistivity_y.setter
    def electric_resistivity_y(self, electric_resistivity_y):
        """Sets the electric_resistivity_y of this OneOfSolidCompressibleMaterialElectricConductivityType.


        :param electric_resistivity_y: The electric_resistivity_y of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :type: DimensionalFunctionElectricResistivity
        """

        self._electric_resistivity_y = electric_resistivity_y

    @property
    def electric_resistivity_z(self):
        """Gets the electric_resistivity_z of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501


        :return: The electric_resistivity_z of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :rtype: DimensionalFunctionElectricResistivity
        """
        return self._electric_resistivity_z

    @electric_resistivity_z.setter
    def electric_resistivity_z(self, electric_resistivity_z):
        """Sets the electric_resistivity_z of this OneOfSolidCompressibleMaterialElectricConductivityType.


        :param electric_resistivity_z: The electric_resistivity_z of this OneOfSolidCompressibleMaterialElectricConductivityType.  # noqa: E501
        :type: DimensionalFunctionElectricResistivity
        """

        self._electric_resistivity_z = electric_resistivity_z

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
        if not isinstance(other, OneOfSolidCompressibleMaterialElectricConductivityType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSolidCompressibleMaterialElectricConductivityType):
            return True

        return self.to_dict() != other.to_dict()
