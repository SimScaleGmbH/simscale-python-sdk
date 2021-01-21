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


class DimensionalFunctionInitialConditionDomainsTemperature(object):
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
        '_global': 'DimensionalFunctionTemperature',
        'subdomains': 'list[SubdomainDimensionalFunctionInitialConditionTemperature]'
    }

    attribute_map = {
        '_global': 'global',
        'subdomains': 'subdomains'
    }

    def __init__(self, _global=None, subdomains=None, local_vars_configuration=None):  # noqa: E501
        """DimensionalFunctionInitialConditionDomainsTemperature - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__global = None
        self._subdomains = None
        self.discriminator = None

        if _global is not None:
            self._global = _global
        if subdomains is not None:
            self.subdomains = subdomains

    @property
    def _global(self):
        """Gets the _global of this DimensionalFunctionInitialConditionDomainsTemperature.  # noqa: E501


        :return: The _global of this DimensionalFunctionInitialConditionDomainsTemperature.  # noqa: E501
        :rtype: DimensionalFunctionTemperature
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this DimensionalFunctionInitialConditionDomainsTemperature.


        :param _global: The _global of this DimensionalFunctionInitialConditionDomainsTemperature.  # noqa: E501
        :type: DimensionalFunctionTemperature
        """

        self.__global = _global

    @property
    def subdomains(self):
        """Gets the subdomains of this DimensionalFunctionInitialConditionDomainsTemperature.  # noqa: E501


        :return: The subdomains of this DimensionalFunctionInitialConditionDomainsTemperature.  # noqa: E501
        :rtype: list[SubdomainDimensionalFunctionInitialConditionTemperature]
        """
        return self._subdomains

    @subdomains.setter
    def subdomains(self, subdomains):
        """Sets the subdomains of this DimensionalFunctionInitialConditionDomainsTemperature.


        :param subdomains: The subdomains of this DimensionalFunctionInitialConditionDomainsTemperature.  # noqa: E501
        :type: list[SubdomainDimensionalFunctionInitialConditionTemperature]
        """

        self._subdomains = subdomains

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
        if not isinstance(other, DimensionalFunctionInitialConditionDomainsTemperature):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DimensionalFunctionInitialConditionDomainsTemperature):
            return True

        return self.to_dict() != other.to_dict()
