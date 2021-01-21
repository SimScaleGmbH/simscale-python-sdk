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


class OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy(object):
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
        'limiter_coefficient': 'float'
    }

    attribute_map = {
        'type': 'type',
        'limiter_coefficient': 'limiterCoefficient'
    }

    discriminator_value_class_map = {
        'GAUSS_LINEAR_CORRECTED': 'GaussLinearCorrectedLaplacianScheme',
        'GAUSS_LINEAR_LIMITED_CORRECTED': 'GaussLinearLimitedCorrectedLaplacianScheme',
        'GAUSS_LINEAR_UNCORRECTED': 'GaussLinearUncorrectedLaplacianScheme'
    }

    def __init__(self, type='GAUSS_LINEAR_UNCORRECTED', limiter_coefficient=None, local_vars_configuration=None):  # noqa: E501
        """OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._limiter_coefficient = None
        self.discriminator = 'type'

        self.type = type
        if limiter_coefficient is not None:
            self.limiter_coefficient = limiter_coefficient

    @property
    def type(self):
        """Gets the type of this OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy.  # noqa: E501


        :return: The type of this OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy.


        :param type: The type of this OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def limiter_coefficient(self):
        """Gets the limiter_coefficient of this OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy.  # noqa: E501

        This property defines a limiter coefficient for the scheme. 1 ensures boundedness while 0 applies no limiting.  # noqa: E501

        :return: The limiter_coefficient of this OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy.  # noqa: E501
        :rtype: float
        """
        return self._limiter_coefficient

    @limiter_coefficient.setter
    def limiter_coefficient(self, limiter_coefficient):
        """Sets the limiter_coefficient of this OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy.

        This property defines a limiter coefficient for the scheme. 1 ensures boundedness while 0 applies no limiting.  # noqa: E501

        :param limiter_coefficient: The limiter_coefficient of this OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                limiter_coefficient is not None and limiter_coefficient > 1):  # noqa: E501
            raise ValueError("Invalid value for `limiter_coefficient`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                limiter_coefficient is not None and limiter_coefficient < 0):  # noqa: E501
            raise ValueError("Invalid value for `limiter_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._limiter_coefficient = limiter_coefficient

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
        if not isinstance(other, OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfLaplacianSchemesLaplacianAlphaEffEnthalpy):
            return True

        return self.to_dict() != other.to_dict()
