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


class OneOfTurbulentHeatFluxTBCHeatSource(object):
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
        'heat_flux': 'DimensionalHeatFlux',
        'power': 'DimensionalPower'
    }

    attribute_map = {
        'type': 'type',
        'heat_flux': 'heatFlux',
        'power': 'power'
    }

    discriminator_value_class_map = {
        'FLUX': 'FluxHeatSource',
        'POWER': 'PowerHeatSource'
    }

    def __init__(self, type='POWER', heat_flux=None, power=None, local_vars_configuration=None):  # noqa: E501
        """OneOfTurbulentHeatFluxTBCHeatSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._heat_flux = None
        self._power = None
        self.discriminator = 'type'

        self.type = type
        if heat_flux is not None:
            self.heat_flux = heat_flux
        if power is not None:
            self.power = power

    @property
    def type(self):
        """Gets the type of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501


        :return: The type of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfTurbulentHeatFluxTBCHeatSource.


        :param type: The type of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def heat_flux(self):
        """Gets the heat_flux of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501


        :return: The heat_flux of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501
        :rtype: DimensionalHeatFlux
        """
        return self._heat_flux

    @heat_flux.setter
    def heat_flux(self, heat_flux):
        """Sets the heat_flux of this OneOfTurbulentHeatFluxTBCHeatSource.


        :param heat_flux: The heat_flux of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501
        :type: DimensionalHeatFlux
        """

        self._heat_flux = heat_flux

    @property
    def power(self):
        """Gets the power of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501


        :return: The power of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501
        :rtype: DimensionalPower
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this OneOfTurbulentHeatFluxTBCHeatSource.


        :param power: The power of this OneOfTurbulentHeatFluxTBCHeatSource.  # noqa: E501
        :type: DimensionalPower
        """

        self._power = power

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
        if not isinstance(other, OneOfTurbulentHeatFluxTBCHeatSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfTurbulentHeatFluxTBCHeatSource):
            return True

        return self.to_dict() != other.to_dict()
