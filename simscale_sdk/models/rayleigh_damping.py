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


class RayleighDamping(object):
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
        'alpha_coefficient': 'DimensionalDampingCoefficient',
        'beta_damping': 'DimensionalTime'
    }

    attribute_map = {
        'type': 'type',
        'alpha_coefficient': 'alphaCoefficient',
        'beta_damping': 'betaDamping'
    }

    def __init__(self, type='RAYLEIGH', alpha_coefficient=None, beta_damping=None, local_vars_configuration=None):  # noqa: E501
        """RayleighDamping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._alpha_coefficient = None
        self._beta_damping = None
        self.discriminator = None

        self.type = type
        if alpha_coefficient is not None:
            self.alpha_coefficient = alpha_coefficient
        if beta_damping is not None:
            self.beta_damping = beta_damping

    @property
    def type(self):
        """Gets the type of this RayleighDamping.  # noqa: E501


        :return: The type of this RayleighDamping.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RayleighDamping.


        :param type: The type of this RayleighDamping.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def alpha_coefficient(self):
        """Gets the alpha_coefficient of this RayleighDamping.  # noqa: E501


        :return: The alpha_coefficient of this RayleighDamping.  # noqa: E501
        :rtype: DimensionalDampingCoefficient
        """
        return self._alpha_coefficient

    @alpha_coefficient.setter
    def alpha_coefficient(self, alpha_coefficient):
        """Sets the alpha_coefficient of this RayleighDamping.


        :param alpha_coefficient: The alpha_coefficient of this RayleighDamping.  # noqa: E501
        :type: DimensionalDampingCoefficient
        """

        self._alpha_coefficient = alpha_coefficient

    @property
    def beta_damping(self):
        """Gets the beta_damping of this RayleighDamping.  # noqa: E501


        :return: The beta_damping of this RayleighDamping.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._beta_damping

    @beta_damping.setter
    def beta_damping(self, beta_damping):
        """Sets the beta_damping of this RayleighDamping.


        :param beta_damping: The beta_damping of this RayleighDamping.  # noqa: E501
        :type: DimensionalTime
        """

        self._beta_damping = beta_damping

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
        if not isinstance(other, RayleighDamping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RayleighDamping):
            return True

        return self.to_dict() != other.to_dict()
