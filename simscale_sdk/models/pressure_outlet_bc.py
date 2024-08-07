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


class PressureOutletBC(object):
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
        'pressure': 'OneOfPressureOutletBCPressure',
        'pressure_rgh': 'OneOfPressureOutletBCPressureRgh',
        'gauge_pressure': 'OneOfPressureOutletBCGaugePressure',
        'phase_fractions_v2': 'OneOfPressureOutletBCPhaseFractionsV2',
        'mass_fractions_v2': 'OutletBackFlowMFValues',
        'gauge_pressure_rgh': 'OneOfPressureOutletBCGaugePressureRgh',
        'net_radiative_heat_flux': 'OneOfPressureOutletBCNetRadiativeHeatFlux',
        'radiative_intensity_ray': 'OneOfPressureOutletBCRadiativeIntensityRay',
        'relative_humidity': 'InletOutletRHBC',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'pressure': 'pressure',
        'pressure_rgh': 'pressureRgh',
        'gauge_pressure': 'gaugePressure',
        'phase_fractions_v2': 'phaseFractionsV2',
        'mass_fractions_v2': 'massFractionsV2',
        'gauge_pressure_rgh': 'gaugePressureRgh',
        'net_radiative_heat_flux': 'netRadiativeHeatFlux',
        'radiative_intensity_ray': 'radiativeIntensityRay',
        'relative_humidity': 'relativeHumidity',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='PRESSURE_OUTLET_V30', name=None, pressure=None, pressure_rgh=None, gauge_pressure=None, phase_fractions_v2=None, mass_fractions_v2=None, gauge_pressure_rgh=None, net_radiative_heat_flux=None, radiative_intensity_ray=None, relative_humidity=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """PressureOutletBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._pressure = None
        self._pressure_rgh = None
        self._gauge_pressure = None
        self._phase_fractions_v2 = None
        self._mass_fractions_v2 = None
        self._gauge_pressure_rgh = None
        self._net_radiative_heat_flux = None
        self._radiative_intensity_ray = None
        self._relative_humidity = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if pressure is not None:
            self.pressure = pressure
        if pressure_rgh is not None:
            self.pressure_rgh = pressure_rgh
        if gauge_pressure is not None:
            self.gauge_pressure = gauge_pressure
        if phase_fractions_v2 is not None:
            self.phase_fractions_v2 = phase_fractions_v2
        if mass_fractions_v2 is not None:
            self.mass_fractions_v2 = mass_fractions_v2
        if gauge_pressure_rgh is not None:
            self.gauge_pressure_rgh = gauge_pressure_rgh
        if net_radiative_heat_flux is not None:
            self.net_radiative_heat_flux = net_radiative_heat_flux
        if radiative_intensity_ray is not None:
            self.radiative_intensity_ray = radiative_intensity_ray
        if relative_humidity is not None:
            self.relative_humidity = relative_humidity
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this PressureOutletBC.  # noqa: E501

        This boundary condition allows to specify a <b>pressure</b> value at an outlet boundary.  Schema name: PressureOutletBC  # noqa: E501

        :return: The type of this PressureOutletBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PressureOutletBC.

        This boundary condition allows to specify a <b>pressure</b> value at an outlet boundary.  Schema name: PressureOutletBC  # noqa: E501

        :param type: The type of this PressureOutletBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this PressureOutletBC.  # noqa: E501


        :return: The name of this PressureOutletBC.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PressureOutletBC.


        :param name: The name of this PressureOutletBC.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pressure(self):
        """Gets the pressure of this PressureOutletBC.  # noqa: E501


        :return: The pressure of this PressureOutletBC.  # noqa: E501
        :rtype: OneOfPressureOutletBCPressure
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this PressureOutletBC.


        :param pressure: The pressure of this PressureOutletBC.  # noqa: E501
        :type: OneOfPressureOutletBCPressure
        """

        self._pressure = pressure

    @property
    def pressure_rgh(self):
        """Gets the pressure_rgh of this PressureOutletBC.  # noqa: E501


        :return: The pressure_rgh of this PressureOutletBC.  # noqa: E501
        :rtype: OneOfPressureOutletBCPressureRgh
        """
        return self._pressure_rgh

    @pressure_rgh.setter
    def pressure_rgh(self, pressure_rgh):
        """Sets the pressure_rgh of this PressureOutletBC.


        :param pressure_rgh: The pressure_rgh of this PressureOutletBC.  # noqa: E501
        :type: OneOfPressureOutletBCPressureRgh
        """

        self._pressure_rgh = pressure_rgh

    @property
    def gauge_pressure(self):
        """Gets the gauge_pressure of this PressureOutletBC.  # noqa: E501


        :return: The gauge_pressure of this PressureOutletBC.  # noqa: E501
        :rtype: OneOfPressureOutletBCGaugePressure
        """
        return self._gauge_pressure

    @gauge_pressure.setter
    def gauge_pressure(self, gauge_pressure):
        """Sets the gauge_pressure of this PressureOutletBC.


        :param gauge_pressure: The gauge_pressure of this PressureOutletBC.  # noqa: E501
        :type: OneOfPressureOutletBCGaugePressure
        """

        self._gauge_pressure = gauge_pressure

    @property
    def phase_fractions_v2(self):
        """Gets the phase_fractions_v2 of this PressureOutletBC.  # noqa: E501


        :return: The phase_fractions_v2 of this PressureOutletBC.  # noqa: E501
        :rtype: OneOfPressureOutletBCPhaseFractionsV2
        """
        return self._phase_fractions_v2

    @phase_fractions_v2.setter
    def phase_fractions_v2(self, phase_fractions_v2):
        """Sets the phase_fractions_v2 of this PressureOutletBC.


        :param phase_fractions_v2: The phase_fractions_v2 of this PressureOutletBC.  # noqa: E501
        :type: OneOfPressureOutletBCPhaseFractionsV2
        """

        self._phase_fractions_v2 = phase_fractions_v2

    @property
    def mass_fractions_v2(self):
        """Gets the mass_fractions_v2 of this PressureOutletBC.  # noqa: E501


        :return: The mass_fractions_v2 of this PressureOutletBC.  # noqa: E501
        :rtype: OutletBackFlowMFValues
        """
        return self._mass_fractions_v2

    @mass_fractions_v2.setter
    def mass_fractions_v2(self, mass_fractions_v2):
        """Sets the mass_fractions_v2 of this PressureOutletBC.


        :param mass_fractions_v2: The mass_fractions_v2 of this PressureOutletBC.  # noqa: E501
        :type: OutletBackFlowMFValues
        """

        self._mass_fractions_v2 = mass_fractions_v2

    @property
    def gauge_pressure_rgh(self):
        """Gets the gauge_pressure_rgh of this PressureOutletBC.  # noqa: E501


        :return: The gauge_pressure_rgh of this PressureOutletBC.  # noqa: E501
        :rtype: OneOfPressureOutletBCGaugePressureRgh
        """
        return self._gauge_pressure_rgh

    @gauge_pressure_rgh.setter
    def gauge_pressure_rgh(self, gauge_pressure_rgh):
        """Sets the gauge_pressure_rgh of this PressureOutletBC.


        :param gauge_pressure_rgh: The gauge_pressure_rgh of this PressureOutletBC.  # noqa: E501
        :type: OneOfPressureOutletBCGaugePressureRgh
        """

        self._gauge_pressure_rgh = gauge_pressure_rgh

    @property
    def net_radiative_heat_flux(self):
        """Gets the net_radiative_heat_flux of this PressureOutletBC.  # noqa: E501


        :return: The net_radiative_heat_flux of this PressureOutletBC.  # noqa: E501
        :rtype: OneOfPressureOutletBCNetRadiativeHeatFlux
        """
        return self._net_radiative_heat_flux

    @net_radiative_heat_flux.setter
    def net_radiative_heat_flux(self, net_radiative_heat_flux):
        """Sets the net_radiative_heat_flux of this PressureOutletBC.


        :param net_radiative_heat_flux: The net_radiative_heat_flux of this PressureOutletBC.  # noqa: E501
        :type: OneOfPressureOutletBCNetRadiativeHeatFlux
        """

        self._net_radiative_heat_flux = net_radiative_heat_flux

    @property
    def radiative_intensity_ray(self):
        """Gets the radiative_intensity_ray of this PressureOutletBC.  # noqa: E501


        :return: The radiative_intensity_ray of this PressureOutletBC.  # noqa: E501
        :rtype: OneOfPressureOutletBCRadiativeIntensityRay
        """
        return self._radiative_intensity_ray

    @radiative_intensity_ray.setter
    def radiative_intensity_ray(self, radiative_intensity_ray):
        """Sets the radiative_intensity_ray of this PressureOutletBC.


        :param radiative_intensity_ray: The radiative_intensity_ray of this PressureOutletBC.  # noqa: E501
        :type: OneOfPressureOutletBCRadiativeIntensityRay
        """

        self._radiative_intensity_ray = radiative_intensity_ray

    @property
    def relative_humidity(self):
        """Gets the relative_humidity of this PressureOutletBC.  # noqa: E501


        :return: The relative_humidity of this PressureOutletBC.  # noqa: E501
        :rtype: InletOutletRHBC
        """
        return self._relative_humidity

    @relative_humidity.setter
    def relative_humidity(self, relative_humidity):
        """Sets the relative_humidity of this PressureOutletBC.


        :param relative_humidity: The relative_humidity of this PressureOutletBC.  # noqa: E501
        :type: InletOutletRHBC
        """

        self._relative_humidity = relative_humidity

    @property
    def topological_reference(self):
        """Gets the topological_reference of this PressureOutletBC.  # noqa: E501


        :return: The topological_reference of this PressureOutletBC.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this PressureOutletBC.


        :param topological_reference: The topological_reference of this PressureOutletBC.  # noqa: E501
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
        if not isinstance(other, PressureOutletBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PressureOutletBC):
            return True

        return self.to_dict() != other.to_dict()
