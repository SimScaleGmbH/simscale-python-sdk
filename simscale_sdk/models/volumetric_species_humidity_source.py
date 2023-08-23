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


class VolumetricSpeciesHumiditySource(object):
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
        'water_vapor_mass_rate': 'DimensionalAbsoluteHumidityRate',
        'dry_air_mass_rate': 'DimensionalAbsoluteHumidityRate',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'water_vapor_mass_rate': 'waterVaporMassRate',
        'dry_air_mass_rate': 'dryAirMassRate',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids'
    }

    def __init__(self, type='VOLUMETRIC_SPECIES_MASS_FLOW_RATE', name=None, water_vapor_mass_rate=None, dry_air_mass_rate=None, topological_reference=None, geometry_primitive_uuids=None, local_vars_configuration=None):  # noqa: E501
        """VolumetricSpeciesHumiditySource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._water_vapor_mass_rate = None
        self._dry_air_mass_rate = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if water_vapor_mass_rate is not None:
            self.water_vapor_mass_rate = water_vapor_mass_rate
        if dry_air_mass_rate is not None:
            self.dry_air_mass_rate = dry_air_mass_rate
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def type(self):
        """Gets the type of this VolumetricSpeciesHumiditySource.  # noqa: E501

        <i>Humidity sources</i> can be used to simulate humidity generation or purification from a volume. Three types are available:<br><li><b>Species source</b> (recommended)</li>: Used when the mass of the species entering the fluid domain per second are known.<li><b>Absolute humidity source</b></li>: Used when the local change of the absolute humidity over time is known.<li><b>Specific humidity source</b></li>: Similar to absolute humidity source but for the specific humidity.  Schema name: VolumetricSpeciesHumiditySource  # noqa: E501

        :return: The type of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumetricSpeciesHumiditySource.

        <i>Humidity sources</i> can be used to simulate humidity generation or purification from a volume. Three types are available:<br><li><b>Species source</b> (recommended)</li>: Used when the mass of the species entering the fluid domain per second are known.<li><b>Absolute humidity source</b></li>: Used when the local change of the absolute humidity over time is known.<li><b>Specific humidity source</b></li>: Similar to absolute humidity source but for the specific humidity.  Schema name: VolumetricSpeciesHumiditySource  # noqa: E501

        :param type: The type of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this VolumetricSpeciesHumiditySource.  # noqa: E501


        :return: The name of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumetricSpeciesHumiditySource.


        :param name: The name of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def water_vapor_mass_rate(self):
        """Gets the water_vapor_mass_rate of this VolumetricSpeciesHumiditySource.  # noqa: E501


        :return: The water_vapor_mass_rate of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :rtype: DimensionalAbsoluteHumidityRate
        """
        return self._water_vapor_mass_rate

    @water_vapor_mass_rate.setter
    def water_vapor_mass_rate(self, water_vapor_mass_rate):
        """Sets the water_vapor_mass_rate of this VolumetricSpeciesHumiditySource.


        :param water_vapor_mass_rate: The water_vapor_mass_rate of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :type: DimensionalAbsoluteHumidityRate
        """

        self._water_vapor_mass_rate = water_vapor_mass_rate

    @property
    def dry_air_mass_rate(self):
        """Gets the dry_air_mass_rate of this VolumetricSpeciesHumiditySource.  # noqa: E501


        :return: The dry_air_mass_rate of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :rtype: DimensionalAbsoluteHumidityRate
        """
        return self._dry_air_mass_rate

    @dry_air_mass_rate.setter
    def dry_air_mass_rate(self, dry_air_mass_rate):
        """Sets the dry_air_mass_rate of this VolumetricSpeciesHumiditySource.


        :param dry_air_mass_rate: The dry_air_mass_rate of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :type: DimensionalAbsoluteHumidityRate
        """

        self._dry_air_mass_rate = dry_air_mass_rate

    @property
    def topological_reference(self):
        """Gets the topological_reference of this VolumetricSpeciesHumiditySource.  # noqa: E501


        :return: The topological_reference of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this VolumetricSpeciesHumiditySource.


        :param topological_reference: The topological_reference of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this VolumetricSpeciesHumiditySource.  # noqa: E501


        :return: The geometry_primitive_uuids of this VolumetricSpeciesHumiditySource.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this VolumetricSpeciesHumiditySource.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this VolumetricSpeciesHumiditySource.  # noqa: E501
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
        if not isinstance(other, VolumetricSpeciesHumiditySource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumetricSpeciesHumiditySource):
            return True

        return self.to_dict() != other.to_dict()
