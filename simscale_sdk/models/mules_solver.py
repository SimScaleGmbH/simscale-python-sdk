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


class MULESSolver(object):
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
        'alpha_correctors': 'int',
        'alpha_sub_cycles': 'int',
        'compression_coefficient': 'float',
        'isotropic_compression_coefficient': 'float',
        'semi_implicit': 'OneOfMULESSolverSemiImplicit'
    }

    attribute_map = {
        'type': 'type',
        'alpha_correctors': 'alphaCorrectors',
        'alpha_sub_cycles': 'alphaSubCycles',
        'compression_coefficient': 'compressionCoefficient',
        'isotropic_compression_coefficient': 'isotropicCompressionCoefficient',
        'semi_implicit': 'semiImplicit'
    }

    def __init__(self, type='MULES_V7', alpha_correctors=None, alpha_sub_cycles=None, compression_coefficient=None, isotropic_compression_coefficient=None, semi_implicit=None, local_vars_configuration=None):  # noqa: E501
        """MULESSolver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._alpha_correctors = None
        self._alpha_sub_cycles = None
        self._compression_coefficient = None
        self._isotropic_compression_coefficient = None
        self._semi_implicit = None
        self.discriminator = None

        self.type = type
        if alpha_correctors is not None:
            self.alpha_correctors = alpha_correctors
        if alpha_sub_cycles is not None:
            self.alpha_sub_cycles = alpha_sub_cycles
        if compression_coefficient is not None:
            self.compression_coefficient = compression_coefficient
        if isotropic_compression_coefficient is not None:
            self.isotropic_compression_coefficient = isotropic_compression_coefficient
        if semi_implicit is not None:
            self.semi_implicit = semi_implicit

    @property
    def type(self):
        """Gets the type of this MULESSolver.  # noqa: E501

        Schema name: MULESSolver  # noqa: E501

        :return: The type of this MULESSolver.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MULESSolver.

        Schema name: MULESSolver  # noqa: E501

        :param type: The type of this MULESSolver.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def alpha_correctors(self):
        """Gets the alpha_correctors of this MULESSolver.  # noqa: E501


        :return: The alpha_correctors of this MULESSolver.  # noqa: E501
        :rtype: int
        """
        return self._alpha_correctors

    @alpha_correctors.setter
    def alpha_correctors(self, alpha_correctors):
        """Sets the alpha_correctors of this MULESSolver.


        :param alpha_correctors: The alpha_correctors of this MULESSolver.  # noqa: E501
        :type: int
        """

        self._alpha_correctors = alpha_correctors

    @property
    def alpha_sub_cycles(self):
        """Gets the alpha_sub_cycles of this MULESSolver.  # noqa: E501


        :return: The alpha_sub_cycles of this MULESSolver.  # noqa: E501
        :rtype: int
        """
        return self._alpha_sub_cycles

    @alpha_sub_cycles.setter
    def alpha_sub_cycles(self, alpha_sub_cycles):
        """Sets the alpha_sub_cycles of this MULESSolver.


        :param alpha_sub_cycles: The alpha_sub_cycles of this MULESSolver.  # noqa: E501
        :type: int
        """

        self._alpha_sub_cycles = alpha_sub_cycles

    @property
    def compression_coefficient(self):
        """Gets the compression_coefficient of this MULESSolver.  # noqa: E501


        :return: The compression_coefficient of this MULESSolver.  # noqa: E501
        :rtype: float
        """
        return self._compression_coefficient

    @compression_coefficient.setter
    def compression_coefficient(self, compression_coefficient):
        """Sets the compression_coefficient of this MULESSolver.


        :param compression_coefficient: The compression_coefficient of this MULESSolver.  # noqa: E501
        :type: float
        """

        self._compression_coefficient = compression_coefficient

    @property
    def isotropic_compression_coefficient(self):
        """Gets the isotropic_compression_coefficient of this MULESSolver.  # noqa: E501


        :return: The isotropic_compression_coefficient of this MULESSolver.  # noqa: E501
        :rtype: float
        """
        return self._isotropic_compression_coefficient

    @isotropic_compression_coefficient.setter
    def isotropic_compression_coefficient(self, isotropic_compression_coefficient):
        """Sets the isotropic_compression_coefficient of this MULESSolver.


        :param isotropic_compression_coefficient: The isotropic_compression_coefficient of this MULESSolver.  # noqa: E501
        :type: float
        """

        self._isotropic_compression_coefficient = isotropic_compression_coefficient

    @property
    def semi_implicit(self):
        """Gets the semi_implicit of this MULESSolver.  # noqa: E501


        :return: The semi_implicit of this MULESSolver.  # noqa: E501
        :rtype: OneOfMULESSolverSemiImplicit
        """
        return self._semi_implicit

    @semi_implicit.setter
    def semi_implicit(self, semi_implicit):
        """Sets the semi_implicit of this MULESSolver.


        :param semi_implicit: The semi_implicit of this MULESSolver.  # noqa: E501
        :type: OneOfMULESSolverSemiImplicit
        """

        self._semi_implicit = semi_implicit

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
        if not isinstance(other, MULESSolver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MULESSolver):
            return True

        return self.to_dict() != other.to_dict()
