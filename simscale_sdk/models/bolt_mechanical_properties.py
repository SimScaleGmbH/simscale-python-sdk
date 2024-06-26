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


class BoltMechanicalProperties(object):
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
        'youngs_modulus': 'DimensionalPressure',
        'poissons_ratio': 'float',
        'density': 'DimensionalDensity'
    }

    attribute_map = {
        'youngs_modulus': 'youngsModulus',
        'poissons_ratio': 'poissonsRatio',
        'density': 'density'
    }

    def __init__(self, youngs_modulus=None, poissons_ratio=None, density=None, local_vars_configuration=None):  # noqa: E501
        """BoltMechanicalProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._youngs_modulus = None
        self._poissons_ratio = None
        self._density = None
        self.discriminator = None

        if youngs_modulus is not None:
            self.youngs_modulus = youngs_modulus
        if poissons_ratio is not None:
            self.poissons_ratio = poissons_ratio
        if density is not None:
            self.density = density

    @property
    def youngs_modulus(self):
        """Gets the youngs_modulus of this BoltMechanicalProperties.  # noqa: E501


        :return: The youngs_modulus of this BoltMechanicalProperties.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._youngs_modulus

    @youngs_modulus.setter
    def youngs_modulus(self, youngs_modulus):
        """Sets the youngs_modulus of this BoltMechanicalProperties.


        :param youngs_modulus: The youngs_modulus of this BoltMechanicalProperties.  # noqa: E501
        :type: DimensionalPressure
        """

        self._youngs_modulus = youngs_modulus

    @property
    def poissons_ratio(self):
        """Gets the poissons_ratio of this BoltMechanicalProperties.  # noqa: E501

        Provide the Poisson's ratio value which describes the compression or elongation of the bolt material transverse to axial strain. Poisson's ratio can have a value within range from -1 to 0.5.  # noqa: E501

        :return: The poissons_ratio of this BoltMechanicalProperties.  # noqa: E501
        :rtype: float
        """
        return self._poissons_ratio

    @poissons_ratio.setter
    def poissons_ratio(self, poissons_ratio):
        """Sets the poissons_ratio of this BoltMechanicalProperties.

        Provide the Poisson's ratio value which describes the compression or elongation of the bolt material transverse to axial strain. Poisson's ratio can have a value within range from -1 to 0.5.  # noqa: E501

        :param poissons_ratio: The poissons_ratio of this BoltMechanicalProperties.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                poissons_ratio is not None and poissons_ratio >= 0.5):  # noqa: E501
            raise ValueError("Invalid value for `poissons_ratio`, must be a value less than `0.5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                poissons_ratio is not None and poissons_ratio <= -1):  # noqa: E501
            raise ValueError("Invalid value for `poissons_ratio`, must be a value greater than `-1`")  # noqa: E501

        self._poissons_ratio = poissons_ratio

    @property
    def density(self):
        """Gets the density of this BoltMechanicalProperties.  # noqa: E501


        :return: The density of this BoltMechanicalProperties.  # noqa: E501
        :rtype: DimensionalDensity
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this BoltMechanicalProperties.


        :param density: The density of this BoltMechanicalProperties.  # noqa: E501
        :type: DimensionalDensity
        """

        self._density = density

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
        if not isinstance(other, BoltMechanicalProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoltMechanicalProperties):
            return True

        return self.to_dict() != other.to_dict()
