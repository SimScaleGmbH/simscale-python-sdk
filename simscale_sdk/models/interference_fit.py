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


class InterferenceFit(object):
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
        'enable_interference_fit': 'bool',
        'closure': 'DimensionalFunctionLength'
    }

    attribute_map = {
        'enable_interference_fit': 'enableInterferenceFit',
        'closure': 'closure'
    }

    def __init__(self, enable_interference_fit=None, closure=None, local_vars_configuration=None):  # noqa: E501
        """InterferenceFit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_interference_fit = None
        self._closure = None
        self.discriminator = None

        if enable_interference_fit is not None:
            self.enable_interference_fit = enable_interference_fit
        if closure is not None:
            self.closure = closure

    @property
    def enable_interference_fit(self):
        """Gets the enable_interference_fit of this InterferenceFit.  # noqa: E501


        :return: The enable_interference_fit of this InterferenceFit.  # noqa: E501
        :rtype: bool
        """
        return self._enable_interference_fit

    @enable_interference_fit.setter
    def enable_interference_fit(self, enable_interference_fit):
        """Sets the enable_interference_fit of this InterferenceFit.


        :param enable_interference_fit: The enable_interference_fit of this InterferenceFit.  # noqa: E501
        :type: bool
        """

        self._enable_interference_fit = enable_interference_fit

    @property
    def closure(self):
        """Gets the closure of this InterferenceFit.  # noqa: E501


        :return: The closure of this InterferenceFit.  # noqa: E501
        :rtype: DimensionalFunctionLength
        """
        return self._closure

    @closure.setter
    def closure(self, closure):
        """Sets the closure of this InterferenceFit.


        :param closure: The closure of this InterferenceFit.  # noqa: E501
        :type: DimensionalFunctionLength
        """

        self._closure = closure

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
        if not isinstance(other, InterferenceFit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InterferenceFit):
            return True

        return self.to_dict() != other.to_dict()
