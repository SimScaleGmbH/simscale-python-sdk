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


class OneOfFlowDomainBoundariesZMAX(object):
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
        'velocity': 'OneOfWallBCVelocity',
        'temperature': 'OneOfWallBCTemperature',
        'passive_scalars': 'list[FixedValuePSBC]',
        'phase_fraction': 'OneOfWallBCPhaseFraction',
        'turbulence_intensity': 'OneOfVelocityInletBCTurbulenceIntensity',
        'dissipation_type': 'OneOfVelocityInletBCDissipationType',
        'net_radiative_heat_flux': 'OneOfWallBCNetRadiativeHeatFlux',
        'radiative_intensity_ray': 'OneOfWallBCRadiativeIntensityRay',
        'topological_reference': 'TopologicalReference',
        'pressure': 'OneOfPressureOutletBCPressure',
        'pressure_rgh': 'OneOfPressureOutletBCPressureRgh',
        'gauge_pressure': 'OneOfPressureOutletBCGaugePressure',
        'gauge_pressure_rgh': 'OneOfPressureOutletBCGaugePressureRgh',
        'reference_velocity': 'DimensionalSpeed',
        'reference_height': 'DimensionalLength',
        'ground_roughness': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'velocity': 'velocity',
        'temperature': 'temperature',
        'passive_scalars': 'passiveScalars',
        'phase_fraction': 'phaseFraction',
        'turbulence_intensity': 'turbulenceIntensity',
        'dissipation_type': 'dissipationType',
        'net_radiative_heat_flux': 'netRadiativeHeatFlux',
        'radiative_intensity_ray': 'radiativeIntensityRay',
        'topological_reference': 'topologicalReference',
        'pressure': 'pressure',
        'pressure_rgh': 'pressureRgh',
        'gauge_pressure': 'gaugePressure',
        'gauge_pressure_rgh': 'gaugePressureRgh',
        'reference_velocity': 'referenceVelocity',
        'reference_height': 'referenceHeight',
        'ground_roughness': 'groundRoughness'
    }

    discriminator_value_class_map = {
        'VELOCITY_INLET_V3': 'VelocityInletBC',
        'PRESSURE_OUTLET_V30': 'PressureOutletBC',
        'WALL_V34': 'WallBC',
        'PERIODIC': 'PeriodicBC',
        'ATMOSPHERIC_BOUNDARY_LAYER_INLET': 'AtmosphericBoundaryLayerInletBC'
    }

    def __init__(self, type='ATMOSPHERIC_BOUNDARY_LAYER_INLET', name=None, velocity=None, temperature=None, passive_scalars=None, phase_fraction=None, turbulence_intensity=None, dissipation_type=None, net_radiative_heat_flux=None, radiative_intensity_ray=None, topological_reference=None, pressure=None, pressure_rgh=None, gauge_pressure=None, gauge_pressure_rgh=None, reference_velocity=None, reference_height=None, ground_roughness=None, local_vars_configuration=None):  # noqa: E501
        """OneOfFlowDomainBoundariesZMAX - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._velocity = None
        self._temperature = None
        self._passive_scalars = None
        self._phase_fraction = None
        self._turbulence_intensity = None
        self._dissipation_type = None
        self._net_radiative_heat_flux = None
        self._radiative_intensity_ray = None
        self._topological_reference = None
        self._pressure = None
        self._pressure_rgh = None
        self._gauge_pressure = None
        self._gauge_pressure_rgh = None
        self._reference_velocity = None
        self._reference_height = None
        self._ground_roughness = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if velocity is not None:
            self.velocity = velocity
        if temperature is not None:
            self.temperature = temperature
        if passive_scalars is not None:
            self.passive_scalars = passive_scalars
        if phase_fraction is not None:
            self.phase_fraction = phase_fraction
        if turbulence_intensity is not None:
            self.turbulence_intensity = turbulence_intensity
        if dissipation_type is not None:
            self.dissipation_type = dissipation_type
        if net_radiative_heat_flux is not None:
            self.net_radiative_heat_flux = net_radiative_heat_flux
        if radiative_intensity_ray is not None:
            self.radiative_intensity_ray = radiative_intensity_ray
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if pressure is not None:
            self.pressure = pressure
        if pressure_rgh is not None:
            self.pressure_rgh = pressure_rgh
        if gauge_pressure is not None:
            self.gauge_pressure = gauge_pressure
        if gauge_pressure_rgh is not None:
            self.gauge_pressure_rgh = gauge_pressure_rgh
        if reference_velocity is not None:
            self.reference_velocity = reference_velocity
        if reference_height is not None:
            self.reference_height = reference_height
        if ground_roughness is not None:
            self.ground_roughness = ground_roughness

    @property
    def type(self):
        """Gets the type of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501

        The atmospheric boundary layer boundary condition implements the standard logarithmic profile for the stream-wise wind velocity component with corresponding profiles for turbulence kinetic energy and specific dissipation rate, where the ground roughness effects are taken into account.  Schema name: AtmosphericBoundaryLayerInletBC  # noqa: E501

        :return: The type of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfFlowDomainBoundariesZMAX.

        The atmospheric boundary layer boundary condition implements the standard logarithmic profile for the stream-wise wind velocity component with corresponding profiles for turbulence kinetic energy and specific dissipation rate, where the ground roughness effects are taken into account.  Schema name: AtmosphericBoundaryLayerInletBC  # noqa: E501

        :param type: The type of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The name of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfFlowDomainBoundariesZMAX.


        :param name: The name of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def velocity(self):
        """Gets the velocity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The velocity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfWallBCVelocity
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this OneOfFlowDomainBoundariesZMAX.


        :param velocity: The velocity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfWallBCVelocity
        """

        self._velocity = velocity

    @property
    def temperature(self):
        """Gets the temperature of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The temperature of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfWallBCTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this OneOfFlowDomainBoundariesZMAX.


        :param temperature: The temperature of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfWallBCTemperature
        """

        self._temperature = temperature

    @property
    def passive_scalars(self):
        """Gets the passive_scalars of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501

        Please choose a boundary condition for passive scalar (T).  # noqa: E501

        :return: The passive_scalars of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: list[FixedValuePSBC]
        """
        return self._passive_scalars

    @passive_scalars.setter
    def passive_scalars(self, passive_scalars):
        """Sets the passive_scalars of this OneOfFlowDomainBoundariesZMAX.

        Please choose a boundary condition for passive scalar (T).  # noqa: E501

        :param passive_scalars: The passive_scalars of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: list[FixedValuePSBC]
        """

        self._passive_scalars = passive_scalars

    @property
    def phase_fraction(self):
        """Gets the phase_fraction of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The phase_fraction of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfWallBCPhaseFraction
        """
        return self._phase_fraction

    @phase_fraction.setter
    def phase_fraction(self, phase_fraction):
        """Sets the phase_fraction of this OneOfFlowDomainBoundariesZMAX.


        :param phase_fraction: The phase_fraction of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfWallBCPhaseFraction
        """

        self._phase_fraction = phase_fraction

    @property
    def turbulence_intensity(self):
        """Gets the turbulence_intensity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The turbulence_intensity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfVelocityInletBCTurbulenceIntensity
        """
        return self._turbulence_intensity

    @turbulence_intensity.setter
    def turbulence_intensity(self, turbulence_intensity):
        """Sets the turbulence_intensity of this OneOfFlowDomainBoundariesZMAX.


        :param turbulence_intensity: The turbulence_intensity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfVelocityInletBCTurbulenceIntensity
        """

        self._turbulence_intensity = turbulence_intensity

    @property
    def dissipation_type(self):
        """Gets the dissipation_type of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The dissipation_type of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfVelocityInletBCDissipationType
        """
        return self._dissipation_type

    @dissipation_type.setter
    def dissipation_type(self, dissipation_type):
        """Sets the dissipation_type of this OneOfFlowDomainBoundariesZMAX.


        :param dissipation_type: The dissipation_type of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfVelocityInletBCDissipationType
        """

        self._dissipation_type = dissipation_type

    @property
    def net_radiative_heat_flux(self):
        """Gets the net_radiative_heat_flux of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The net_radiative_heat_flux of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfWallBCNetRadiativeHeatFlux
        """
        return self._net_radiative_heat_flux

    @net_radiative_heat_flux.setter
    def net_radiative_heat_flux(self, net_radiative_heat_flux):
        """Sets the net_radiative_heat_flux of this OneOfFlowDomainBoundariesZMAX.


        :param net_radiative_heat_flux: The net_radiative_heat_flux of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfWallBCNetRadiativeHeatFlux
        """

        self._net_radiative_heat_flux = net_radiative_heat_flux

    @property
    def radiative_intensity_ray(self):
        """Gets the radiative_intensity_ray of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The radiative_intensity_ray of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfWallBCRadiativeIntensityRay
        """
        return self._radiative_intensity_ray

    @radiative_intensity_ray.setter
    def radiative_intensity_ray(self, radiative_intensity_ray):
        """Sets the radiative_intensity_ray of this OneOfFlowDomainBoundariesZMAX.


        :param radiative_intensity_ray: The radiative_intensity_ray of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfWallBCRadiativeIntensityRay
        """

        self._radiative_intensity_ray = radiative_intensity_ray

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The topological_reference of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfFlowDomainBoundariesZMAX.


        :param topological_reference: The topological_reference of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def pressure(self):
        """Gets the pressure of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The pressure of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfPressureOutletBCPressure
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this OneOfFlowDomainBoundariesZMAX.


        :param pressure: The pressure of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfPressureOutletBCPressure
        """

        self._pressure = pressure

    @property
    def pressure_rgh(self):
        """Gets the pressure_rgh of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The pressure_rgh of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfPressureOutletBCPressureRgh
        """
        return self._pressure_rgh

    @pressure_rgh.setter
    def pressure_rgh(self, pressure_rgh):
        """Sets the pressure_rgh of this OneOfFlowDomainBoundariesZMAX.


        :param pressure_rgh: The pressure_rgh of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfPressureOutletBCPressureRgh
        """

        self._pressure_rgh = pressure_rgh

    @property
    def gauge_pressure(self):
        """Gets the gauge_pressure of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The gauge_pressure of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfPressureOutletBCGaugePressure
        """
        return self._gauge_pressure

    @gauge_pressure.setter
    def gauge_pressure(self, gauge_pressure):
        """Sets the gauge_pressure of this OneOfFlowDomainBoundariesZMAX.


        :param gauge_pressure: The gauge_pressure of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfPressureOutletBCGaugePressure
        """

        self._gauge_pressure = gauge_pressure

    @property
    def gauge_pressure_rgh(self):
        """Gets the gauge_pressure_rgh of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The gauge_pressure_rgh of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: OneOfPressureOutletBCGaugePressureRgh
        """
        return self._gauge_pressure_rgh

    @gauge_pressure_rgh.setter
    def gauge_pressure_rgh(self, gauge_pressure_rgh):
        """Sets the gauge_pressure_rgh of this OneOfFlowDomainBoundariesZMAX.


        :param gauge_pressure_rgh: The gauge_pressure_rgh of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: OneOfPressureOutletBCGaugePressureRgh
        """

        self._gauge_pressure_rgh = gauge_pressure_rgh

    @property
    def reference_velocity(self):
        """Gets the reference_velocity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The reference_velocity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: DimensionalSpeed
        """
        return self._reference_velocity

    @reference_velocity.setter
    def reference_velocity(self, reference_velocity):
        """Sets the reference_velocity of this OneOfFlowDomainBoundariesZMAX.


        :param reference_velocity: The reference_velocity of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: DimensionalSpeed
        """

        self._reference_velocity = reference_velocity

    @property
    def reference_height(self):
        """Gets the reference_height of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The reference_height of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._reference_height

    @reference_height.setter
    def reference_height(self, reference_height):
        """Sets the reference_height of this OneOfFlowDomainBoundariesZMAX.


        :param reference_height: The reference_height of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: DimensionalLength
        """

        self._reference_height = reference_height

    @property
    def ground_roughness(self):
        """Gets the ground_roughness of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501


        :return: The ground_roughness of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._ground_roughness

    @ground_roughness.setter
    def ground_roughness(self, ground_roughness):
        """Sets the ground_roughness of this OneOfFlowDomainBoundariesZMAX.


        :param ground_roughness: The ground_roughness of this OneOfFlowDomainBoundariesZMAX.  # noqa: E501
        :type: DimensionalLength
        """

        self._ground_roughness = ground_roughness

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
        if not isinstance(other, OneOfFlowDomainBoundariesZMAX):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfFlowDomainBoundariesZMAX):
            return True

        return self.to_dict() != other.to_dict()