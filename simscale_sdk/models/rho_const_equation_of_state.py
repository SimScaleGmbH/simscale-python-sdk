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


class RhoConstEquationOfState(object):
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
        'density': 'DimensionalDensity',
        'density_function': 'DimensionalFunctionDensity',
        'energy': 'str'
    }

    attribute_map = {
        'type': 'type',
        'density': 'density',
        'density_function': 'densityFunction',
        'energy': 'energy'
    }

    def __init__(self, type='RHO_CONST', density=None, density_function=None, energy=None, local_vars_configuration=None):  # noqa: E501
        """RhoConstEquationOfState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._density = None
        self._density_function = None
        self._energy = None
        self.discriminator = None

        self.type = type
        if density is not None:
            self.density = density
        if density_function is not None:
            self.density_function = density_function
        if energy is not None:
            self.energy = energy

    @property
    def type(self):
        """Gets the type of this RhoConstEquationOfState.  # noqa: E501

        <br><p>The <b>Equation of state</b> describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:</p><p><b>Rho const:</b> Fluid density is assumed constant.</p><p><b>Incompressibel perfect gas:</b> The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.</p><p><b>Perfect gas:</b> Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.</p><p><b>Perfect fluid:</b> Fluid density can change due to pressure and temperature with respect to a base value.</p><p><b>Adiabatic perfect fluid:</b> The fluid is a perfect fluid which is adiabatic in nature.</p> <a href='https://www.simscale.com/docs/simulation-setup/materials/thermophysical-fluid-models/#equation-of-state' target='_blank'>Learn more</a>.  Schema name: RhoConstEquationOfState  # noqa: E501

        :return: The type of this RhoConstEquationOfState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RhoConstEquationOfState.

        <br><p>The <b>Equation of state</b> describes the relation between density of a fluid and the fluid pressure and temperature. The available options are:</p><p><b>Rho const:</b> Fluid density is assumed constant.</p><p><b>Incompressibel perfect gas:</b> The fluid is assumed to be an 'Ideal Gas' that is incompressible by pressure. But, fluid density can change due to temperature.</p><p><b>Perfect gas:</b> Fluid is assumed to be an 'Ideal Gas' and obeys the 'Ideal Gas Law'.</p><p><b>Perfect fluid:</b> Fluid density can change due to pressure and temperature with respect to a base value.</p><p><b>Adiabatic perfect fluid:</b> The fluid is a perfect fluid which is adiabatic in nature.</p> <a href='https://www.simscale.com/docs/simulation-setup/materials/thermophysical-fluid-models/#equation-of-state' target='_blank'>Learn more</a>.  Schema name: RhoConstEquationOfState  # noqa: E501

        :param type: The type of this RhoConstEquationOfState.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def density(self):
        """Gets the density of this RhoConstEquationOfState.  # noqa: E501


        :return: The density of this RhoConstEquationOfState.  # noqa: E501
        :rtype: DimensionalDensity
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this RhoConstEquationOfState.


        :param density: The density of this RhoConstEquationOfState.  # noqa: E501
        :type: DimensionalDensity
        """

        self._density = density

    @property
    def density_function(self):
        """Gets the density_function of this RhoConstEquationOfState.  # noqa: E501


        :return: The density_function of this RhoConstEquationOfState.  # noqa: E501
        :rtype: DimensionalFunctionDensity
        """
        return self._density_function

    @density_function.setter
    def density_function(self, density_function):
        """Sets the density_function of this RhoConstEquationOfState.


        :param density_function: The density_function of this RhoConstEquationOfState.  # noqa: E501
        :type: DimensionalFunctionDensity
        """

        self._density_function = density_function

    @property
    def energy(self):
        """Gets the energy of this RhoConstEquationOfState.  # noqa: E501

        <p><b>Energy</b> provides the methods for the form of energy to be used. The options are:</p><p><b>Sensible enthalpy:</b> The enthalpy form of equation is used without the heat of formation. In most cases this is the recommended choice.</p><p><b>Sensible internal Energy:</b> The internal energy form of equation is used without the heat of formation but also incorporates energy change due to reactions.</p>  # noqa: E501

        :return: The energy of this RhoConstEquationOfState.  # noqa: E501
        :rtype: str
        """
        return self._energy

    @energy.setter
    def energy(self, energy):
        """Sets the energy of this RhoConstEquationOfState.

        <p><b>Energy</b> provides the methods for the form of energy to be used. The options are:</p><p><b>Sensible enthalpy:</b> The enthalpy form of equation is used without the heat of formation. In most cases this is the recommended choice.</p><p><b>Sensible internal Energy:</b> The internal energy form of equation is used without the heat of formation but also incorporates energy change due to reactions.</p>  # noqa: E501

        :param energy: The energy of this RhoConstEquationOfState.  # noqa: E501
        :type: str
        """

        self._energy = energy

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
        if not isinstance(other, RhoConstEquationOfState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RhoConstEquationOfState):
            return True

        return self.to_dict() != other.to_dict()
