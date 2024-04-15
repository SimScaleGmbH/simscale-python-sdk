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


class OneOfCoupledConjugateHeatTransferBoundaryConditions(object):
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
        'turbulence': 'OneOfNaturalConvectionInletOutletBCTurbulence',
        'temperature': 'AmbientTBC',
        'passive_scalars': 'list[InletOutletPSBC]',
        'phase_fraction': 'OneOfWallBCPhaseFraction',
        'associated_phase_fractions': 'list[PhaseNameAndFixedValuePFBC]',
        'mass_fractions': 'list[FixedValueMassFractionBC]',
        'turbulence_intensity': 'OneOfVelocityInletBCTurbulenceIntensity',
        'dissipation_type': 'OneOfVelocityInletBCDissipationType',
        'net_radiative_heat_flux': 'OneOfNaturalConvectionInletOutletBCNetRadiativeHeatFlux',
        'radiative_intensity_ray': 'OpenBoundaryRayBC',
        'relative_humidity': 'InletOutletRHBC',
        'topological_reference': 'TopologicalReference',
        'pressure': 'FanPBC',
        'pressure_rgh': 'AmbientPBC',
        'gauge_pressure': 'FanPBC',
        'gauge_pressure_rgh': 'AmbientPBC',
        'electric_boundary_condition': 'OneOfWallBCElectricBoundaryCondition'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'velocity': 'velocity',
        'turbulence': 'turbulence',
        'temperature': 'temperature',
        'passive_scalars': 'passiveScalars',
        'phase_fraction': 'phaseFraction',
        'associated_phase_fractions': 'associatedPhaseFractions',
        'mass_fractions': 'massFractions',
        'turbulence_intensity': 'turbulenceIntensity',
        'dissipation_type': 'dissipationType',
        'net_radiative_heat_flux': 'netRadiativeHeatFlux',
        'radiative_intensity_ray': 'radiativeIntensityRay',
        'relative_humidity': 'relativeHumidity',
        'topological_reference': 'topologicalReference',
        'pressure': 'pressure',
        'pressure_rgh': 'pressureRgh',
        'gauge_pressure': 'gaugePressure',
        'gauge_pressure_rgh': 'gaugePressureRgh',
        'electric_boundary_condition': 'electricBoundaryCondition'
    }

    discriminator_value_class_map = {
        'VELOCITY_INLET_V3': 'VelocityInletBC',
        'VELOCITY_OUTLET_V7': 'VelocityOutletBC',
        'PRESSURE_INLET_V31': 'PressureInletBC',
        'PRESSURE_OUTLET_V30': 'PressureOutletBC',
        'WALL_V34': 'WallBC',
        'FAN': 'FanBC',
        'SYMMETRY': 'SymmetryBC',
        'NATURAL_CONVECTION_INLET_OUTLET': 'NaturalConvectionInletOutletBC'
    }

    def __init__(self, type='NATURAL_CONVECTION_INLET_OUTLET', name=None, velocity=None, turbulence=None, temperature=None, passive_scalars=None, phase_fraction=None, associated_phase_fractions=None, mass_fractions=None, turbulence_intensity=None, dissipation_type=None, net_radiative_heat_flux=None, radiative_intensity_ray=None, relative_humidity=None, topological_reference=None, pressure=None, pressure_rgh=None, gauge_pressure=None, gauge_pressure_rgh=None, electric_boundary_condition=None, local_vars_configuration=None):  # noqa: E501
        """OneOfCoupledConjugateHeatTransferBoundaryConditions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._velocity = None
        self._turbulence = None
        self._temperature = None
        self._passive_scalars = None
        self._phase_fraction = None
        self._associated_phase_fractions = None
        self._mass_fractions = None
        self._turbulence_intensity = None
        self._dissipation_type = None
        self._net_radiative_heat_flux = None
        self._radiative_intensity_ray = None
        self._relative_humidity = None
        self._topological_reference = None
        self._pressure = None
        self._pressure_rgh = None
        self._gauge_pressure = None
        self._gauge_pressure_rgh = None
        self._electric_boundary_condition = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if velocity is not None:
            self.velocity = velocity
        if turbulence is not None:
            self.turbulence = turbulence
        if temperature is not None:
            self.temperature = temperature
        if passive_scalars is not None:
            self.passive_scalars = passive_scalars
        if phase_fraction is not None:
            self.phase_fraction = phase_fraction
        if associated_phase_fractions is not None:
            self.associated_phase_fractions = associated_phase_fractions
        if mass_fractions is not None:
            self.mass_fractions = mass_fractions
        if turbulence_intensity is not None:
            self.turbulence_intensity = turbulence_intensity
        if dissipation_type is not None:
            self.dissipation_type = dissipation_type
        if net_radiative_heat_flux is not None:
            self.net_radiative_heat_flux = net_radiative_heat_flux
        if radiative_intensity_ray is not None:
            self.radiative_intensity_ray = radiative_intensity_ray
        if relative_humidity is not None:
            self.relative_humidity = relative_humidity
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
        if electric_boundary_condition is not None:
            self.electric_boundary_condition = electric_boundary_condition

    @property
    def type(self):
        """Gets the type of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501

        <p>This boundary condition is suitable for an <b>open boundary</b> where the air can enter or exit freely from or to the <b>atmosphere<b>. <a href='https://www.simscale.com/docs/simulation-setup/boundary-conditions/natural-convection-inlet-outlet/' target='_blank'>Learn more</a>.</P>  Schema name: NaturalConvectionInletOutletBC  # noqa: E501

        :return: The type of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfCoupledConjugateHeatTransferBoundaryConditions.

        <p>This boundary condition is suitable for an <b>open boundary</b> where the air can enter or exit freely from or to the <b>atmosphere<b>. <a href='https://www.simscale.com/docs/simulation-setup/boundary-conditions/natural-convection-inlet-outlet/' target='_blank'>Learn more</a>.</P>  Schema name: NaturalConvectionInletOutletBC  # noqa: E501

        :param type: The type of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The name of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param name: The name of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def velocity(self):
        """Gets the velocity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The velocity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: OneOfWallBCVelocity
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param velocity: The velocity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: OneOfWallBCVelocity
        """

        self._velocity = velocity

    @property
    def turbulence(self):
        """Gets the turbulence of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The turbulence of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: OneOfNaturalConvectionInletOutletBCTurbulence
        """
        return self._turbulence

    @turbulence.setter
    def turbulence(self, turbulence):
        """Sets the turbulence of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param turbulence: The turbulence of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: OneOfNaturalConvectionInletOutletBCTurbulence
        """

        self._turbulence = turbulence

    @property
    def temperature(self):
        """Gets the temperature of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The temperature of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: AmbientTBC
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param temperature: The temperature of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: AmbientTBC
        """

        self._temperature = temperature

    @property
    def passive_scalars(self):
        """Gets the passive_scalars of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501

        Please choose a boundary condition for passive scalar (T).  # noqa: E501

        :return: The passive_scalars of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: list[InletOutletPSBC]
        """
        return self._passive_scalars

    @passive_scalars.setter
    def passive_scalars(self, passive_scalars):
        """Sets the passive_scalars of this OneOfCoupledConjugateHeatTransferBoundaryConditions.

        Please choose a boundary condition for passive scalar (T).  # noqa: E501

        :param passive_scalars: The passive_scalars of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: list[InletOutletPSBC]
        """

        self._passive_scalars = passive_scalars

    @property
    def phase_fraction(self):
        """Gets the phase_fraction of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The phase_fraction of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: OneOfWallBCPhaseFraction
        """
        return self._phase_fraction

    @phase_fraction.setter
    def phase_fraction(self, phase_fraction):
        """Sets the phase_fraction of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param phase_fraction: The phase_fraction of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: OneOfWallBCPhaseFraction
        """

        self._phase_fraction = phase_fraction

    @property
    def associated_phase_fractions(self):
        """Gets the associated_phase_fractions of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501

        Please choose a boundary condition for phase fraction (alpha).  # noqa: E501

        :return: The associated_phase_fractions of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: list[PhaseNameAndFixedValuePFBC]
        """
        return self._associated_phase_fractions

    @associated_phase_fractions.setter
    def associated_phase_fractions(self, associated_phase_fractions):
        """Sets the associated_phase_fractions of this OneOfCoupledConjugateHeatTransferBoundaryConditions.

        Please choose a boundary condition for phase fraction (alpha).  # noqa: E501

        :param associated_phase_fractions: The associated_phase_fractions of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: list[PhaseNameAndFixedValuePFBC]
        """

        self._associated_phase_fractions = associated_phase_fractions

    @property
    def mass_fractions(self):
        """Gets the mass_fractions of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501

        Please choose a boundary condition for component mass density fraction.  # noqa: E501

        :return: The mass_fractions of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: list[FixedValueMassFractionBC]
        """
        return self._mass_fractions

    @mass_fractions.setter
    def mass_fractions(self, mass_fractions):
        """Sets the mass_fractions of this OneOfCoupledConjugateHeatTransferBoundaryConditions.

        Please choose a boundary condition for component mass density fraction.  # noqa: E501

        :param mass_fractions: The mass_fractions of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: list[FixedValueMassFractionBC]
        """

        self._mass_fractions = mass_fractions

    @property
    def turbulence_intensity(self):
        """Gets the turbulence_intensity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The turbulence_intensity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: OneOfVelocityInletBCTurbulenceIntensity
        """
        return self._turbulence_intensity

    @turbulence_intensity.setter
    def turbulence_intensity(self, turbulence_intensity):
        """Sets the turbulence_intensity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param turbulence_intensity: The turbulence_intensity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: OneOfVelocityInletBCTurbulenceIntensity
        """

        self._turbulence_intensity = turbulence_intensity

    @property
    def dissipation_type(self):
        """Gets the dissipation_type of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The dissipation_type of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: OneOfVelocityInletBCDissipationType
        """
        return self._dissipation_type

    @dissipation_type.setter
    def dissipation_type(self, dissipation_type):
        """Sets the dissipation_type of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param dissipation_type: The dissipation_type of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: OneOfVelocityInletBCDissipationType
        """

        self._dissipation_type = dissipation_type

    @property
    def net_radiative_heat_flux(self):
        """Gets the net_radiative_heat_flux of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The net_radiative_heat_flux of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: OneOfNaturalConvectionInletOutletBCNetRadiativeHeatFlux
        """
        return self._net_radiative_heat_flux

    @net_radiative_heat_flux.setter
    def net_radiative_heat_flux(self, net_radiative_heat_flux):
        """Sets the net_radiative_heat_flux of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param net_radiative_heat_flux: The net_radiative_heat_flux of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: OneOfNaturalConvectionInletOutletBCNetRadiativeHeatFlux
        """

        self._net_radiative_heat_flux = net_radiative_heat_flux

    @property
    def radiative_intensity_ray(self):
        """Gets the radiative_intensity_ray of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The radiative_intensity_ray of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: OpenBoundaryRayBC
        """
        return self._radiative_intensity_ray

    @radiative_intensity_ray.setter
    def radiative_intensity_ray(self, radiative_intensity_ray):
        """Sets the radiative_intensity_ray of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param radiative_intensity_ray: The radiative_intensity_ray of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: OpenBoundaryRayBC
        """

        self._radiative_intensity_ray = radiative_intensity_ray

    @property
    def relative_humidity(self):
        """Gets the relative_humidity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The relative_humidity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: InletOutletRHBC
        """
        return self._relative_humidity

    @relative_humidity.setter
    def relative_humidity(self, relative_humidity):
        """Sets the relative_humidity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param relative_humidity: The relative_humidity of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: InletOutletRHBC
        """

        self._relative_humidity = relative_humidity

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The topological_reference of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param topological_reference: The topological_reference of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def pressure(self):
        """Gets the pressure of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The pressure of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: FanPBC
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param pressure: The pressure of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: FanPBC
        """

        self._pressure = pressure

    @property
    def pressure_rgh(self):
        """Gets the pressure_rgh of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The pressure_rgh of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: AmbientPBC
        """
        return self._pressure_rgh

    @pressure_rgh.setter
    def pressure_rgh(self, pressure_rgh):
        """Sets the pressure_rgh of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param pressure_rgh: The pressure_rgh of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: AmbientPBC
        """

        self._pressure_rgh = pressure_rgh

    @property
    def gauge_pressure(self):
        """Gets the gauge_pressure of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The gauge_pressure of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: FanPBC
        """
        return self._gauge_pressure

    @gauge_pressure.setter
    def gauge_pressure(self, gauge_pressure):
        """Sets the gauge_pressure of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param gauge_pressure: The gauge_pressure of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: FanPBC
        """

        self._gauge_pressure = gauge_pressure

    @property
    def gauge_pressure_rgh(self):
        """Gets the gauge_pressure_rgh of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The gauge_pressure_rgh of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: AmbientPBC
        """
        return self._gauge_pressure_rgh

    @gauge_pressure_rgh.setter
    def gauge_pressure_rgh(self, gauge_pressure_rgh):
        """Sets the gauge_pressure_rgh of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param gauge_pressure_rgh: The gauge_pressure_rgh of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: AmbientPBC
        """

        self._gauge_pressure_rgh = gauge_pressure_rgh

    @property
    def electric_boundary_condition(self):
        """Gets the electric_boundary_condition of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501


        :return: The electric_boundary_condition of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :rtype: OneOfWallBCElectricBoundaryCondition
        """
        return self._electric_boundary_condition

    @electric_boundary_condition.setter
    def electric_boundary_condition(self, electric_boundary_condition):
        """Sets the electric_boundary_condition of this OneOfCoupledConjugateHeatTransferBoundaryConditions.


        :param electric_boundary_condition: The electric_boundary_condition of this OneOfCoupledConjugateHeatTransferBoundaryConditions.  # noqa: E501
        :type: OneOfWallBCElectricBoundaryCondition
        """

        self._electric_boundary_condition = electric_boundary_condition

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
        if not isinstance(other, OneOfCoupledConjugateHeatTransferBoundaryConditions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfCoupledConjugateHeatTransferBoundaryConditions):
            return True

        return self.to_dict() != other.to_dict()
