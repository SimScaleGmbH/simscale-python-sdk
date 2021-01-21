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


class OrthotropicConductivity(object):
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
        'thermal_conductivity_x': 'DimensionalFunctionThermalConductivity',
        'thermal_conductivity_y': 'DimensionalFunctionThermalConductivity',
        'thermal_conductivity_z': 'DimensionalFunctionThermalConductivity'
    }

    attribute_map = {
        'type': 'type',
        'thermal_conductivity_x': 'thermalConductivityX',
        'thermal_conductivity_y': 'thermalConductivityY',
        'thermal_conductivity_z': 'thermalConductivityZ'
    }

    def __init__(self, type='ORTHOTROPIC', thermal_conductivity_x=None, thermal_conductivity_y=None, thermal_conductivity_z=None, local_vars_configuration=None):  # noqa: E501
        """OrthotropicConductivity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._thermal_conductivity_x = None
        self._thermal_conductivity_y = None
        self._thermal_conductivity_z = None
        self.discriminator = None

        self.type = type
        if thermal_conductivity_x is not None:
            self.thermal_conductivity_x = thermal_conductivity_x
        if thermal_conductivity_y is not None:
            self.thermal_conductivity_y = thermal_conductivity_y
        if thermal_conductivity_z is not None:
            self.thermal_conductivity_z = thermal_conductivity_z

    @property
    def type(self):
        """Gets the type of this OrthotropicConductivity.  # noqa: E501


        :return: The type of this OrthotropicConductivity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrthotropicConductivity.


        :param type: The type of this OrthotropicConductivity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def thermal_conductivity_x(self):
        """Gets the thermal_conductivity_x of this OrthotropicConductivity.  # noqa: E501


        :return: The thermal_conductivity_x of this OrthotropicConductivity.  # noqa: E501
        :rtype: DimensionalFunctionThermalConductivity
        """
        return self._thermal_conductivity_x

    @thermal_conductivity_x.setter
    def thermal_conductivity_x(self, thermal_conductivity_x):
        """Sets the thermal_conductivity_x of this OrthotropicConductivity.


        :param thermal_conductivity_x: The thermal_conductivity_x of this OrthotropicConductivity.  # noqa: E501
        :type: DimensionalFunctionThermalConductivity
        """

        self._thermal_conductivity_x = thermal_conductivity_x

    @property
    def thermal_conductivity_y(self):
        """Gets the thermal_conductivity_y of this OrthotropicConductivity.  # noqa: E501


        :return: The thermal_conductivity_y of this OrthotropicConductivity.  # noqa: E501
        :rtype: DimensionalFunctionThermalConductivity
        """
        return self._thermal_conductivity_y

    @thermal_conductivity_y.setter
    def thermal_conductivity_y(self, thermal_conductivity_y):
        """Sets the thermal_conductivity_y of this OrthotropicConductivity.


        :param thermal_conductivity_y: The thermal_conductivity_y of this OrthotropicConductivity.  # noqa: E501
        :type: DimensionalFunctionThermalConductivity
        """

        self._thermal_conductivity_y = thermal_conductivity_y

    @property
    def thermal_conductivity_z(self):
        """Gets the thermal_conductivity_z of this OrthotropicConductivity.  # noqa: E501


        :return: The thermal_conductivity_z of this OrthotropicConductivity.  # noqa: E501
        :rtype: DimensionalFunctionThermalConductivity
        """
        return self._thermal_conductivity_z

    @thermal_conductivity_z.setter
    def thermal_conductivity_z(self, thermal_conductivity_z):
        """Sets the thermal_conductivity_z of this OrthotropicConductivity.


        :param thermal_conductivity_z: The thermal_conductivity_z of this OrthotropicConductivity.  # noqa: E501
        :type: DimensionalFunctionThermalConductivity
        """

        self._thermal_conductivity_z = thermal_conductivity_z

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
        if not isinstance(other, OrthotropicConductivity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrthotropicConductivity):
            return True

        return self.to_dict() != other.to_dict()
