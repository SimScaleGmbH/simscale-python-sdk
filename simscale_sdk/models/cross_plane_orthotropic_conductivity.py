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


class CrossPlaneOrthotropicConductivity(object):
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
        'in_plane_conductivity': 'DimensionalFunctionThermalConductivity',
        'cross_plane_conductivity': 'DimensionalFunctionThermalConductivity'
    }

    attribute_map = {
        'type': 'type',
        'in_plane_conductivity': 'inPlaneConductivity',
        'cross_plane_conductivity': 'crossPlaneConductivity'
    }

    def __init__(self, type='CROSS_PLANE_ORTHOTROPIC', in_plane_conductivity=None, cross_plane_conductivity=None, local_vars_configuration=None):  # noqa: E501
        """CrossPlaneOrthotropicConductivity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._in_plane_conductivity = None
        self._cross_plane_conductivity = None
        self.discriminator = None

        self.type = type
        if in_plane_conductivity is not None:
            self.in_plane_conductivity = in_plane_conductivity
        if cross_plane_conductivity is not None:
            self.cross_plane_conductivity = cross_plane_conductivity

    @property
    def type(self):
        """Gets the type of this CrossPlaneOrthotropicConductivity.  # noqa: E501


        :return: The type of this CrossPlaneOrthotropicConductivity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CrossPlaneOrthotropicConductivity.


        :param type: The type of this CrossPlaneOrthotropicConductivity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def in_plane_conductivity(self):
        """Gets the in_plane_conductivity of this CrossPlaneOrthotropicConductivity.  # noqa: E501


        :return: The in_plane_conductivity of this CrossPlaneOrthotropicConductivity.  # noqa: E501
        :rtype: DimensionalFunctionThermalConductivity
        """
        return self._in_plane_conductivity

    @in_plane_conductivity.setter
    def in_plane_conductivity(self, in_plane_conductivity):
        """Sets the in_plane_conductivity of this CrossPlaneOrthotropicConductivity.


        :param in_plane_conductivity: The in_plane_conductivity of this CrossPlaneOrthotropicConductivity.  # noqa: E501
        :type: DimensionalFunctionThermalConductivity
        """

        self._in_plane_conductivity = in_plane_conductivity

    @property
    def cross_plane_conductivity(self):
        """Gets the cross_plane_conductivity of this CrossPlaneOrthotropicConductivity.  # noqa: E501


        :return: The cross_plane_conductivity of this CrossPlaneOrthotropicConductivity.  # noqa: E501
        :rtype: DimensionalFunctionThermalConductivity
        """
        return self._cross_plane_conductivity

    @cross_plane_conductivity.setter
    def cross_plane_conductivity(self, cross_plane_conductivity):
        """Sets the cross_plane_conductivity of this CrossPlaneOrthotropicConductivity.


        :param cross_plane_conductivity: The cross_plane_conductivity of this CrossPlaneOrthotropicConductivity.  # noqa: E501
        :type: DimensionalFunctionThermalConductivity
        """

        self._cross_plane_conductivity = cross_plane_conductivity

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
        if not isinstance(other, CrossPlaneOrthotropicConductivity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossPlaneOrthotropicConductivity):
            return True

        return self.to_dict() != other.to_dict()
