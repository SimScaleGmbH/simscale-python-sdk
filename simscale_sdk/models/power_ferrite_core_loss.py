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


class PowerFerriteCoreLoss(object):
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
        'steinmetz_constant': 'float',
        'frequency_exponent': 'float',
        'flux_density_exponent': 'float'
    }

    attribute_map = {
        'type': 'type',
        'steinmetz_constant': 'steinmetzConstant',
        'frequency_exponent': 'frequencyExponent',
        'flux_density_exponent': 'fluxDensityExponent'
    }

    def __init__(self, type='POWER_FERRITE', steinmetz_constant=None, frequency_exponent=None, flux_density_exponent=None, local_vars_configuration=None):  # noqa: E501
        """PowerFerriteCoreLoss - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._steinmetz_constant = None
        self._frequency_exponent = None
        self._flux_density_exponent = None
        self.discriminator = None

        self.type = type
        if steinmetz_constant is not None:
            self.steinmetz_constant = steinmetz_constant
        if frequency_exponent is not None:
            self.frequency_exponent = frequency_exponent
        if flux_density_exponent is not None:
            self.flux_density_exponent = flux_density_exponent

    @property
    def type(self):
        """Gets the type of this PowerFerriteCoreLoss.  # noqa: E501

        Schema name: PowerFerriteCoreLoss  # noqa: E501

        :return: The type of this PowerFerriteCoreLoss.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PowerFerriteCoreLoss.

        Schema name: PowerFerriteCoreLoss  # noqa: E501

        :param type: The type of this PowerFerriteCoreLoss.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def steinmetz_constant(self):
        """Gets the steinmetz_constant of this PowerFerriteCoreLoss.  # noqa: E501


        :return: The steinmetz_constant of this PowerFerriteCoreLoss.  # noqa: E501
        :rtype: float
        """
        return self._steinmetz_constant

    @steinmetz_constant.setter
    def steinmetz_constant(self, steinmetz_constant):
        """Sets the steinmetz_constant of this PowerFerriteCoreLoss.


        :param steinmetz_constant: The steinmetz_constant of this PowerFerriteCoreLoss.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                steinmetz_constant is not None and steinmetz_constant < 0):  # noqa: E501
            raise ValueError("Invalid value for `steinmetz_constant`, must be a value greater than or equal to `0`")  # noqa: E501

        self._steinmetz_constant = steinmetz_constant

    @property
    def frequency_exponent(self):
        """Gets the frequency_exponent of this PowerFerriteCoreLoss.  # noqa: E501


        :return: The frequency_exponent of this PowerFerriteCoreLoss.  # noqa: E501
        :rtype: float
        """
        return self._frequency_exponent

    @frequency_exponent.setter
    def frequency_exponent(self, frequency_exponent):
        """Sets the frequency_exponent of this PowerFerriteCoreLoss.


        :param frequency_exponent: The frequency_exponent of this PowerFerriteCoreLoss.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                frequency_exponent is not None and frequency_exponent < 0):  # noqa: E501
            raise ValueError("Invalid value for `frequency_exponent`, must be a value greater than or equal to `0`")  # noqa: E501

        self._frequency_exponent = frequency_exponent

    @property
    def flux_density_exponent(self):
        """Gets the flux_density_exponent of this PowerFerriteCoreLoss.  # noqa: E501


        :return: The flux_density_exponent of this PowerFerriteCoreLoss.  # noqa: E501
        :rtype: float
        """
        return self._flux_density_exponent

    @flux_density_exponent.setter
    def flux_density_exponent(self, flux_density_exponent):
        """Sets the flux_density_exponent of this PowerFerriteCoreLoss.


        :param flux_density_exponent: The flux_density_exponent of this PowerFerriteCoreLoss.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                flux_density_exponent is not None and flux_density_exponent < 0):  # noqa: E501
            raise ValueError("Invalid value for `flux_density_exponent`, must be a value greater than or equal to `0`")  # noqa: E501

        self._flux_density_exponent = flux_density_exponent

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
        if not isinstance(other, PowerFerriteCoreLoss):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PowerFerriteCoreLoss):
            return True

        return self.to_dict() != other.to_dict()
