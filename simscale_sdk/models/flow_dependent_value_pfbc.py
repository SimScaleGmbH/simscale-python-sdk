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


class FlowDependentValuePFBC(object):
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
        'lower_bound': 'float',
        'upper_bound': 'float'
    }

    attribute_map = {
        'type': 'type',
        'lower_bound': 'lowerBound',
        'upper_bound': 'upperBound'
    }

    def __init__(self, type='FLOW_DEPENDENT_VALUE', lower_bound=None, upper_bound=None, local_vars_configuration=None):  # noqa: E501
        """FlowDependentValuePFBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._lower_bound = None
        self._upper_bound = None
        self.discriminator = None

        self.type = type
        if lower_bound is not None:
            self.lower_bound = lower_bound
        if upper_bound is not None:
            self.upper_bound = upper_bound

    @property
    def type(self):
        """Gets the type of this FlowDependentValuePFBC.  # noqa: E501


        :return: The type of this FlowDependentValuePFBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FlowDependentValuePFBC.


        :param type: The type of this FlowDependentValuePFBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def lower_bound(self):
        """Gets the lower_bound of this FlowDependentValuePFBC.  # noqa: E501


        :return: The lower_bound of this FlowDependentValuePFBC.  # noqa: E501
        :rtype: float
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, lower_bound):
        """Sets the lower_bound of this FlowDependentValuePFBC.


        :param lower_bound: The lower_bound of this FlowDependentValuePFBC.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                lower_bound is not None and lower_bound > 1):  # noqa: E501
            raise ValueError("Invalid value for `lower_bound`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lower_bound is not None and lower_bound < 0):  # noqa: E501
            raise ValueError("Invalid value for `lower_bound`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lower_bound = lower_bound

    @property
    def upper_bound(self):
        """Gets the upper_bound of this FlowDependentValuePFBC.  # noqa: E501


        :return: The upper_bound of this FlowDependentValuePFBC.  # noqa: E501
        :rtype: float
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, upper_bound):
        """Sets the upper_bound of this FlowDependentValuePFBC.


        :param upper_bound: The upper_bound of this FlowDependentValuePFBC.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                upper_bound is not None and upper_bound > 1):  # noqa: E501
            raise ValueError("Invalid value for `upper_bound`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                upper_bound is not None and upper_bound < 0):  # noqa: E501
            raise ValueError("Invalid value for `upper_bound`, must be a value greater than or equal to `0`")  # noqa: E501

        self._upper_bound = upper_bound

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
        if not isinstance(other, FlowDependentValuePFBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FlowDependentValuePFBC):
            return True

        return self.to_dict() != other.to_dict()
