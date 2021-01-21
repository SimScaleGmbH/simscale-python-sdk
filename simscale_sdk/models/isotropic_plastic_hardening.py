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


class IsotropicPlasticHardening(object):
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
        'youngs_modulus': 'DimensionalFunctionPressure',
        'poissons_ratio': 'OneOfIsotropicPlasticHardeningPoissonsRatio',
        'von_mises_stress': 'DimensionalFunctionPressure'
    }

    attribute_map = {
        'type': 'type',
        'youngs_modulus': 'youngsModulus',
        'poissons_ratio': 'poissonsRatio',
        'von_mises_stress': 'vonMisesStress'
    }

    def __init__(self, type='ISOTROPIC', youngs_modulus=None, poissons_ratio=None, von_mises_stress=None, local_vars_configuration=None):  # noqa: E501
        """IsotropicPlasticHardening - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._youngs_modulus = None
        self._poissons_ratio = None
        self._von_mises_stress = None
        self.discriminator = None

        self.type = type
        if youngs_modulus is not None:
            self.youngs_modulus = youngs_modulus
        if poissons_ratio is not None:
            self.poissons_ratio = poissons_ratio
        if von_mises_stress is not None:
            self.von_mises_stress = von_mises_stress

    @property
    def type(self):
        """Gets the type of this IsotropicPlasticHardening.  # noqa: E501


        :return: The type of this IsotropicPlasticHardening.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IsotropicPlasticHardening.


        :param type: The type of this IsotropicPlasticHardening.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def youngs_modulus(self):
        """Gets the youngs_modulus of this IsotropicPlasticHardening.  # noqa: E501


        :return: The youngs_modulus of this IsotropicPlasticHardening.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._youngs_modulus

    @youngs_modulus.setter
    def youngs_modulus(self, youngs_modulus):
        """Sets the youngs_modulus of this IsotropicPlasticHardening.


        :param youngs_modulus: The youngs_modulus of this IsotropicPlasticHardening.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._youngs_modulus = youngs_modulus

    @property
    def poissons_ratio(self):
        """Gets the poissons_ratio of this IsotropicPlasticHardening.  # noqa: E501


        :return: The poissons_ratio of this IsotropicPlasticHardening.  # noqa: E501
        :rtype: OneOfIsotropicPlasticHardeningPoissonsRatio
        """
        return self._poissons_ratio

    @poissons_ratio.setter
    def poissons_ratio(self, poissons_ratio):
        """Sets the poissons_ratio of this IsotropicPlasticHardening.


        :param poissons_ratio: The poissons_ratio of this IsotropicPlasticHardening.  # noqa: E501
        :type: OneOfIsotropicPlasticHardeningPoissonsRatio
        """

        self._poissons_ratio = poissons_ratio

    @property
    def von_mises_stress(self):
        """Gets the von_mises_stress of this IsotropicPlasticHardening.  # noqa: E501


        :return: The von_mises_stress of this IsotropicPlasticHardening.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._von_mises_stress

    @von_mises_stress.setter
    def von_mises_stress(self, von_mises_stress):
        """Sets the von_mises_stress of this IsotropicPlasticHardening.


        :param von_mises_stress: The von_mises_stress of this IsotropicPlasticHardening.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._von_mises_stress = von_mises_stress

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
        if not isinstance(other, IsotropicPlasticHardening):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IsotropicPlasticHardening):
            return True

        return self.to_dict() != other.to_dict()
