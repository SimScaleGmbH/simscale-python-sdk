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


class OneOfHConstThermoEquationOfState(object):
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
        'energy': 'str',
        'density': 'DimensionalDensity',
        'fluid_constant': 'DimensionalSpecificHeat',
        'reference_density': 'DimensionalDensity',
        'reference_pressure': 'DimensionalPressure',
        'isentropic_exponent': 'float',
        'pressure_offset': 'DimensionalPressure',
        'critical_temperature': 'DimensionalTemperature',
        'critical_volume': 'DimensionalMolarMass',
        'critical_pressure': 'DimensionalPressure',
        'acentric_factor': 'float'
    }

    attribute_map = {
        'type': 'type',
        'energy': 'energy',
        'density': 'density',
        'fluid_constant': 'fluidConstant',
        'reference_density': 'referenceDensity',
        'reference_pressure': 'referencePressure',
        'isentropic_exponent': 'isentropicExponent',
        'pressure_offset': 'pressureOffset',
        'critical_temperature': 'criticalTemperature',
        'critical_volume': 'criticalVolume',
        'critical_pressure': 'criticalPressure',
        'acentric_factor': 'acentricFactor'
    }

    discriminator_value_class_map = {
        'PERFECT_GAS': 'PerfectGasEquationOfState',
        'RHO_CONST': 'RhoConstEquationOfState',
        'PERFECT_FLUID': 'PerfectFluidEquationOfState',
        'INCOMPRESSIBLE_PERFECT_GAS': 'IncompressiblePerfectGasEquationOfState',
        'ADIABATIC_PERFECT_FLUID': 'AdiabaticPerfectFluidEquationOfState',
        'PENG_ROBINSON_GAS': 'PengRobinsonGasEquationOfState'
    }

    def __init__(self, type='PENG_ROBINSON_GAS', energy=None, density=None, fluid_constant=None, reference_density=None, reference_pressure=None, isentropic_exponent=None, pressure_offset=None, critical_temperature=None, critical_volume=None, critical_pressure=None, acentric_factor=None, local_vars_configuration=None):  # noqa: E501
        """OneOfHConstThermoEquationOfState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._energy = None
        self._density = None
        self._fluid_constant = None
        self._reference_density = None
        self._reference_pressure = None
        self._isentropic_exponent = None
        self._pressure_offset = None
        self._critical_temperature = None
        self._critical_volume = None
        self._critical_pressure = None
        self._acentric_factor = None
        self.discriminator = 'type'

        self.type = type
        if energy is not None:
            self.energy = energy
        if density is not None:
            self.density = density
        if fluid_constant is not None:
            self.fluid_constant = fluid_constant
        if reference_density is not None:
            self.reference_density = reference_density
        if reference_pressure is not None:
            self.reference_pressure = reference_pressure
        if isentropic_exponent is not None:
            self.isentropic_exponent = isentropic_exponent
        if pressure_offset is not None:
            self.pressure_offset = pressure_offset
        if critical_temperature is not None:
            self.critical_temperature = critical_temperature
        if critical_volume is not None:
            self.critical_volume = critical_volume
        if critical_pressure is not None:
            self.critical_pressure = critical_pressure
        if acentric_factor is not None:
            self.acentric_factor = acentric_factor

    @property
    def type(self):
        """Gets the type of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The type of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfHConstThermoEquationOfState.


        :param type: The type of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def energy(self):
        """Gets the energy of this OneOfHConstThermoEquationOfState.  # noqa: E501

        <p><b>Energy</b> provides the methods for the form of energy to be used. The options are:</p><p><b>Sensible enthalpy:</b> The enthalpy form of equation is used without the heat of formation. In most cases this is the recommended choice.</p><p><b>Sensible internal Energy:</b> The internal energy form of equation is used without the heat of formation but also incorporates energy change due to reactions.</p>  # noqa: E501

        :return: The energy of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: str
        """
        return self._energy

    @energy.setter
    def energy(self, energy):
        """Sets the energy of this OneOfHConstThermoEquationOfState.

        <p><b>Energy</b> provides the methods for the form of energy to be used. The options are:</p><p><b>Sensible enthalpy:</b> The enthalpy form of equation is used without the heat of formation. In most cases this is the recommended choice.</p><p><b>Sensible internal Energy:</b> The internal energy form of equation is used without the heat of formation but also incorporates energy change due to reactions.</p>  # noqa: E501

        :param energy: The energy of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: str
        """
        allowed_values = ["SENSIBLE_ENTHALPY", "SENSIBLE_INTERNAL_ENERGY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and energy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `energy` ({0}), must be one of {1}"  # noqa: E501
                .format(energy, allowed_values)
            )

        self._energy = energy

    @property
    def density(self):
        """Gets the density of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The density of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: DimensionalDensity
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this OneOfHConstThermoEquationOfState.


        :param density: The density of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: DimensionalDensity
        """

        self._density = density

    @property
    def fluid_constant(self):
        """Gets the fluid_constant of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The fluid_constant of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: DimensionalSpecificHeat
        """
        return self._fluid_constant

    @fluid_constant.setter
    def fluid_constant(self, fluid_constant):
        """Sets the fluid_constant of this OneOfHConstThermoEquationOfState.


        :param fluid_constant: The fluid_constant of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: DimensionalSpecificHeat
        """

        self._fluid_constant = fluid_constant

    @property
    def reference_density(self):
        """Gets the reference_density of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The reference_density of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: DimensionalDensity
        """
        return self._reference_density

    @reference_density.setter
    def reference_density(self, reference_density):
        """Sets the reference_density of this OneOfHConstThermoEquationOfState.


        :param reference_density: The reference_density of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: DimensionalDensity
        """

        self._reference_density = reference_density

    @property
    def reference_pressure(self):
        """Gets the reference_pressure of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The reference_pressure of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._reference_pressure

    @reference_pressure.setter
    def reference_pressure(self, reference_pressure):
        """Sets the reference_pressure of this OneOfHConstThermoEquationOfState.


        :param reference_pressure: The reference_pressure of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: DimensionalPressure
        """

        self._reference_pressure = reference_pressure

    @property
    def isentropic_exponent(self):
        """Gets the isentropic_exponent of this OneOfHConstThermoEquationOfState.  # noqa: E501

        Specify the isentropic exponent. This parameter characterizes changes in density due to pressure. A Larger isentropic exponent results in less sensitivity of the density to reference pressure.  # noqa: E501

        :return: The isentropic_exponent of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: float
        """
        return self._isentropic_exponent

    @isentropic_exponent.setter
    def isentropic_exponent(self, isentropic_exponent):
        """Sets the isentropic_exponent of this OneOfHConstThermoEquationOfState.

        Specify the isentropic exponent. This parameter characterizes changes in density due to pressure. A Larger isentropic exponent results in less sensitivity of the density to reference pressure.  # noqa: E501

        :param isentropic_exponent: The isentropic_exponent of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: float
        """

        self._isentropic_exponent = isentropic_exponent

    @property
    def pressure_offset(self):
        """Gets the pressure_offset of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The pressure_offset of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._pressure_offset

    @pressure_offset.setter
    def pressure_offset(self, pressure_offset):
        """Sets the pressure_offset of this OneOfHConstThermoEquationOfState.


        :param pressure_offset: The pressure_offset of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: DimensionalPressure
        """

        self._pressure_offset = pressure_offset

    @property
    def critical_temperature(self):
        """Gets the critical_temperature of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The critical_temperature of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._critical_temperature

    @critical_temperature.setter
    def critical_temperature(self, critical_temperature):
        """Sets the critical_temperature of this OneOfHConstThermoEquationOfState.


        :param critical_temperature: The critical_temperature of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._critical_temperature = critical_temperature

    @property
    def critical_volume(self):
        """Gets the critical_volume of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The critical_volume of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: DimensionalMolarMass
        """
        return self._critical_volume

    @critical_volume.setter
    def critical_volume(self, critical_volume):
        """Sets the critical_volume of this OneOfHConstThermoEquationOfState.


        :param critical_volume: The critical_volume of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: DimensionalMolarMass
        """

        self._critical_volume = critical_volume

    @property
    def critical_pressure(self):
        """Gets the critical_pressure of this OneOfHConstThermoEquationOfState.  # noqa: E501


        :return: The critical_pressure of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._critical_pressure

    @critical_pressure.setter
    def critical_pressure(self, critical_pressure):
        """Sets the critical_pressure of this OneOfHConstThermoEquationOfState.


        :param critical_pressure: The critical_pressure of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: DimensionalPressure
        """

        self._critical_pressure = critical_pressure

    @property
    def acentric_factor(self):
        """Gets the acentric_factor of this OneOfHConstThermoEquationOfState.  # noqa: E501

        Specify the acentric factor. It is a property of the material that characterized the changes in thermodynamic properties of the fluid due to non-spherical molecules.  # noqa: E501

        :return: The acentric_factor of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :rtype: float
        """
        return self._acentric_factor

    @acentric_factor.setter
    def acentric_factor(self, acentric_factor):
        """Sets the acentric_factor of this OneOfHConstThermoEquationOfState.

        Specify the acentric factor. It is a property of the material that characterized the changes in thermodynamic properties of the fluid due to non-spherical molecules.  # noqa: E501

        :param acentric_factor: The acentric_factor of this OneOfHConstThermoEquationOfState.  # noqa: E501
        :type: float
        """

        self._acentric_factor = acentric_factor

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
        if not isinstance(other, OneOfHConstThermoEquationOfState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfHConstThermoEquationOfState):
            return True

        return self.to_dict() != other.to_dict()
