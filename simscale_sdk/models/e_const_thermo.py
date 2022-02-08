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


class EConstThermo(object):
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
        'specific_heat': 'DimensionalSpecificHeat',
        'equation_of_state': 'PerfectGasEquationOfState'
    }

    attribute_map = {
        'type': 'type',
        'specific_heat': 'specificHeat',
        'equation_of_state': 'equationOfState'
    }

    def __init__(self, type='ECONST', specific_heat=None, equation_of_state=None, local_vars_configuration=None):  # noqa: E501
        """EConstThermo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._specific_heat = None
        self._equation_of_state = None
        self.discriminator = None

        self.type = type
        if specific_heat is not None:
            self.specific_heat = specific_heat
        if equation_of_state is not None:
            self.equation_of_state = equation_of_state

    @property
    def type(self):
        """Gets the type of this EConstThermo.  # noqa: E501

        <br><p>The <b>Thermo models</b> are used to calculate the specific heat at constant pressure (<i>Cp</i>) for the fluid. The available models are:</p><p><b>hConst:</b> This model assumes a constant value for specific heat at fixed pressure (<i>Cp</i>). </p><p><b>eConst:</b> This model assumes a constant value for the specific heat at fixed volume (<i>Cv</i>). </p>  Schema name: EConstThermo  # noqa: E501

        :return: The type of this EConstThermo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EConstThermo.

        <br><p>The <b>Thermo models</b> are used to calculate the specific heat at constant pressure (<i>Cp</i>) for the fluid. The available models are:</p><p><b>hConst:</b> This model assumes a constant value for specific heat at fixed pressure (<i>Cp</i>). </p><p><b>eConst:</b> This model assumes a constant value for the specific heat at fixed volume (<i>Cv</i>). </p>  Schema name: EConstThermo  # noqa: E501

        :param type: The type of this EConstThermo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def specific_heat(self):
        """Gets the specific_heat of this EConstThermo.  # noqa: E501


        :return: The specific_heat of this EConstThermo.  # noqa: E501
        :rtype: DimensionalSpecificHeat
        """
        return self._specific_heat

    @specific_heat.setter
    def specific_heat(self, specific_heat):
        """Sets the specific_heat of this EConstThermo.


        :param specific_heat: The specific_heat of this EConstThermo.  # noqa: E501
        :type: DimensionalSpecificHeat
        """

        self._specific_heat = specific_heat

    @property
    def equation_of_state(self):
        """Gets the equation_of_state of this EConstThermo.  # noqa: E501


        :return: The equation_of_state of this EConstThermo.  # noqa: E501
        :rtype: PerfectGasEquationOfState
        """
        return self._equation_of_state

    @equation_of_state.setter
    def equation_of_state(self, equation_of_state):
        """Sets the equation_of_state of this EConstThermo.


        :param equation_of_state: The equation_of_state of this EConstThermo.  # noqa: E501
        :type: PerfectGasEquationOfState
        """

        self._equation_of_state = equation_of_state

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
        if not isinstance(other, EConstThermo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EConstThermo):
            return True

        return self.to_dict() != other.to_dict()
