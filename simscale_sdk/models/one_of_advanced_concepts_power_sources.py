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


class OneOfAdvancedConceptsPowerSources(object):
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
        'heat_flux': 'DimensionalFunctionVolumetricPower',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]',
        'heat_exchanger_mode': 'OneOfHeatExchangerSourceHeatExchangerMode'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'heat_flux': 'heatFlux',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids',
        'heat_exchanger_mode': 'heatExchangerMode'
    }

    discriminator_value_class_map = {
        'ABSOLUTE_V23': 'AbsolutePowerSource',
        'SPECIFIC_V23': 'SpecificPowerSource',
        'HEAT_EXCHANGER_SOURCE': 'HeatExchangerSource',
        'TR_ABSOLUTE_POWER_SOURCE': 'TrAbsolutePowerSource',
        'TR_SPECIFIC_POWER_SOURCE': 'TrSpecificPowerSource'
    }

    def __init__(self, type='TR_SPECIFIC_POWER_SOURCE', name=None, heat_flux=None, topological_reference=None, geometry_primitive_uuids=None, heat_exchanger_mode=None, local_vars_configuration=None):  # noqa: E501
        """OneOfAdvancedConceptsPowerSources - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._heat_flux = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self._heat_exchanger_mode = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if heat_flux is not None:
            self.heat_flux = heat_flux
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids
        if heat_exchanger_mode is not None:
            self.heat_exchanger_mode = heat_exchanger_mode

    @property
    def type(self):
        """Gets the type of this OneOfAdvancedConceptsPowerSources.  # noqa: E501

        Schema name: TrSpecificPowerSource  # noqa: E501

        :return: The type of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfAdvancedConceptsPowerSources.

        Schema name: TrSpecificPowerSource  # noqa: E501

        :param type: The type of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfAdvancedConceptsPowerSources.  # noqa: E501


        :return: The name of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfAdvancedConceptsPowerSources.


        :param name: The name of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def heat_flux(self):
        """Gets the heat_flux of this OneOfAdvancedConceptsPowerSources.  # noqa: E501


        :return: The heat_flux of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :rtype: DimensionalFunctionVolumetricPower
        """
        return self._heat_flux

    @heat_flux.setter
    def heat_flux(self, heat_flux):
        """Sets the heat_flux of this OneOfAdvancedConceptsPowerSources.


        :param heat_flux: The heat_flux of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :type: DimensionalFunctionVolumetricPower
        """

        self._heat_flux = heat_flux

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfAdvancedConceptsPowerSources.  # noqa: E501


        :return: The topological_reference of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfAdvancedConceptsPowerSources.


        :param topological_reference: The topological_reference of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this OneOfAdvancedConceptsPowerSources.  # noqa: E501


        :return: The geometry_primitive_uuids of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this OneOfAdvancedConceptsPowerSources.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def heat_exchanger_mode(self):
        """Gets the heat_exchanger_mode of this OneOfAdvancedConceptsPowerSources.  # noqa: E501


        :return: The heat_exchanger_mode of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :rtype: OneOfHeatExchangerSourceHeatExchangerMode
        """
        return self._heat_exchanger_mode

    @heat_exchanger_mode.setter
    def heat_exchanger_mode(self, heat_exchanger_mode):
        """Sets the heat_exchanger_mode of this OneOfAdvancedConceptsPowerSources.


        :param heat_exchanger_mode: The heat_exchanger_mode of this OneOfAdvancedConceptsPowerSources.  # noqa: E501
        :type: OneOfHeatExchangerSourceHeatExchangerMode
        """

        self._heat_exchanger_mode = heat_exchanger_mode

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
        if not isinstance(other, OneOfAdvancedConceptsPowerSources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfAdvancedConceptsPowerSources):
            return True

        return self.to_dict() != other.to_dict()
