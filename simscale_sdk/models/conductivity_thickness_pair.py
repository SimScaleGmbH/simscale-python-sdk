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


class ConductivityThicknessPair(object):
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
        'thermal_conductivity': 'DimensionalThermalConductivity',
        'electric_resistivity': 'DimensionalElectricResistivity',
        'layer_thickness': 'DimensionalLength'
    }

    attribute_map = {
        'thermal_conductivity': 'thermalConductivity',
        'electric_resistivity': 'electricResistivity',
        'layer_thickness': 'layerThickness'
    }

    def __init__(self, thermal_conductivity=None, electric_resistivity=None, layer_thickness=None, local_vars_configuration=None):  # noqa: E501
        """ConductivityThicknessPair - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._thermal_conductivity = None
        self._electric_resistivity = None
        self._layer_thickness = None
        self.discriminator = None

        if thermal_conductivity is not None:
            self.thermal_conductivity = thermal_conductivity
        if electric_resistivity is not None:
            self.electric_resistivity = electric_resistivity
        if layer_thickness is not None:
            self.layer_thickness = layer_thickness

    @property
    def thermal_conductivity(self):
        """Gets the thermal_conductivity of this ConductivityThicknessPair.  # noqa: E501


        :return: The thermal_conductivity of this ConductivityThicknessPair.  # noqa: E501
        :rtype: DimensionalThermalConductivity
        """
        return self._thermal_conductivity

    @thermal_conductivity.setter
    def thermal_conductivity(self, thermal_conductivity):
        """Sets the thermal_conductivity of this ConductivityThicknessPair.


        :param thermal_conductivity: The thermal_conductivity of this ConductivityThicknessPair.  # noqa: E501
        :type: DimensionalThermalConductivity
        """

        self._thermal_conductivity = thermal_conductivity

    @property
    def electric_resistivity(self):
        """Gets the electric_resistivity of this ConductivityThicknessPair.  # noqa: E501


        :return: The electric_resistivity of this ConductivityThicknessPair.  # noqa: E501
        :rtype: DimensionalElectricResistivity
        """
        return self._electric_resistivity

    @electric_resistivity.setter
    def electric_resistivity(self, electric_resistivity):
        """Sets the electric_resistivity of this ConductivityThicknessPair.


        :param electric_resistivity: The electric_resistivity of this ConductivityThicknessPair.  # noqa: E501
        :type: DimensionalElectricResistivity
        """

        self._electric_resistivity = electric_resistivity

    @property
    def layer_thickness(self):
        """Gets the layer_thickness of this ConductivityThicknessPair.  # noqa: E501


        :return: The layer_thickness of this ConductivityThicknessPair.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._layer_thickness

    @layer_thickness.setter
    def layer_thickness(self, layer_thickness):
        """Sets the layer_thickness of this ConductivityThicknessPair.


        :param layer_thickness: The layer_thickness of this ConductivityThicknessPair.  # noqa: E501
        :type: DimensionalLength
        """

        self._layer_thickness = layer_thickness

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
        if not isinstance(other, ConductivityThicknessPair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConductivityThicknessPair):
            return True

        return self.to_dict() != other.to_dict()