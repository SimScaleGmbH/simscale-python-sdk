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


class OneOfPressureOutletBCNetRadiativeHeatFlux(object):
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
        'emissivity': 'DimensionalDimensionless',
        'radiative_source_value': 'DimensionalHeatFlux'
    }

    attribute_map = {
        'type': 'type',
        'emissivity': 'emissivity',
        'radiative_source_value': 'radiativeSourceValue'
    }

    discriminator_value_class_map = {
        'GREYBODY_DIFFUSIVE': 'GreybodyDiffusiveRSBC',
        'OPEN_WINDOW': 'OpenWindowRSBC'
    }

    def __init__(self, type='OPEN_WINDOW', emissivity=None, radiative_source_value=None, local_vars_configuration=None):  # noqa: E501
        """OneOfPressureOutletBCNetRadiativeHeatFlux - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._emissivity = None
        self._radiative_source_value = None
        self.discriminator = 'type'

        self.type = type
        if emissivity is not None:
            self.emissivity = emissivity
        if radiative_source_value is not None:
            self.radiative_source_value = radiative_source_value

    @property
    def type(self):
        """Gets the type of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501


        :return: The type of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfPressureOutletBCNetRadiativeHeatFlux.


        :param type: The type of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def emissivity(self):
        """Gets the emissivity of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501


        :return: The emissivity of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501
        :rtype: DimensionalDimensionless
        """
        return self._emissivity

    @emissivity.setter
    def emissivity(self, emissivity):
        """Sets the emissivity of this OneOfPressureOutletBCNetRadiativeHeatFlux.


        :param emissivity: The emissivity of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501
        :type: DimensionalDimensionless
        """

        self._emissivity = emissivity

    @property
    def radiative_source_value(self):
        """Gets the radiative_source_value of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501


        :return: The radiative_source_value of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501
        :rtype: DimensionalHeatFlux
        """
        return self._radiative_source_value

    @radiative_source_value.setter
    def radiative_source_value(self, radiative_source_value):
        """Sets the radiative_source_value of this OneOfPressureOutletBCNetRadiativeHeatFlux.


        :param radiative_source_value: The radiative_source_value of this OneOfPressureOutletBCNetRadiativeHeatFlux.  # noqa: E501
        :type: DimensionalHeatFlux
        """

        self._radiative_source_value = radiative_source_value

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
        if not isinstance(other, OneOfPressureOutletBCNetRadiativeHeatFlux):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfPressureOutletBCNetRadiativeHeatFlux):
            return True

        return self.to_dict() != other.to_dict()
